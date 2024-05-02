import pygame
import sys
import os

# Variables
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)
main = True
worldx = 1280
worldy = 800
fps = 40
ani = 4


# Objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movey = 0
        self.image = pygame.image.load(os.path.join('images', 'player.png')).convert()
        self.rect = self.image.get_rect()

    def control(self, y):
        self.movey += y

    def update(self):
        self.rect.y = self.rect.y + self.movey


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'ball.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 120
        self.counter = 0

    def move(self):
        distance = 80
        speed = 8

        if 0 <= self.counter <= distance:
            self.rect.x += speed
        elif distance <= self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'enemy.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = 5
        self.counter = 0

    def move(self):
        distance = 75
        speed = 8

        if 0 <= self.counter <= distance:
            self.rect.y += speed
        elif distance <= self.counter <= distance * 2:
            self.rect.y -= speed
        else:
            self.counter = 0

        self.counter += 1


# Setup
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()
player = Player()
ball = Ball()
enemy = Enemy()
player.rect.x = 5
enemy_list = pygame.sprite.Group()
ball_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
player_list.add(player)
ball_list.add(ball)
enemy_list.add(enemy)

# Main loop
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(-10)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(10)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(10)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(-10)

    world.blit(backdrop, backdropbox)
    player.update()
    for e in ball_list:
        e.move()
    for e in enemy_list:
        e.move()
    enemy_list.draw(world)
    ball_list.draw(world)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
