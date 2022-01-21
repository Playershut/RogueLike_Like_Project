from classes import *
from settings import *

choice_hero_id = 0  # 0 - герой не выбран, 1 - эльф, 2 - рыцарь, 3 - ящер, 4 - волшебник


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


def start_screen():
    global choice_hero_id
    background = pygame.transform.scale(load_image('startscreen_background_image.png'), (WIDTH, HEIGHT))
    SCREEN.blit(background, (0, 0))

    font = pygame.font.Font(None, 30)
    text_start_game = 'Выберите героя'
    start_game = font.render(text_start_game, True, pygame.Color('white'))
    rect_start_game = start_game.get_rect()
    rect_start_game.center = SCREEN.get_rect().center
    SCREEN.blit(start_game, rect_start_game)

    elf = pygame.transform.scale(load_image('heroes\\elf\\m\\idle_anim\\f0.png'), (96, 168))
    rect_elf = elf.get_rect().move(50, 390)
    SCREEN.blit(elf, rect_elf)

    knight = pygame.transform.scale(load_image('heroes\\knight\\m\\idle_anim\\f0.png'), (96, 168))
    rect_knight = knight.get_rect().move(255, 390)
    SCREEN.blit(knight, rect_knight)

    lizard = pygame.transform.scale(load_image('heroes\\lizard\\m\\idle_anim\\f0.png'), (96, 168))
    rect_lizard = lizard.get_rect().move(450, 390)
    SCREEN.blit(lizard, rect_lizard)

    wizzard = pygame.transform.scale(load_image('heroes\\wizzard\\m\\idle_anim\\f0.png'), (96, 168))
    rect_wizzard = wizzard.get_rect().move(645, 390)
    SCREEN.blit(wizzard, rect_wizzard)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_elf.collidepoint(event.pos):
                        choice_hero_id = 1
                        return
                    if rect_knight.collidepoint(event.pos):
                        choice_hero_id = 2
                        return
                    if rect_lizard.collidepoint(event.pos):
                        choice_hero_id = 3
                        return
                    if rect_wizzard.collidepoint(event.pos):
                        choice_hero_id = 4
                        return

        pygame.display.flip()
        CLOCK.tick(FPS)


pygame.display.set_caption('Roguelike Like')
pygame.font.init()

start_screen()

level_map = load_level('maps\\lvl_1.txt')
player, max_w, max_h = generate_level(load_level('maps\\lvl_1.txt'))

enemy = Enemy('undeads', 'zombie', ALL_SPRITES, ENEMIES_SPRITES)
enemy.rect.midbottom = (736, 544)
enemy.right_faced = False
enemies_list = [enemy]


if choice_hero_id == 1:
    HERO = Hero('elf', 'm', all_sprites, hero_sprites)
elif choice_hero_id == 2:
    HERO = Hero('knight', 'm', all_sprites, hero_sprites)
elif choice_hero_id == 3:
    HERO = Hero('lizard', 'm', all_sprites, hero_sprites)
elif choice_hero_id == 4:
    HERO = Hero('wizzard', 'm', all_sprites, hero_sprites)

HERO.rect.center = (0, 0)
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
            ((key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and HERO.attack_is_ready)):
        HERO.anim_type = IDLE
    if key[pygame.K_ESCAPE]:
        running = False

    SCREEN.fill((0, 0, 0))

    ALL_SPRITES.draw(SCREEN)
    ALL_SPRITES.update(ENEMIES_SPRITES, HERO, enemies_list)
    UI_SPRITES.draw(SCREEN)
    UI_SPRITES.update()

    camera.update(HERO)

    for sprite in ALL_SPRITES:
        camera.apply(sprite)

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
