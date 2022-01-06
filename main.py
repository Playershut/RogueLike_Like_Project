from classes import *
from settings import *
from random import randint

pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
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

hero = Entity('elf', 'm', all_sprites, hero_sprites)
enemy = Entity('demons', 'mimic', all_sprites, enemies_sprites)
enemy.rect.midbottom = (736, 544)
enemy.right_faced = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] or key[pygame.K_w]:
        hero.anim_type = RUN
        hero.rect.top -= hero.speed
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        hero.anim_type = RUN
        hero.rect.top += hero.speed
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        hero.right_faced = False
        hero.anim_type = RUN
        hero.rect.right -= hero.speed
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        hero.right_faced = True
        hero.anim_type = RUN
        hero.rect.right += hero.speed
    if not ((key[pygame.K_UP] or key[pygame.K_w]) or (key[pygame.K_DOWN] or key[pygame.K_s]) or
            (key[pygame.K_LEFT] or key[pygame.K_a]) or (key[pygame.K_RIGHT] or key[pygame.K_d])):
        hero.anim_type = IDLE

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    all_sprites.update(enemies_sprites, hero_sprites)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
