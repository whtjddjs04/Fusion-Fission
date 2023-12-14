import pygame
import random
from player import *
from display import *

class Enemy(pygame.sprite.Sprite):
    GRAVITY = 1
    SPRITES = load_sprite_sheets("Enemies", "AngryPig", 36, 30, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = random.choice(["left", "right"])
        self.animation_count = 0
        self.fall_count = 0
        self.hit = False
        self.hit_count = 0
        self.changedir = False
        self.angry = False
        
        self.speed = 2

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


    def make_hit(self):
        self.hit = True

    def landed(self):
        self.y_vel = 0

    def patrol(self):
        if self.direction == "left":
            self.x_vel -= self.speed
        if self.direction == "right":
            self.x_vel += self.speed

        if self.rect.x < 0:
            self.direction = "right"
        elif self.rect.right > WIDTH:
            self.direction = "left"

    def detect_dirchange(self):    
        if self.changedir == True:
            self.start = pygame.time.get_ticks()
            self.changedir = False
        now = pygame.time.get_ticks()
        if now - self.start >= 2000:
            self.direction = random.choice(["left", "right"])
            self.change = True

        return self.direction

       
    def check_screen(self, block_size):
        if self.rect.x < 0:
            self.direction = "right"
        elif self.rect.right > WIDTH:
            self.direction = "left"

        if self.rect.bottom > HEIGHT and self.rect.top == HEIGHT:
            self.rect.bottom = HEIGHT-block_size
        if self.rect.bottom > HEIGHT and self.rect.top < HEIGHT:
            pygame.time.delay(1000)
            self.rect.x = 100
            self.rect.y = 100

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "Idle"
        if self.hit:
            sprite_sheet = "Hit 1"
        elif self.x_vel != 0 and self.angry == False:
            sprite_sheet = "Walk"
        elif self.x_vel != 0 and self.angry == True:
            sprite_sheet = "Run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()
    
    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y)) 

def enemy_collide(enemy, objects, dx):
    enemy.move(dx, 0)
    enemy.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(enemy, obj):
            collided_object = obj
            break

    enemy.move(-dx, 0)
    enemy.update()
    return collided_object 

def enemy_state(player1, player2, enemy):
    distance1_x = player1.rect.x - enemy.rect.x
    distance1_y = player1.rect.y - enemy.rect.y
    distance1 = (distance1_x**2 + distance1_y**2) ** 0.5
    distance2_x = player2.rect.x - enemy.rect.x
    distance2_y = player2.rect.y - enemy.rect.y
    distance2 = (distance2_x**2 + distance2_y**2) ** 0.5

    if distance1 < 200 or distance2 < 200:
        enemy.angry = True
    elif distance1 > 200 and distance2 > 200:
        enemy.angry = False
