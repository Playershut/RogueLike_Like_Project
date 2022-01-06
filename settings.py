import os
import sys

import pygame


# functions
# ---------------


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    image = pygame.transform.scale2x(pygame.transform.scale2x(image))

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# ---------------

# constants
# ---------------
WIDTH, HEIGHT = 800, 600

IDLE = 0
RUN = 1
HIT = 2
# ---------------

debug_display = pygame.display.set_mode((WIDTH, HEIGHT))

# dicts and lists
# ---------------
HEROES_RACES = ['elf', 'knight', 'lizard', 'wizzard']

ENTITY_ANIM_DICT = {
    # heroes
    'elf':
        {'m': {'hit_anim': load_image('heroes\\elf\\m\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\elf\\m\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\elf\\m\\idle_anim\\f{i}.png')
                   for i in range(4)]},
         'f': {'hit_anim': load_image('heroes\\elf\\f\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\elf\\f\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\elf\\f\\idle_anim\\f{i}.png')
                   for i in range(4)]}},
    'knight':
        {'m': {'hit_anim': load_image('heroes\\knight\\m\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\knight\\m\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\knight\\m\\idle_anim\\f{i}.png')
                   for i in range(4)]},
         'f': {'hit_anim': load_image('heroes\\knight\\f\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\knight\\f\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\knight\\f\\idle_anim\\f{i}.png')
                   for i in range(4)]}},
    'lizard':
        {'m': {'hit_anim': load_image('heroes\\lizard\\m\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\lizard\\m\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\lizard\\m\\idle_anim\\f{i}.png')
                   for i in range(4)]},
         'f': {'hit_anim': load_image('heroes\\knight\\f\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\lizard\\f\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\lizard\\f\\idle_anim\\f{i}.png')
                   for i in range(4)]}},
    'wizzard':
        {'m': {'hit_anim': load_image('heroes\\wizzard\\m\\hit_anim\\f0.png'),
               'run_anim': [
                   load_image(f'heroes\\wizzard\\m\\run_anim\\f{i}.png')
                   for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\wizzard\\m\\idle_anim\\f{i}.png')
                   for i in range(4)]},
         'f': {'hit_anim': load_image('heroes\\wizzard\\f\\hit_anim\\f0.png'),
               'run_anim': [load_image(f'heroes\\wizzard\\f\\run_anim\\f{i}.png')
                            for i in range(4)],
               'idle_anim': [
                   load_image(f'heroes\\wizzard\\f\\idle_anim\\f{i}.png')
                   for i in range(4)]}},
    # enemies
    'demons':
        {'big_demon':
             {'idle_anim': [load_image(f'enemies\\demons\\big_demon\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\big_demon\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'chort':
             {'idle_anim': [load_image(f'enemies\\demons\\chort\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\chort\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'imp':
             {'idle_anim': [load_image(f'enemies\\demons\\imp\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\imp\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'mimic':
             {'open_anim': [load_image(f'enemies\\demons\\mimic\\f{i}.png')
                            for i in range(3)]},
         'necromancer':
             {'idle_anim': [load_image(f'enemies\\demons\\necromancer\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\necromancer\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'wogol':
             {'idle_anim': [load_image(f'enemies\\demons\\wogol\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\wogol\\run_anim\\f{i}.png')
                           for i in range(4)]}},
    'orcs':
        {'goblin':
             {'idle_anim': [load_image(f'enemies\\orcs\\goblin\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\goblin\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'masked_orc':
             {'idle_anim': [load_image(f'enemies\\orcs\\masked_orc\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\masked_orc\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'ogre':
             {'idle_anim': [load_image(f'enemies\\orcs\\ogre\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\ogre\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'orc_shaman':
             {'idle_anim': [load_image(f'enemies\\orcs\\orc_shaman\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\orc_shaman\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'orc_warrior':
             {'idle_anim': [load_image(f'enemies\\orcs\\orc_warrior\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\orc_warrior\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'swampy':
             {'idle_anim': [load_image(f'enemies\\orcs\\swampy\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\swampy\\run_anim\\f{i}.png')
                           for i in range(4)]}},
    'undeads':
        {'big_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\big_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\big_zombie\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'ice_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\ice_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\ice_zombie\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'muddy':
             {'idle_anim': [load_image(f'enemies\\undeads\\muddy\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\muddy\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'skelet':
             {'idle_anim': [load_image(f'enemies\\undeads\\skelet\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\skelet\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'tiny_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\tiny_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\tiny_zombie\\run_anim\\f{i}.png')
                           for i in range(4)]},
         'zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\zombie\\run_anim\\f{i}.png')
                           for i in range(4)]}}
}

TILES_LIST = [load_image(f'environment\\tiles\\floor_{i}.png') for i in range(1, 9)]

# ---------------
