from pygame import *

#класс родитель
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
       

back = (200, 255, 255) 
window = display.set_mode((600,500))
window.fill(back)
clock = time.Clock()
#создания ракеток и меча
racket1 = Player('racket.png',30,200,50,150,4)
racket2 = Player('racket.png',520,200,50,150,4)
ball = GameSprite("tenis_ball.png", 200,200,50,50,4)

game = True
while game == True:
    for ex in event.get():
        if ex.type == QUIT:
            game = False

    window.fill(back)
    racket1.reset()###
    racket1.reset()###

    racket2.update_l()###
    racket2.update_l()###
    ball.reset()
    
    display.update()
    clock.tick(60)
    