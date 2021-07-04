import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprites = []
        self.is_animating = False
        self.falling = False
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping00.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping01.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping02.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping03.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping04.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping05.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping06.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping07.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping08.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping09.png'))
        self.sprites.append(pygame.image.load('mario_jumping/sprite_mario-jumping10.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self, value):
        self.is_animating = value

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.08

            if self.current_sprite >= 7:
                self.falling = True

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.is_animating = False


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")
font = pygame.font.Font('PressStart2P.ttf', 24)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(150, 250)
initial_pos = 250
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.animate(True)

        if event.type == pygame.KEYUP:
            player.animate(False)

    i = 5
    while player.is_animating:
        player.pos_y -= 1 * i
        i -= 0.2
        if i < 0:
            i = 0

        if player.falling:
            while initial_pos > player.pos_y:
                j = 0.2

                player.pos_y += 1 * j
                j += 0.35
                if j > 2:
                    j = 2

            player.falling = False

        screen.fill((0, 0, 0))
        screen.blit(player.sprites[int(player.current_sprite)], (player.pos_x, player.pos_y))
        moving_sprites.update()
        pygame.display.flip()

    # Drawing
    screen.fill((0, 0, 0))
    instruction = font.render("PRESS SPACE TO JUMP", True, (255, 255, 255))
    instruction_rect = instruction.get_rect()
    instruction_rect.center = (300, 100)
    screen.blit(instruction, instruction_rect)
    screen.blit(player.sprites[int(player.current_sprite)], (player.pos_x, player.pos_y))
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
