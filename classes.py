import time

import pygame.transform

from settings import *


class Character(pygame.sprite.Sprite):
    def __init__(self, race, typee, *group):
        super().__init__(*group)
        if race in HEROES_RACES:
            path_to_hit_anim = f'heroes\\{race}\\{typee}\\hit_anim\\'
            path_to_idle_anim = f'heroes\\{race}\\{typee}\\idle_anim\\'
            path_to_run_anim = f'heroes\\{race}\\{typee}\\run_anim\\'

            self.frames_in_hit_anim = len(os.listdir('data\\' + path_to_hit_anim))
            self.frames_in_idle_anim = len(os.listdir('data\\' + path_to_idle_anim))
            self.frames_in_run_anim = len(os.listdir('data\\' + path_to_run_anim))

            self.hit_anim = [load_image(f'{path_to_hit_anim}f{i}.png') for i in
                             range(self.frames_in_hit_anim)]
            self.idle_anim = [load_image(f'{path_to_idle_anim}f{i}.png') for i in
                              range(self.frames_in_idle_anim)]
            self.run_anim = [load_image(f'{path_to_run_anim}f{i}.png') for i in
                             range(self.frames_in_run_anim)]
            self.is_hero = True
        else:
            path_to_idle_anim = f'enemies\\{race}\\{typee}\\idle_anim\\'
            path_to_run_anim = f'enemies\\{race}\\{typee}\\run_anim\\'

            self.frames_in_idle_anim = len(os.listdir('data\\' + path_to_idle_anim))
            self.frames_in_run_anim = len(os.listdir('data\\' + path_to_run_anim))

            self.idle_anim = [load_image(f'{path_to_idle_anim}f{i}.png') for i in
                              range(self.frames_in_idle_anim)]
            self.run_anim = [load_image(f'{path_to_run_anim}f{i}.png') for i in
                             range(self.frames_in_run_anim)]
            self.is_hero = False
        self.sprite = pygame.sprite.Sprite()
        self.image = self.idle_anim[0]
        self.sprite.image = self.image
        self.frame = 0
        self.anim_type = IDLE
        self.right_faced = True
        self.speed = 10
        self.rect = self.sprite.image.get_rect()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self, *args):
        if self.anim_type == RUN:
            self.image = pygame.transform.flip(
                self.run_anim[self.frame % self.frames_in_run_anim],
                not self.right_faced, False)
            self.frame += 1
        if self.anim_type == IDLE:
            self.image = pygame.transform.flip(
                self.idle_anim[self.frame % self.frames_in_idle_anim],
                not self.right_faced, False)
            self.frame += 1
        if self.is_hero:
            if pygame.sprite.spritecollideany(self.sprite, args[0]):
                self.image = pygame.transform.flip(
                    self.hit_anim[self.frame % self.frames_in_hit_anim],
                    not self.right_faced, False)
                self.frame += 1
        else:
            if args and pygame.sprite.spritecollideany(self.sprite, args[1]):
                bckp_img = self.image
                self.image = pygame.surface.Surface((16, 16))
                self.frame += 1
