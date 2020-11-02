import pygame as pg

SIZE = WIDTH, HEIGHT = 800, 600
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
WIDTH = (200, 200, 200)

pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()

bg_image = pg.image.load('Image/road.ing')
bg_image_rect = 


def bg():
    pg.draw.line(screen, GREEN, (20, 0), (20, 600), (40))
    pg.draw.line(screen, GREEN, (780, 0), (780, 600), (40))
    for xx in range(10):
        for yy in range(10):
            pg.draw.line(
                screen, WIDTH,
                (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Image/Car1.png')


car1 = Car()
car1_image = car1.image
car1_w, car1_h = car1.image.get_width(), car1.image.get_height()
print()
car1.x, car1.y = WIDTH // 2, HEIGHT // 2

game = True
while game:
    for e in pg.event.get():
        if e. type == pg.QUIT:
            game = False

    car1.y -= 1
    if car1.y < -car1_h:
        car1.y = HEIGHT

    screen.fill(GREY)
    bg()
    #screen.blit(car1_image, (car1.x, car1.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rully     FPS: {int(clock.get_fps())}')

pg.image.save(screen, 'road.jpg') 
