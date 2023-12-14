from display import *
import pygame.mixer

pygame.mixer.init()

sound_volume = 50
get_sound = pygame.mixer.Sound('Coin.mp3')
get_sound.set_volume(sound_volume / 100.0)

def get_block(size, block_id):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(16 * block_id[0], 16 * block_id[1], size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


level_map_1 = [
        "1111111111111111111111111111111111111111",
        "1955555555555555555555555555555555555581",
        "12                 eccRRRRRRd         41",
        "12                 ssseccRRRd         41",
        "12                    ssseccf         41",
        "12                       ssss         41",
        "12             %ww^                   41",
        "12             aRRd                   41",
        "12             aRRRwwwww^             41",
        "12         %wwwRRRRRRRRRRww^          41",
        "12         aRRRRRRRRRRRRRRRRww^       41",
        "12LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL41",
        "12                                    41",
        "12                                    41",
        "12                                    41",
        "12                                    41",
        "12                                    41",
        "12           #GG$         #G$         41",
        "12        #GG!DDr    ZX   lDrg        41",
        "12       BlDDDDDrSSSSCVSSSlDrhB       41",
        "12GGGGGGGG!DDDDD@GGGGGGGGG!D@GGGGGGGGG41",
        "12DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD41",
        "1633333333333333333333333333333333333371",
        "1111111111111111111111111111111111111111"
    ]

level_map_2 = [
        "1111111111111111111111111111111111111111",
        "1955555555555555555555555555555555811111",
        "12ssssssssssssssssssssssssssssssss411111",
        "12                                411111",
        "12                                411111",
        "12                                411111",
        "12    ZXwwww^    #GGGGGGGGGGG$    411111",
        "12    CVccccf    lDDDDDDDDDDDr    411111",
        "12km  adsssss   BlDnnnnnnnnnno    411111",
        "12    ad       ZXlrsssssssssss    411111",
        "12    ad       CVlr               411111",
        "12  jkadkm  #GGGG!r               411111",
        "12    ad    lDnnnno   jkkkmBjkkkkki55581",
        "12    ad    lrsssss                   41",
        "12km  ad  jklr                        41",
        "12    ad    lr                        41",
        "12    ad    lrkkmBjkkmjmjkkkmBjkkkm   41",
        "12  jkefkm  lrsssssssssssssssssssss   41",
        "12          lr                        41",
        "12          lr                        41",
        "12B        Blr                     jkm41",
        "12GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG41",
        "1633333333333333333333333333333333333371",
        "1111111111111111111111111111111111111111"
    ]

level_map_3=[
        '1111111111111111111111111111111111111111',
        '1QOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOT1',
        '1MssssssssssssssssssssssssssssssssssssK1',
        '1M                                    K1',
        '1M                                    K1',
        '1M                                   pK1',
        '1M                                    K1',
        '1Mqqqqqqqqt                vx         K1',
        '1M                         yz       pqK1',
        '1M               pq#GGGGGGGG$         K1',
        '1M                 lDDDDDDDDru        K1',
        '1M      #GGGG$     lDnnnnnnnoqqqt     K1',
        '1M      lDDDDr     lrssssssssssss     K1',
        '1M    pqlDDDDrqt   lr                 K1',
        '1M      lDDDDrss   lr                 K1',
        '1M      lDDDDr     lr   upqqtpqtupqqqqK1',
        '1Mqt    Ynnnno    ulr              uvxK1',
        '1M            +++++lr               yzK1',
        '1M                 lr                 K1',
        '1MGGGG$           Alr                 K1',
        '1MvxDDr          uFlr pt   u   u      K1',
        '1MyzuDrGGG$     #GG!rSSSSSSSSSSSS     K1',
        '1UIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIW1',
        '1111111111111111111111111111111111111111'
    ]


def create_level(level_map_1):
    objects = []
    block_size = 16


    for y, row in enumerate(level_map_1):
        for x, char in enumerate(row):
            if char == '1':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 9))
                objects.append(block)
            elif char == '2':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (2, 9))
                objects.append(block)
            elif char == '3':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 8))
                objects.append(block)
            elif char == '4':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (0, 9))
                objects.append(block)
            elif char == '5':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 10))
                objects.append(block)
            elif char == '6':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (3, 9))
                objects.append(block)
            elif char == '7':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (4, 9))
                objects.append(block)
            elif char == '8':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (4, 8))
                objects.append(block)
            elif char == '9':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (3, 8))
                objects.append(block)
            elif char == 'i':  
                spike = Spike(x * block_size*2, y * block_size*2, block_size*2, (0, 10))
                objects.append(spike)
            elif char == 'D':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (7, 1))
                objects.append(block)
            elif char == 'G':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (7, 0))
                objects.append(block)
            elif char == 'B':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (12, 9))
                objects.append(block)
            elif char == 'R':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 5))
                objects.append(block)
            elif char == 'L':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (13, 8))
                objects.append(block)
            elif char == 'Z':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (13, 9))
                objects.append(block)
            elif char == 'X':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (14, 9))
                objects.append(block)
            elif char == 'C':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (13, 10))
                objects.append(block)
            elif char == 'V':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (14, 10))
                objects.append(block)
            elif char == '!':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (10, 1))
                objects.append(block)
            elif char == '@':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (9, 1))
                objects.append(block)
            elif char == '#':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (6, 0))
                objects.append(block)
            elif char == '$':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (8, 0))
                objects.append(block)
            elif char == 'l':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (6, 1))
                objects.append(block)
            elif char == 'r':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (8, 1))
                objects.append(block)
            elif char == '%':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (17, 4))
                objects.append(block)
            elif char == '^':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 4))
                objects.append(block)
            elif char == 'a':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (17, 5))
                objects.append(block)
            elif char == 'w':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 4))
                objects.append(block)
            elif char == 'd':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 5))
                objects.append(block)
            elif char == 'e':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (17, 6))
                objects.append(block)
            elif char == 'c':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 6))
                objects.append(block)
            elif char == 'f':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 6))
                objects.append(block)
            elif char == 'g':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (15, 8))
                objects.append(block)
            elif char == 'h':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (15, 10))
                objects.append(block)
            elif char == 'j':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (12, 8))
                objects.append(block)
            elif char == 'k':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (13, 8))
                objects.append(block)
            elif char == 'm':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (14, 8))
                objects.append(block)
            elif char == 'n':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (7, 2))
                objects.append(block)
            elif char == 'o':  
                block = Block(x * block_size*2, y * block_size*2, block_size*2, (8, 2))
                objects.append(block)
            elif char == 'p':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (17, 8))
                objects.append(spike)
            elif char == 'q':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 8))
                objects.append(spike)
            elif char == 't':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 8))
                objects.append(spike)
            elif char == 'u':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (17, 9))
                objects.append(spike)
            elif char == 'v':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 9))
                objects.append(spike)
            elif char == 'x':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 9))
                objects.append(spike)
            elif char == 'y':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 10))
                objects.append(spike)
            elif char == 'z':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (19, 10))
                objects.append(spike)
            elif char == 'A':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (20, 8))
                objects.append(spike)
            elif char == 'E':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (20, 9))
                objects.append(spike)
            elif char == 'F':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (20, 10))
                objects.append(spike)
            elif char == 'H':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (0, 0))
                objects.append(spike)
            elif char == 'I':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 0))
                objects.append(spike)
            elif char == 'J':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (2, 0))
                objects.append(spike)
            elif char == 'K':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (0, 1))
                objects.append(spike)
            elif char == 'L':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 1))
                objects.append(spike)
            elif char == 'M':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (2, 1))
                objects.append(spike)
            elif char == 'N':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (0, 2))
                objects.append(spike)
            elif char == 'O':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (1, 2))
                objects.append(spike)
            elif char == 'P':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (2, 2))
                objects.append(spike)
            elif char == 'Q':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (3, 0))
                objects.append(spike)
            elif char == 'T':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (4, 0))
                objects.append(spike)
            elif char == 'U':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (3, 1))
                objects.append(spike)
            elif char == 'W':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (4, 1))
                objects.append(spike)
            elif char == 'Y':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (6, 2))
                objects.append(spike)
            elif char == '+':  
                spike = Block(x * block_size*2, y * block_size*2, block_size*2, (18, 0))
                objects.append(spike)
            elif char == 'S':  
                spike = Spike(x * block_size*2, y * block_size*2, block_size*2, (17, 3))
                objects.append(spike)
            elif char == 's':  
                spike = Spike(x * block_size*2, y * block_size*2, block_size*2, (18, 3))
                objects.append(spike)

    return objects

        

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size, block_id):
        super().__init__(x, y, size, size)
        block = get_block(size, block_id)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

        

class Fruit(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fruits")
        self.fruits = load_sprite_sheets("Items", "Fruits", width, height)
        self.image = self.fruits["Apple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Apple"
    
    def apple(self):
        self.animation_name = "Apple"

    def banana(self):
        self.animation_name = "Banana"

    def collected(self):
        self.animation_name = "Collected"

    
    def loop(self):
        sprites = self.fruits[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Spike(Object):
    def __init__(self, x, y, size, block_id):
        super().__init__(x, y, size, size, "spike")
        spike = get_block(size, block_id)
        self.image.blit(spike, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

def get_item(player, player2, apples, bananas, fruits): 
    for apple in apples:
        if pygame.sprite.collide_mask(player, apple):
            get_sound.play()
            apple.kill()
    for banana in bananas:
        if pygame.sprite.collide_mask(player2, banana):
            get_sound.play()
            banana.kill()
    return len(fruits.sprites())

