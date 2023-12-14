import pygame
from player import *
from display import *
from level import *
from enemy import *
from gamestate import GameState

block_size = 96


def main():
    clock = pygame.time.Clock()

    player1 = Player(100, 150, 50, 50)
    player2 = Player2(100, 400, 50, 50)

    enemy = Enemy(400, 100, 50, 50)

    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    game_state = GameState(player1, player2, enemy, fire)

    game_state.level_loader()

    run = True
    while run:
        clock.tick(FPS)

        player1.check_screen(block_size)
        player2.check_screen(block_size)
        enemy.check_screen(block_size)
        enemy_state(player1, player2, enemy)

        game_state.state_manager()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
