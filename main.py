import  pygame

class BaseSprite:
    def __init__(self, x, y, texture,speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

class Rocket(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed



galaxy_img = pygame.image.load("galaxy.jpg")
galaxy_img = pygame.transform.scale(galaxy_img, [700, 500])

window = pygame.display.set_mode([700, 500])

rocket = Rocket(250, 380, "rocket.png", 5, 80, 120)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        rocket.update()


    window.fill([104, 1, 14])


    window.blit(galaxy_img, [0, 0])
    rocket.draw(window)
    pygame.display.flip()


