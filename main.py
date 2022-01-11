from classes import *
from settings import *


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, ALL_SPRITES)
            elif level[y][x] == '#':
                Tile('wall', x, y, ALL_SPRITES, WALLS_SPRITES)
            elif level[y][x] == '@':
                Tile('empty', x, y, ALL_SPRITES)
                # new_player = Player(x, y)
    return new_player, x, y


pygame.display.set_caption('Roguelike Like')
pygame.font.init()

start_screen()

level_map = load_level('maps\\lvl_1.txt')
player, max_w, max_h = generate_level(load_level('maps\\lvl_1.txt'))

enemy = Enemy('undeads', 'big_zombie', ALL_SPRITES, ENEMIES_SPRITES)
enemy.rect.midbottom = (736, 544)
enemy.right_faced = False
enemies_list = [enemy]

HERO = Hero('elf', 'm', ALL_SPRITES, HERO_SPRITES)
camera = Camera()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_w]:
        HERO.anim_type = RUN
        HERO.rect.top -= HERO.speed
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        HERO.anim_type = RUN
        HERO.rect.top += HERO.speed
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        HERO.right_faced = False
        HERO.anim_type = RUN
        HERO.rect.right -= HERO.speed
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        HERO.right_faced = True
        HERO.anim_type = RUN
        HERO.rect.right += HERO.speed
    if key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
        HERO.attack(enemies_list)
    if not ((key[pygame.K_UP] or key[pygame.K_w]) or (key[pygame.K_DOWN] or key[pygame.K_s]) or
            (key[pygame.K_LEFT] or key[pygame.K_a]) or (key[pygame.K_RIGHT] or key[pygame.K_d]) or
            ((key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and HERO.attack_cooldown == 0)):
        HERO.anim_type = IDLE
    if key[pygame.K_ESCAPE]:
        running = False

    SCREEN.fill((0, 0, 0))

    ALL_SPRITES.draw(SCREEN)
    ALL_SPRITES.update(ENEMIES_SPRITES, HERO, enemies_list)

    camera.update(HERO)

    for sprite in ALL_SPRITES:
        camera.apply(sprite)

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
