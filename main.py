from classes import *
from settings import *

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Roguelike Like')

all_sprites = pygame.sprite.Group()

hero = Character('elf', 'f', all_sprites)

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
        hero.anim_type = RUN
        hero.right_faced = False
        hero.rect.right -= hero.speed
    if key[pygame.K_RIGHT]:
        hero.anim_type = RUN
        hero.right_faced = True
        hero.rect.right += hero.speed
    if key[pygame.K_SPACE]:
        hero.anim_type = HIT
    if not (key[pygame.K_UP], key[pygame.K_DOWN], key[pygame.K_LEFT], key[pygame.K_RIGHT]):
        hero.anim_type = IDLE

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    all_sprites.update()

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
