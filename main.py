from pygame import *
from random import randint
window_height = 700
window_weight = 500
window = display.set_mode((window_height, window_weight))
mixer.init()
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
game = True
fps = 60
clock = time.Clock()
mixer.music.load('space.ogg')
font.init()
font2 = font.SysFont('Aerial', 36)
font1 = font.SysFont('Aerial', 36)
win = font1.render('YOU WIN!', True, (0, 0, 0))
lose = font1.render('YOU LOSE!', True, (0, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

racket = Player('saassadasd.png', 5, 5, 300, 10, 100)
racket2 = Player('saassadasd.png', 5, 685, 300, 10, 100)
ball = GameSprite('png-transparent-tennis-ball-tennis-balls-racket-drawing-football-green-yellow-circle-Photoroom.png-Photoroom.png', 4, 250, 350, 50, 50)

finish = False

while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket.update_l()
    racket2.update_r()
    racket.reset()
    racket2.reset()
    ball.reset()
    ball.update()
    display.update()
    clock.tick(fps)
        