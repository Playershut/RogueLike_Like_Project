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

        self.sprite = pygame.sprite.Sprite()
        self.image = self.idle_anim[0]
        self.sprite.image = self.image
        self.frame = 0
        self.anim_type = IDLE
        self.right_faced = True
        self.rect = self.sprite.image.get_rect()
        self.sprite.rect = self.sprite.image.get_rect()

        self.speed = 0
        self.hp = 0
        self.dmg = 0
        self.attack_cooldown = 2 * FPS

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
        if self.anim_type == DMGD:
            self.image.fill((100, 100, 100, 0), special_flags=pygame.BLEND_RGBA_ADD)

        ALL_SPRITES.change_layer(self, self.rect.bottom)


class Hero(Entity):
    def __init__(self, race, typee, *group):
        super(Hero, self).__init__(race, typee, *group)
        self.speed = 10
        self.hp = 6
        self.dmg = 1

    def get_nearest_enemy(self, enemies_list):
        s_x, s_y = self.rect.midbottom  # self
        dist_to_nearest_enemy = 1000
        nearest_enemy = None
        for enemy in enemies_list:
            e_x, e_y = enemy.rect.midbottom  # enemy
            diff_x = e_x - s_x
            diff_y = e_y - s_y
            dist_to_enemy = (abs(diff_x) ** 2 + abs(diff_y) ** 2) ** 0.5
            if dist_to_enemy < dist_to_nearest_enemy:
                if (e_x > s_x and self.right_faced) or (s_x > e_x and not self.right_faced):
                    dist_to_nearest_enemy = dist_to_enemy
                    nearest_enemy = enemy
        if dist_to_nearest_enemy <= 75:
            return nearest_enemy
        return None

    def attack(self, enemies_list):
        nearest_enemy = self.get_nearest_enemy(enemies_list)
        if nearest_enemy and self.attack_cooldown == 0:
            nearest_enemy.hp -= self.dmg
            nearest_enemy.anim_type = DMGD

    def update(self, *args):
        super(Hero, self).update(*args)
        if self.hp <= 0:
            self.kill()
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


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
        self.dist_to_player = (abs(self.diff_x) ** 2 + abs(self.diff_y) ** 2) ** 0.5
        if 75 <= self.dist_to_player <= 250:
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

    def attack_player(self, player: Hero):
        if self.dist_to_player <= 75 and self.attack_cooldown == 0:
            player.hp -= self.dmg
            player.anim_type = DMGD

    def update(self, *args):
        super(Enemy, self).update(*args)
        if self.hp <= 0:
            self.kill()
            # Particle(self.rect.midtop, self.rect)
        self.move_to_player(args[1])
        self.attack_player(args[1])
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = TILES_IMAGE[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


# class Particle(pygame.sprite.Sprite):
#     def __init__(self, pos, entity_rect):
#         super().__init__(ALL_SPRITES)
#         self.image = SKULL_IMAGE
#         self.rect = self.image.get_rect()
#
#         self.velocity = [0, 0]
#         self.rect.x, self.rect.y = pos
#
#         self.entity_rect = entity_rect
#
#         self.gravity = GRAVITY
#
#     def update(self, *args):
#         self.velocity[1] += self.gravity
#
#         self.rect.x += self.velocity[0]
#         self.rect.y += self.velocity[1]
#
#         if not self.rect.colliderect(self.entity_rect):
#             self.kill()
