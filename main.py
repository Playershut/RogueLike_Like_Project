from classes import *
from settings import *
from random import randint

pygame.display.set_caption('Roguelike Like')
pygame.font.init()

all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
walls_sprites = pygame.sprite.Group()
hero_sprites = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, all_sprites)
            elif level[y][x] == '#':
                Tile('wall', x, y, all_sprites, walls_sprites)
            elif level[y][x] == '@':
                Tile('empty', x, y, all_sprites)
                # new_player = Player(x, y)
    return new_player, x, y


def start_screen():
    background = pygame.transform.scale(load_image('startscreen_background_image.png'), (WIDTH, HEIGHT))
    SCREEN.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_start_game = 'Начать игру'
    start_game = font.render(text_start_game, True, pygame.Color('white'))
    rect_start_game = start_game.get_rect()
    rect_start_game.center = SCREEN.get_rect().center
    SCREEN.blit(start_game, rect_start_game)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_start_game.collidepoint(event.pos):
                        return
        pygame.display.flip()
        CLOCK.tick(FPS)


start_screen()

level_map = load_level('maps\\lvl_1.txt')
player, max_w, max_h = generate_level(load_level('maps\\lvl_1.txt'))


enemy = Enemy('undeads', 'big_zombie', all_sprites, enemies_sprites)
enemy.rect.midbottom = (736, 544)
enemy.right_faced = False

HERO = Hero('elf', 'm', all_sprites, hero_sprites)

running = True

frame_counter = 1

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
    if not ((key[pygame.K_UP] or key[pygame.K_w]) or (key[pygame.K_DOWN] or key[pygame.K_s]) or
            (key[pygame.K_LEFT] or key[pygame.K_a]) or (key[pygame.K_RIGHT] or key[pygame.K_d])):
        HERO.anim_type = IDLE

    SCREEN.fill((0, 0, 0))

    all_sprites.draw(SCREEN)
    all_sprites.update(enemies_sprites, HERO)

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
