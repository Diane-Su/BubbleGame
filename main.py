import sys
import pygame
import random
from os import path
from pygame.sprite import collide_circle, spritecollide
# 初始化 initialize
# test commit
pygame.init()
size = width, height = 650, 500
background_color = (150, 150, 150)
begin_time = 0 
screen = pygame.display.set_mode(size)
font_name = pygame.font.match_font('Arial')
clock = pygame.time.Clock()
pop_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),'pop.wav'))
BOM_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),'BOM.ogg'))
ice_sound = pygame.mixer.Sound(path.join(path.dirname(__file__),'ice.wav'))
#bgm = pygame.mixer.music.load(path.join(path.dirname(__file__),'music.ogg'))
x, y = pygame.mouse.get_pos()
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,(255,255,255))
    text_rect =text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)
class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            path.join(path.dirname(__file__), "bubble.png"))
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,630)
        ,random.randint(10,470)
        )
        self.vec = [random.randint(-4,4),random.randint(-4,4)]
    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]
        if self.rect.y<0 or self.rect.bottom>height:
            self.vec[1] = - self.vec[1]
        if self.rect.x<0 or self.rect.right>width:
            self.vec[0] = - self.vec[0]
        pass
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            path.join(path.dirname(__file__),"ball2.png"))
        self.orign_image = self.image
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.frozen_time = 0
        self.isfrozen = 0
        self.score = 0
        self.confused_time = 0
        self.isconfused = 0 
        pygame.mouse.set_visible(True)
    def update(self):
        if self.isfrozen:
            if pygame.time.get_ticks()-self.frozen_time>3000:
                self.isfrozen=False
            pass 
        else:
            self.move()
            pass
        
        if self.isconfused:
            if pygame.time.get_ticks()-self.confused_time>5000:
                self.isconfused=False
            pass
    def move(self):
        x, y = pygame.mouse.get_pos()
        x_difference = x - self.rect.centerx
        y_difference = y - self.rect.centery
        x_difference = x_difference/10
        y_difference = y_difference/10 
        if self.isconfused:
            x_difference = x - self.rect.centerx
            y_difference = y - self.rect.centery
            x_difference = -x_difference/50
            y_difference = -y_difference/50
        self.rect.centerx = self.rect.centerx + x_difference
        self.rect.centery = self.rect.centery + y_difference     
    def bigger(self):
        ballCurrentPos = self.rect.center
        self.image = pygame.transform.scale(
        self.orign_image,(self.rect.w+1,self.rect.h+1))
        self.rect = self.image.get_rect()
        self.rect.center = ballCurrentPos
        self.score = self.score+1
        pass
    def smaller(self):
        ballCurrentPos = self.rect.center
        self.image = pygame.transform.scale(
        self.orign_image,(self.rect.w-3,self.rect.h-3))
        self.rect = self.image.get_rect()
        self.rect.center = ballCurrentPos
        self.score = self.score-2
        pass
    def stop(self):
        # frozen time
        self.frozen_time = pygame.time.get_ticks()
        self.isfrozen =True
        pass
    def confused(self):
        self.confused_time = pygame.time.get_ticks()
        self.isconfused =True 
class Badball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path.join(path.dirname(__file__),"炸彈.png"))
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,630)
        ,random.randint(10,470)
        )
        self.vec = [random.randint(-4,4),random.randint(-4,4)]
    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]
        if self.rect.y<0 or self.rect.bottom>height:
            self.vec[1] = - self.vec[1]
        if self.rect.x<0 or self.rect.right>width:
            self.vec[0] = - self.vec[0]
        pass
class Ice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path.join(path.dirname(__file__),"ice.png"))
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,630)
        ,random.randint(10,470)
        )
        self.vec = [random.randint(-4,4),random.randint(-4,4)]
    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]
        if self.rect.y<0 or self.rect.bottom>height:
            self.vec[1] = - self.vec[1]
        if self.rect.x<0 or self.rect.right>width:
            self.vec[0] = - self.vec[0]
        pass
class Lightning(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path.join(path.dirname(__file__),"lightning.png"))
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,630)
        ,random.randint(10,470)
        )
        self.vec = [random.randint(-4,4),random.randint(-4,4)]
    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]
        if self.rect.y<0 or self.rect.bottom>height:
            self.vec[1] = - self.vec[1]
        if self.rect.x<0 or self.rect.right>width:
            self.vec[0] = - self.vec[0]
        pass
bubble_group = pygame.sprite.Group()
badball_group = pygame.sprite.Group()
ice_group = pygame.sprite.Group()
lightning_group = pygame.sprite.Group()
ball = Ball()
all_sprite_group = pygame.sprite.Group()
all_sprite_group.add(ball)
# pygame.mixer.music.play()
# 迴圈開始
while 1:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 更新遊戲資料
    if len(bubble_group)<=6:
        # 產生Bubble
        bubble = Bubble()
        bubble_group.add(bubble)
    bubble_group.update()
    badball_group.update()
    ice_group.update()
    lightning_group.update()
    all_sprite_group.update()
    if len(badball_group)<=5:
        badball = Badball()
        badball_group.add(badball)
    if len(ice_group)<=2:
        ice = Ice()
        ice_group.add(ice)
    if len(lightning_group)<=2:
        lightning = Lightning()
        lightning_group.add(lightning)
     #碰撞
    collides = pygame.sprite.spritecollide(ball, bubble_group,False,
                                collided=pygame.sprite.
                                collide_circle_ratio(1))
    for bubble in collides:
        pop_sound.play()
        bubble.kill()
        ball.bigger()
    collides = pygame.sprite.spritecollide(ball, badball_group,False,
                                collided=pygame.sprite.
                                collide_circle_ratio(0.65))
    for badball in collides:
        BOM_sound.play()
        badball.kill()
        ball.smaller()
    collides = pygame.sprite.spritecollide(ball, ice_group,False,
                                collided=pygame.sprite.
                                collide_circle_ratio(0.75))
    for ice in collides:
        ice_sound.play()
        ice.kill()
        ball.stop()
    collides = pygame.sprite.spritecollide(ball, lightning_group,False,
                                collided=pygame.sprite.
                                collide_circle_ratio(0.65))
    for lightning in collides:
        lightning.kill()
        ball.confused()
    # 更新遊戲畫面
    screen.fill(background_color)
    all_sprite_group.draw(screen)
    bubble_group.draw(screen) #畫在螢幕上
    badball_group.draw(screen)
    ice_group.draw(screen)
    lightning_group.draw(screen)
    draw_text(screen,'Grade'+str(ball.score),36,500,300)
    pygame.display.flip()
    clock.tick(30)
