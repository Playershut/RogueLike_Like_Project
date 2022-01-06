import pygame.transform

from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, race, typee, *group):
        super().__init__(*group)

        if typee != 'mimic':
            self.idle_anim = ENTITY_ANIM_DICT[race][typee]['idle_anim']
            self.run_anim = ENTITY_ANIM_DICT[race][typee]['run_anim']
        else:
            self.run_anim = ENTITY_ANIM_DICT[race][typee]['open_anim']
            self.idle_anim = [self.run_anim[0]]

        self.hit_anim = ENTITY_ANIM_DICT[race][typee]['hit_anim'] if race in HEROES_RACES else None

        self.sprite = pygame.sprite.Sprite()
        self.image = self.idle_anim[0]
        self.sprite.image = self.image
        self.frame = 0
        self.anim_type = IDLE
        self.right_faced = True
        self.rect = self.sprite.image.get_rect()
        self.sprite.rect = self.sprite.image.get_rect()

        self.speed = 10
        self.hp = 6
        self.dmg = 1

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


class Enemy(Entity):
    pass


class Hero(Entity):
    pass
