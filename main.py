from classes import *
from settings import *
from random import randint

pygame.display.set_caption('Roguelike Like')

all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
walls_sprites = pygame.sprite.Group()
hero_sprites = pygame.sprite.Group()

for i in range(13):
    for j in range(10):
        tile = pygame.sprite.Sprite(all_sprites)
        tile.image = TILES_LIST[randint(0, 7)]
        tile.rect = tile.image.get_rect()
        tile.rect.topleft = (i * 64, j * 64)

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
