import pygame.transform

from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, race, typee, *group):
        super().__init__(*group)

        if typee != 'mimic':
            self.idle_anim = ENTITY_PARAMS_DICT[race][typee]['idle_anim']
            self.run_anim = ENTITY_PARAMS_DICT[race][typee]['run_anim']
        else:
            self.run_anim = ENTITY_PARAMS_DICT[race][typee]['open_anim']
            self.idle_anim = [self.run_anim[0]]

        self.hit_anim = ENTITY_PARAMS_DICT[race][typee]['hit_anim'] if race in HEROES_RACES else None

        self.sprite = pygame.sprite.Sprite()
        self.image = self.idle_anim[0]
        self.sprite.image = self.image
        self.frame = 0
        self.anim_type = IDLE
        self.right_faced = True
        self.rect = self.sprite.image.get_rect()
        self.sprite.rect = self.sprite.image.get_rect()

        self.speed = -1
        self.hp = -1
        self.dmg = -1

    def update(self, *args):
        if self.anim_type == RUN:
            self.image = pygame.transform.flip(
                self.run_anim[self.frame % len(self.run_anim)],
                not self.right_faced, False)
            self.frame += 1
        if self.anim_type == IDLE:
            self.image = pygame.transform.flip(
                self.idle_anim[self.frame % len(self.idle_anim)],
                not self.right_faced, False)
            self.frame += 1


class Hero(Entity):
    def __init__(self, race, typee, *group):
        super(Hero, self).__init__(race, typee, *group)
        self.speed = 10
        self.hp = 6
        self.dmg = 1


class Enemy(Entity):
    def __init__(self, race, typee, *group):
        super(Enemy, self).__init__(race, typee, *group)

        self.speed = ENTITY_PARAMS_DICT[race][typee]['speed']
        self.hp = ENTITY_PARAMS_DICT[race][typee]['hp']
        self.dmg = ENTITY_PARAMS_DICT[race][typee]['dmg']

    def can_see_player(self, player: Hero):
        p_x, p_y = player.rect.midbottom  # player
        s_x, s_y = self.rect.midbottom  # self
        self.diff_x = p_x - s_x
        self.diff_y = p_y - s_y
        dist_to_player = (abs(self.diff_x)**2 + abs(self.diff_y)**2)**0.5
        if 75 <= dist_to_player <= 250:
            self.anim_type = RUN
            return True
        self.anim_type = IDLE
        return False

    def move_to_player(self, player: Hero):
        if self.can_see_player(player):
            if self.diff_x > 0:
                self.rect.right += self.speed
                self.right_faced = True
            elif self.diff_x < 0:
                self.rect.right -= self.speed
                self.right_faced = False

            if self.diff_y > 0:
                self.rect.top += self.speed
            elif self.diff_y < 0:
                self.rect.top -= self.speed

    def update(self, *args):
        super(Enemy, self).update(*args)
        self.move_to_player(args[1])
