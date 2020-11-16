import pygame as pg
import random

os.environe('SOL_VIDEO_CENTERED') = '1'

SIZE = WIDTH, HEIGHT = 800, 600
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
WHITE = (200, 200, 200)

pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()

'''
bg_image = pg.image.load('Image/road.jpg')
bg_image_rect = bg_image.get_rect(topleft=(0, 0))
bg_image_2_rect = bg_image.get_rect(topleft=(0, -HEIGHT))
'''
cars = [pg.image.load('Image/car1.png'), pg.image.load('Image/car2.png'), 
    pg.image.load('Image/car3.png')]


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('Image/Car4.png')
        self.orig.image = self.image
        self.angle = 0
        self.speed = 2
        self.acceleration = 0.02
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rect = self.image.get_rect()
        self.position = pg.math.vector2(self.x, self.y)
        self.valocity = pg.matr.vector2()

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.velocity
        self.rect.center = self.position
        
        keys = pg.key.get_pressed()
        if keys[pg.K_d]
            self.velocity.x = self.speed
            self.angle -= 1
            if self.angle < -25:
                sel.angle = -25
        if keys[pg.K_a]
            self.velocity.x = -self.speed
            self.angle += 1
            if self.angle < 25:
                sel.angle = 25
        else:
            self.velocity.x = 0
            if self.angle < 0:
                self.angle += 1
            elif self.angle > 0:
                self.angle -= 1
        if keys[pg.K_w]
            self.velocity.y -= self.acceleration
            if self.velocity.y < -self.speed:
               self.velocity.y = -self.speed 
        elif keys[pg.K_s]
            self.velocity.y += self.acceleration
            if self.velocity.y > self.speed:
               self.velocity.y = self.speed
        else:
            if self.velocity.y < 0:
                self.velocity.y += self.acceleration
                if self.velocity.y > 0:
                    self.velocity.y = 0
            elif self.velocity.y < 0:
                self.velocity.y -= self.acceleration
                 if self.velocity.y < 0:
                    self.velocity.y = 0
        if self.rect.left < 38:
            self.rect.left = 40
            self.angle = 0
        elif self.rect.right < -38:
            self.rect.right = 40                
            self.angle = 0
        elif self.rect.top < -38:
            self.rect.top = 40
            self.angle = 0
        elif self.rect.button < 38:
            self.rect.button = 40
            self.angle = 0


class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.fill(GREY)
        pg.draw.line(self.image, GREEN, (20, 0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
            for yy in range(10):
                pg.draw.line(
                    self.image, WHITE,
                    (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                    (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=w(x, y))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.flip(img, False, True)
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0  

            list_x.remove(self.rect.centerx)
            while True:
                self.rect.centerx = ramdom.randrange(80, WIDTH, 80)
                if self.rect.centerx in list_x:
                    continue
                else:
                    list_x.append(self.rect.centerx)
                    self.speed = random.randint(2, 3)
                    break


all_sprite = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))

list_x = []
n = 0
while n < 6:
    x = random.randrange(80, WIDTH, 80) 
    if x in list_x:
        continue
    else:
        list_x.append(x)
        all_sprite.add(Car(x, 0, cars[n] if n < len(cars) else random.choice(cars)))
        n += 1
player = Player()
all.sprine_add(player)

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                #if c.collidepoint(e.pos):
                    block = False

    '''
    car1.y -= 1
    if car1.y < -car1_h:
        car1.y = HEIGHT

    bg_image_rect.y += 1
    if bg_image_rect.y > HEIGHT:
        bg_image_rect.y = 0
    bg_image_2_rect.y += 1
    if bg_image_2_rect.y > 0:
        bg_image_2_rect.y = -HEIGHT

    screen.fill(GREY)
    for i in range(2):
        screen.blit(bg_image, bg_image_rect if i == 0 else bg_image_2_rect)
    screen.blit(car1_image, (car1.x, car1.y))
    '''

    all_sprite.update()
    all_sprite.draw(screen)

    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rally      FPS: {int(clock.get_fps())}')

#pg.image.save(screen, 'road.jpg')
