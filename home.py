import pygame
import os
import pygame.mixer
from os.path import join
from display import *

def get_layers(name):
    image = pygame.image.load(join("assets", "Layers", name))
    return image

def draw_text(surface, text, font, color, rect, max_width):
    words = text.split(' ')
    space_width, _ = font.size(' ')

    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width, word_height = font.size(word)

        if current_width + word_width < max_width:
            current_line.append(word)
            current_width += word_width + space_width
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width + space_width

    lines.append(' '.join(current_line))

    y = rect.y
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(rect.centerx, y))
        surface.blit(text_surface, text_rect)
        y += word_height
        
pygame.init()
pygame.mixer.init()

home_image = get_layers('Castle in the fog.png')
stage_image = get_layers('Forest.png')
story_image = get_layers('Curse forest.png')
option_image = get_layers('Cave.png')
menu_image = get_layers('Night sea.png')

sound_volume = 50

click_sound = pygame.mixer.Sound('Hole Punch Sound.mp3')
click_sound.set_volume(sound_volume / 100.0)

BGM_sound = pygame.mixer.Sound('BGM.mp3')
BGM_sound.set_volume(sound_volume / 100.0)
BGM_channel = pygame.mixer.Channel(0)

BGM_channel.play(BGM_sound)
BGM_channel.play(BGM_sound, loops=-1)

screen_width, screen_height = 1280, 720

white = (255, 255, 255)
black = (0, 0, 0)

font_path = join(os.path.dirname(__file__), 'DungGeunMo.ttf')
font = pygame.font.Font(font_path, 36)

larger_font = pygame.font.Font(font_path, 64)

start_text = font.render("START", True, white)
story_text = font.render("STORY", True, white)
option_text = font.render("OPTION", True, white)
quit_text = font.render("QUIT", True, white)

start_rect = start_text.get_rect(center=(screen_width // 2, 300))
story_rect = story_text.get_rect(center=(screen_width // 2, 400))
option_rect = option_text.get_rect(center=(screen_width // 2, 500))
quit_rect = quit_text.get_rect(center=(screen_width // 2, 600))

stage1_text = font.render("STAGE 1", True, white)
stage2_text = font.render("STAGE 2", True, white)
stage3_text = font.render("STAGE 3", True, white)
gameover_text = larger_font.render("GAME CLEAR!", True, black)

stage1_rect = stage1_text.get_rect(center=(screen_width // 2, 250))
stage2_rect = stage2_text.get_rect(center=(screen_width // 2, 350))
stage3_rect = stage3_text.get_rect(center=(screen_width // 2, 450))
gameover_rect = gameover_text.get_rect(center=(screen_width // 2, 250))

sound_text = font.render("SOUND", True, white)
fps_text = font.render("FPS", True, white)
size_text = font.render("WINDOW SIZE", True, white)
soundup_text = font.render(">", True, white)
sounddown_text = font.render("<", True, white)
fpsup_text = font.render(">", True, white)
fpsdown_text = font.render("<", True, white)

sound_rect = sound_text.get_rect(center=(screen_width // 2, 200))
fps_rect = fps_text.get_rect(center=(screen_width // 2, 350))
size_rect = size_text.get_rect(center=(screen_width // 2, 500))
soundup_rect = soundup_text.get_rect(center=(screen_width // 2 + 50, 260))
sounddown_rect = sounddown_text.get_rect(center=(screen_width // 2 - 50, 260))
fpsup_rect = fpsup_text.get_rect(center=(screen_width // 2 + 50, 410))
fpsdown_rect = fpsdown_text.get_rect(center=(screen_width // 2 - 50, 410))

back_text = font.render("BACK", True, white)

back_rect = back_text.get_rect(center=(80, 50))

story_content = """어느날 장난꾸러기 신이 두 명의 플레이어를 발견한다. 때마침 심심했던 이 신은 이 두 플레이어에게 장난을 치려 하는데…신의 장난으로 두 플레이어의 점프키가 합쳐지고, 맵을 통과하여 신을 재미있게 해주면 이 저주를 풀어준다고 한다…이렇게 이 플레이어들의 모험이 시작되는데…"""

story_surface = font.render(story_content, True, white)
story_rect2 = story_surface.get_rect(center=(screen_width // 2, 130))

continue_text = font.render("CONTINUE", True, white)
restart_text = font.render("RESTART", True, white)
option_text = font.render("OPTION", True, white)
back_text = font.render("BACK", True, white)

continue_rect = continue_text.get_rect(center=(screen_width // 2, 200))
restart_rect = restart_text.get_rect(center=(screen_width // 2, 300))
option2_rect = option_text.get_rect(center=(screen_width // 2, 400))
back2_rect = back_text.get_rect(center=(screen_width // 2, 500))

def set_previous_screen():
    global previous_screen, previous_previous_screen
    previous_previous_screen = previous_screen
    previous_screen = None

sound_volume = 50
fps_value = 30
window_size = (screen_width, screen_height)

clock = pygame.time.Clock()
