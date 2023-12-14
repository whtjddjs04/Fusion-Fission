import pygame
from os import listdir
from os.path import isfile, join

WIDTH, HEIGHT = 1280, 720
FPS = 60

pygame.init()

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

pygame.display.set_caption("Platformer")

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window, background, bg_image, player, player2, enemy, objects, offset_x, fruits):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    for fruit in fruits:
        fruit.draw(window, offset_x)
            
    player.draw(window, offset_x)
    player2.draw(window, offset_x)

    pygame.display.update()


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image



def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if dir1 == "MainCharacters" and direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        elif dir1 =="Enemies" and direction:
            all_sprites[image.replace(".png", "") + "_right"] = flip(sprites)
            all_sprites[image.replace(".png", "") + "_left"] = sprites
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size, block_id):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96 * block_id[0], 64 * block_id[1], size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)