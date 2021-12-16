import sys, pygame
from pygame.time import Clock
from pygame.math import Vector2
import pygame.draw
from dataclasses import dataclass
import pygame.locals as key
import time

@dataclass
class player:
    rect: pygame.Rect
    s:int=0
    """rect - прямоугольник s-скорость изменения кординты"""
    def update(self,width:int,height:int,dt:float):
        """Смешение ракетки"""
        self.rect.top += self.s * dt
        self.rect.clamp_ip(0,0,width,height)
    def __init__(self,width:int,height:int):
        """Инициализация входных значений"""
        self.rect=pygame.Rect(width,height,10,200)
    def draw(self,screen:pygame.Surface):
        """Вывод ракетки на экран"""
        pygame.draw.rect(screen,color,self.rect)
@dataclass
class ball:
    b: Vector2
    s:Vector2 =Vector2(0.3,0.3)
    c:Vector2 = Vector2(0,0)
    """b- кординта s- скорсть изменения c- счет"""
    def __init__(self,v:Vector2):
        """Инициализация входных значений"""
        self.b=v
    def draw(self,screen:pygame.Surface):
        """Вывод мяча на экран"""
        pygame.draw.circle(screen,color,(int(self.b[0]), int(self.b[1])),7)

    def update(self,dt:float,p1:player,p2:player,width:int,height:int):
        """Изменение кординаты мяча"""
        self.b+=self.s*dt
        if p1.rect.collidepoint(self.b):
            self.s[0]*=-1
        elif p2.rect.collidepoint(self.b):
            self.s[0]*=-1
        elif self.b[1] <=0 or self.b[1] >=height:
            self.s[1]*=-1
        if self.b[0]<0:
            self.c[0]+=1
            self.b=Vector2(width//2, height//2)
        elif self.b[0]>width:
            self.c[1]+=1
            self.b=Vector2(width//2, height//2)
            

if __name__ == '__main__':
    clock = Clock()
    pygame.init()
    pygame.font.init()
    size = width, height = 1280, 720
    start = time.time()
    clock = Clock()
    screen = pygame.display.set_mode(size)
    color = 255,255,255
    black=0,0,0
    basic_font = pygame.font.SysFont('arial', 36)
    p1=player(width-5,height//2)
    p2=player(5,height//2)
    b=ball(Vector2(width//2, height//2))
    while True:
        dt = clock.tick_busy_loop(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    """Обработка клавиш"""
                    if event.key == key.K_w:
                        p2.s = -1
                    elif event.key == key.K_s:
                        p2.s = 1
                    elif event.key == key.K_UP:
                        p1.s = -1
                    elif event.key == key.K_DOWN:
                        p1.s = 1
                elif event.type == pygame.KEYUP:
                    if event.key == key.K_w or event.key == key.K_s:
                        p2.s = 0
                    elif event.key == key.K_UP or event.key == key.K_DOWN:
                        p1.s = 0
        p1.update(width,height,dt)
        p2.update(width,height,dt)
        b.update(dt,p1,p2,width,height)
        screen.fill(black)
        pt1 = basic_font.render(f'{int(b.c[0])}',False,color)
        pt2 = basic_font.render(f'{int(b.c[1])}',False,color)
        screen.blit(pt1,(660,470))
        screen.blit(pt2,(560,470))
        p1.draw(screen)
        p2.draw(screen)
        b.draw(screen)
        pygame.display.flip()