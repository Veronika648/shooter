import random

import pygame

desteroyed_enemy = 0
class Bullet:
    def __init__(self, speed, x, y, width, height, skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.bullets = []

    def draw(self, window):
        window.blit(self.skin, self.hitbox)
    def update(self):
        self.hitbox.y -= self.speed


class Player:
    def __init__(self, speed,
                 x, y,
                 width, height,
                 skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.bullets = []
    def draw(self, window):
        window.blit(self.skin, self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(10, self.hitbox.x+10, self.hitbox.y, 10, 20, "bullet.png"))
        for bullet in self.bullets:
            bullet.update()


class Enemy:
    def __init__(self, speed,
                 x, y,
                 width, height,
                 skin):
        self.speed = speed
        self.skin = pygame.image.load(skin)
        self.skin = pygame.transform.scale(self.skin, [width, height])
        self.hitbox = self.skin.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.skin, self.hitbox)


    def update(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 500:
            self.hitbox.y = -100
            self.hitbox.x = random.randint(0, 600)


def start_game():
    global missed_enemy, desteroyed_enemy


    pygame.init()
    window = pygame.display.set_mode([700, 500])
    clock = pygame.time.Clock()

    background_img = pygame.image.load("galaxy.jpg")
    background_img = pygame.transform.scale(background_img, [700, 500])
    game = True

    hero = Player(10, 500, 400, 60, 80, "rocket.png")

    enemies = []
    y =  50
    for i in range(10):
        enemies.append(Enemy(1, random.randint(0, 600), y, 50, 50, "ufo.png"))
        y -= 100

        desteroyed_text = pygame.font.Font(None, 20).render("Знищено:"+ str(desteroyed_enemy), True, [250, 250, 250])

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #
                print(pygame.mouse.get_pos())  #


        desteroyed_text = pygame.font.Font(None, 20).render("Знищено:"+ str(desteroyed_enemy), True, [250, 250, 250])

        for bullet in hero.bullets[:]:
            for enemy in enemies:
                if bullet.hitbox.colliderect(enemy.hitbox):
                    hero.bullets.remove(bullet)
                    enemy.hitbox.y = -100
                    enemy. hitbox.x = random.randint(0, 600)
                    desteroyed_enemy += 1



                    break


        hero.update()
        window.fill([123, 123,123 ])
        window.blit(background_img, [0,0])
        window.blit(desteroyed_text, [0, 0])

        hero.draw(window)

        for enemy in enemies:
            enemy.update()
            enemy.draw(window)


        pygame.display.flip()

        clock.tick(60)


