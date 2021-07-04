import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking00.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking01.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking02.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking03.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking04.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking05.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking06.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking07.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking08.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking09.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking10.png'))
        self.sprites.append(pygame.image.load('mario_walking/sprite_mario-walking11.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self, value):
        self.is_animating = value

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1250
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")
font = pygame.font.Font('PressStart2P.ttf', 24)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0, 300)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.animate(True)

        if event.type == pygame.KEYUP:
            player.animate(False)

    if player.is_animating:
        player.pos_x += 2

    # Drawing
    screen.fill((0, 0, 0))
    instruction = font.render("PRESS D TO WALK", True, (255, 255, 255))
    instruction_rect = instruction.get_rect()
    instruction_rect.center = (625, 100)
    screen.blit(instruction, instruction_rect)
    screen.blit(player.sprites[int(player.current_sprite)], (player.pos_x, player.pos_y))
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
