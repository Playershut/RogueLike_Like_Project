from classes import *
from settings import *

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Roguelike Like')

all_sprites = pygame.sprite.Group()
enemies_sprites = pygame.sprite.Group()
walls_sprites = pygame.sprite.Group()
hero_sprites = pygame.sprite.Group()

hero = Character('elf', 'm', all_sprites, hero_sprites)
enemy = Character('orc', 'ogre', all_sprites, enemies_sprites)
enemy.rect.bottomright = (450, 450)
enemy.right_faced = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        hero.anim_type = RUN
        hero.rect.top -= hero.speed
    if key[pygame.K_DOWN]:
        hero.anim_type = RUN
        hero.rect.top += hero.speed
    if key[pygame.K_LEFT]:
        hero.right_faced = False
        hero.anim_type = RUN
        hero.rect.right -= hero.speed
    if key[pygame.K_RIGHT]:
        hero.right_faced = True
        hero.anim_type = RUN
        hero.rect.right += hero.speed
    if not (key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
        hero.anim_type = IDLE

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    all_sprites.update(enemies_sprites, hero_sprites)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
