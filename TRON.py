import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

#  cycle_ride = pygame.mixer.Sound("sounds/light cycle sound.ogg")  # TODO

W, H = 1920, 1018
W_game_surf, H_game_surf = 1260, 880

BLACK = (0, 0, 0)
FRAME_COLOR = (108, 147, 146)

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("TRON")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

background = pygame.image.load("images/background.png").convert_alpha()

surf = pygame.Surface((1360, 950))
game_surf = pygame.Surface((W_game_surf, H_game_surf))


class Cycle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed


player_cycle = Cycle(W_game_surf // 2, H_game_surf - 55, 2, 'images/player_light_cycle.png')
# enemy_cycle = Cycle(W_game_surf // 2, 55, speed, 'images/enemy_light_cycle.png')

sc.fill(BLACK)
surf.fill(FRAME_COLOR)
pygame.display.update()

cycle_up = player_cycle.image
cycle_down = pygame.transform.flip(player_cycle.image, False, True)
cycle_left = pygame.transform.rotate(player_cycle.image, 90)
cycle_right = pygame.transform.rotate(player_cycle.image, -90)

direction = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()  # проверяю нажатие клавиш

    if keys[pygame.K_LEFT]:
        direction = 'left'
    elif keys[pygame.K_RIGHT]:
        direction = 'right'
    elif keys[pygame.K_UP]:
        direction = 'up'
    elif keys[pygame.K_DOWN]:
        direction = 'down'

    if direction == "left":
        player_cycle.image = cycle_left
        player_cycle.rect.x -= player_cycle.speed
    elif direction == "right":
        player_cycle.image = cycle_right
        player_cycle.rect.x += player_cycle.speed
    elif direction == "up":
        player_cycle.image = cycle_up
        player_cycle.rect.y -= player_cycle.speed
    elif direction == "down":
        player_cycle.image = cycle_down
        player_cycle.rect.y += player_cycle.speed
    else:
        player_cycle.image = cycle_up
        player_cycle.rect.y -= player_cycle.speed

    sc.blit(surf, (280, 28))
    surf.blit(game_surf, (50, 35))
    game_surf.blit(background, (0, 0))

    game_surf.blit(player_cycle.image, player_cycle.rect)
    # game_surf.blit(enemy_cycle.image, enemy_cycle.rect)

    pygame.display.update()

    clock.tick(FPS)
