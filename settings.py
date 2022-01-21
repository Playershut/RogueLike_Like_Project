import os
import sys

import pygame

pygame.init()

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


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

# ---------------

# constants
# ---------------
WIDTH, HEIGHT = 800, 600
TILE_WIDTH, TILE_HEIGHT = 64, 64  # 53, 54

IDLE = 0
RUN = 1
# HIT = 2
DMGD = 3

GRAVITY = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

SCREEN_RECT = (0, 0, WIDTH, HEIGHT)

FONT = pygame.font.Font('data\\fonts\\BahisyRegular.ttf', 36)

ALL_SPRITES = pygame.sprite.LayeredUpdates()
ENEMIES_SPRITES = pygame.sprite.Group()
WALLS_SPRITES = pygame.sprite.Group()
HERO_SPRITES = pygame.sprite.Group()
UI_SPRITES = pygame.sprite.Group()
UI_SPRITES_LIST = []

CLOCK = pygame.time.Clock()
FPS = 10

SKULL_IMAGE = load_image('ui\\skull.png')
# ---------------


# dicts and lists
# ---------------
UI_HEARTS = [load_image(f'ui\\ui_heart_{state}.png') for state in ('empty', 'half', 'full')]

HEROES_RACES = ['elf', 'knight', 'lizard', 'wizzard']

ENTITY_PARAMS_DICT = {
    # heroes
    'elf':
        {'m': {'run_anim': [
            load_image(f'heroes\\elf\\m\\run_anim\\f{i}.png')
            for i in range(4)],
            'idle_anim': [
                load_image(f'heroes\\elf\\m\\idle_anim\\f{i}.png')
                for i in range(4)]},
            'f': {'run_anim': [
                load_image(f'heroes\\elf\\f\\run_anim\\f{i}.png')
                for i in range(4)],
                'idle_anim': [
                    load_image(f'heroes\\elf\\f\\idle_anim\\f{i}.png')
                    for i in range(4)]}},
    'knight':
        {'m': {'run_anim': [
            load_image(f'heroes\\knight\\m\\run_anim\\f{i}.png')
            for i in range(4)],
            'idle_anim': [
                load_image(f'heroes\\knight\\m\\idle_anim\\f{i}.png')
                for i in range(4)]},
            'f': {'run_anim': [
                load_image(f'heroes\\knight\\f\\run_anim\\f{i}.png')
                for i in range(4)],
                'idle_anim': [
                    load_image(f'heroes\\knight\\f\\idle_anim\\f{i}.png')
                    for i in range(4)]}},
    'lizard':
        {'m': {'run_anim': [
            load_image(f'heroes\\lizard\\m\\run_anim\\f{i}.png')
            for i in range(4)],
            'idle_anim': [
                load_image(f'heroes\\lizard\\m\\idle_anim\\f{i}.png')
                for i in range(4)]},
            'f': {'run_anim': [
                load_image(f'heroes\\lizard\\f\\run_anim\\f{i}.png')
                for i in range(4)],
                'idle_anim': [
                    load_image(f'heroes\\lizard\\f\\idle_anim\\f{i}.png')
                    for i in range(4)]}},
    'wizzard':
        {'m': {'run_anim': [
            load_image(f'heroes\\wizzard\\m\\run_anim\\f{i}.png')
            for i in range(4)],
            'idle_anim': [
                load_image(f'heroes\\wizzard\\m\\idle_anim\\f{i}.png')
                for i in range(4)]},
            'f': {'run_anim': [load_image(f'heroes\\wizzard\\f\\run_anim\\f{i}.png')
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
                           for i in range(4)],
              'speed': 6,
              'hp': 3,
              'dmg': 2},
         'chort':
             {'idle_anim': [load_image(f'enemies\\demons\\chort\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\chort\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 7,
              'hp': 2,
              'dmg': 1},
         'imp':
             {'idle_anim': [load_image(f'enemies\\demons\\imp\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\imp\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 8,
              'hp': 1,
              'dmg': 1},
         'mimic':
             {'open_anim': [load_image(f'enemies\\demons\\mimic\\f{i}.png')
                            for i in range(3)],
              'speed': 0,
              'hp': 1,
              'dmg': 1},
         'necromancer':
             {'idle_anim': [load_image(f'enemies\\demons\\necromancer\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\necromancer\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 6,
              'hp': 2,
              'dmg': 2},
         'wogol':
             {'idle_anim': [load_image(f'enemies\\demons\\wogol\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\demons\\wogol\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 9,
              'hp': 1,
              'dmg': 1}},
    'orcs':
        {'goblin':
             {'idle_anim': [load_image(f'enemies\\orcs\\goblin\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\goblin\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 9,
              'hp': 1,
              'dmg': 1},
         'masked_orc':
             {'idle_anim': [load_image(f'enemies\\orcs\\masked_orc\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\masked_orc\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 7,
              'hp': 1,
              'dmg': 1},
         'ogre':
             {'idle_anim': [load_image(f'enemies\\orcs\\ogre\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\ogre\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 5,
              'hp': 3,
              'dmg': 2},
         'orc_shaman':
             {'idle_anim': [load_image(f'enemies\\orcs\\orc_shaman\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\orc_shaman\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 7,
              'hp': 1,
              'dmg': 1},
         'orc_warrior':
             {'idle_anim': [load_image(f'enemies\\orcs\\orc_warrior\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\orc_warrior\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 7,
              'hp': 2,
              'dmg': 2},
         'swampy':
             {'idle_anim': [load_image(f'enemies\\orcs\\swampy\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\orcs\\swampy\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 9,
              'hp': 1,
              'dmg': 1}},
    'undeads':
        {'big_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\big_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\big_zombie\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 4,
              'hp': 4,
              'dmg': 2},
         'ice_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\ice_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\ice_zombie\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 9,
              'hp': 1,
              'dmg': 1},
         'muddy':
             {'idle_anim': [load_image(f'enemies\\undeads\\muddy\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\muddy\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 9,
              'hp': 1,
              'dmg': 1},
         'skelet':
             {'idle_anim': [load_image(f'enemies\\undeads\\skelet\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\skelet\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 7,
              'hp': 1,
              'dmg': 1},
         'tiny_zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\tiny_zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\tiny_zombie\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 8,
              'hp': 1,
              'dmg': 1},
         'zombie':
             {'idle_anim': [load_image(f'enemies\\undeads\\zombie\\idle_anim\\f{i}.png')
                            for i in range(4)],
              'run_anim': [load_image(f'enemies\\undeads\\zombie\\run_anim\\f{i}.png')
                           for i in range(4)],
              'speed': 6,
              'hp': 2,
              'dmg': 1}}
}

# TILES_LIST = [load_image(f'environment\\tiles\\floor_{i}.png') for i in range(1, 9)]

TILES_IMAGE = {
    'wall': load_image('environment\\walls\\wall_mid.png'),
    'empty': load_image('environment\\tiles\\floor_3.png')
}
# ---------------
