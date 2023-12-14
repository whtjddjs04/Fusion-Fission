import pygame
import pygame.mixer
from display import *

PLAYER_VEL = 5
enemy_vel = 2

pygame.mixer.init()

sound_volume = 50

jump_sound = pygame.mixer.Sound('Fart Sound.mp3')
jump_sound.set_volume(sound_volume / 100.0)

landing_sound = pygame.mixer.Sound('Landing.mp3')
landing_sound.set_volume(sound_volume / 100.0)

hit_sound = pygame.mixer.Sound('Hit.wav')
hit_sound.set_volume(sound_volume / 100.0)

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.name = "player"
        self.has_landed = False

    def single_jump(self):
        self.y_vel = -self.GRAVITY * 6
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
            self.has_landed = False
        jump_sound.play()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

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

    def check_screen(self, block_size):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
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

    def landed(self):
        if not self.has_landed:
            landing_sound.play()
            self.has_landed = True

        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

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

class Player2(Player):
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
                 

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player1, player2, enemy, objects):
    keys = pygame.key.get_pressed()

    player1.x_vel = 0
    collide_left_p1 = collide(player1, objects, -PLAYER_VEL * 2)
    collide_right_p1 = collide(player1, objects, PLAYER_VEL * 2)
    vertical_collide_p1 = handle_vertical_collision(player1, objects, player1.y_vel)

    if keys[pygame.K_LEFT] and not collide_left_p1:
        player1.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right_p1:
        player1.move_right(PLAYER_VEL)

    player2.x_vel = 0
    collide_left_p2 = collide(player2, objects, -PLAYER_VEL * 2)
    collide_right_p2 = collide(player2, objects, PLAYER_VEL * 2)
    vertical_collide_p2 = handle_vertical_collision(player2, objects, player2.y_vel)

    if keys[pygame.K_a] and not collide_left_p2:
        player2.move_left(PLAYER_VEL)
    if keys[pygame.K_d] and not collide_right_p2:
        player2.move_right(PLAYER_VEL)


    collide_left_enemy = collide(enemy, objects, -enemy_vel * 2)
    collide_right_enemy= collide(enemy, objects, enemy_vel * 2)
    vertical_collide_enemy = handle_vertical_collision(enemy, objects, enemy.y_vel)

    if enemy.direction == "left" and not collide_left_enemy:
        enemy.move_left(3)
    if enemy.direction == "right" and not collide_right_enemy:
        enemy.move_right(3)

    to_check = [collide_left_p1, collide_right_p1, *vertical_collide_p1,
                collide_left_p2, collide_right_p2, *vertical_collide_p2, 
                collide_left_enemy, collide_right_enemy, *vertical_collide_enemy]

    for obj in to_check:
        if obj and obj.name == "fire":
            if obj in [collide_left_p1, collide_right_p1, *vertical_collide_p1]:
                player1.make_hit()
            if obj in [collide_left_p2, collide_right_p2, *vertical_collide_p2]:
                player2.make_hit()
            if obj in vertical_collide_enemy:
                enemy.x_vel = 0
        if obj and obj.name == "spike":
            if obj in [collide_left_p1, collide_right_p1, *vertical_collide_p1]:
                hit_sound.play()
                player1.make_hit()
                
            if obj in [collide_left_p2, collide_right_p2, *vertical_collide_p2]:
                hit_sound.play()
                player2.make_hit()
                
            if obj in vertical_collide_enemy:
                enemy.x_vel = 0