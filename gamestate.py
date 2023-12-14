import pygame
import sys
from level import *
from enemy import *
from home import *

block_size = 96


class GameState:
    def __init__(self, player1, player2, enemy, fire):
        self.state = "home"
        self.player1 = player1
        self.player2 = player2
        self.enemy = enemy
        self.fire = fire
        self.objects = create_level(level_map_1)
        self.offset_x = 0

        self.apples = pygame.sprite.Group()
        self.bananas = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        self.apples.add(Fruit(495 + 50 * i, 145, 32, 32) for i in range(2))
        self.apples.add(Fruit(650 + 50 * i, 200, 32, 32) for i in range(2))
        self.apples.add(Fruit(1150 + 50 * i, 300, 32, 32) for i in range(1))
        self.bananas.add(Fruit(440 + 50 * i, 490, 32, 32) for i in range(2))
        self.bananas.add(Fruit(670 + 50 * i, 525, 32, 32) for i in range(1))
        self.bananas.add(Fruit(850 + 50 * i, 490, 32, 32) for i in range(1))
        self.bananas.add(Fruit(1150 + 50 * i, 580, 32, 32) for i in range(1))

        for apple in self.apples:
            self.fruits.add(apple)
        for banana in self.bananas:
            banana.banana()
            self.fruits.add(banana)

        self.home_screen = True
        self.stage_select = False
        self.story_screen = False
        self.option_screen = False
        self.tutorial1_screen = False
        self.gamestage1_screen = False
        self.gamestage2_screen = False
        self.gamestage3_screen = False
        self.menu_screen = False
        self.previous_screen = None
        self.previous_previous_screen = None
        self.sound_volume = 50
        self.fps_value = 30

    def home(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.home_screen:
                    if start_rect.collidepoint(mouse_x, mouse_y):
                        self.home_screen = False
                        self.stage_select = True
                        click_sound.play()
                        print("시작하기 버튼이 클릭되었습니다.")
                    elif story_rect.collidepoint(mouse_x, mouse_y):
                        self.home_screen = False
                        self.story_screen = True
                        click_sound.play()
                        print("스토리 버튼이 클릭되었습니다.")
                    elif option_rect.collidepoint(mouse_x, mouse_y):
                        self.home_screen = False
                        self.option_screen = True
                        click_sound.play()
                        print("OPTION 버튼이 클릭되었습니다.")
                    elif quit_rect.collidepoint(mouse_x, mouse_y):
                        click_sound.play()
                        pygame.quit()
                        sys.exit()
                    self.previous_screen = "home"

                elif self.stage_select:
                    if stage1_rect.collidepoint(mouse_x, mouse_y):
                        self.stage_select = False
                        self.gamestage1_screen = True
                        click_sound.play()
                        print("스테이지 1 선택")
                        self.state = "stage1"
                        self.level_loader()
                        self.previous_screen = "gamestage1"
                        self.previous_previous_screen = "gamestage1"

                    elif stage2_rect.collidepoint(mouse_x, mouse_y):
                        self.stage_select = False
                        self.gamestage2_screen = True
                        click_sound.play()
                        print("스테이지 2 선택")
                        self.state = "stage2"
                        self.level_loader()
                        self.previous_screen = "gamestage2"
                        self.previous_previous_screen = "gamestage2"
                    elif stage3_rect.collidepoint(mouse_x, mouse_y):
                        self.stage_select = False
                        self.gamestage3_screen = True
                        click_sound.play()
                        print("스테이지 3 선택")
                        self.state = "stage3"
                        self.level_loader()
                        self.previous_screen = "gamestage3"
                        self.previous_previous_screen = "gamestage3"
                    elif back_rect.collidepoint(mouse_x, mouse_y):
                        self.stage_select = False
                        self.home_screen = True
                        click_sound.play()
                        print("Back 버튼이 클릭되었습니다.")

                elif self.story_screen:
                    if back_rect.collidepoint(mouse_x, mouse_y):
                        self.story_screen = False
                        self.home_screen = True
                        click_sound.play()
                        print("Back 버튼이 클릭되었습니다.")

                elif self.option_screen:
                    if soundup_rect.collidepoint(mouse_x, mouse_y):
                        self.sound_volume = min(100, self.sound_volume + 5)
                        click_sound.set_volume(self.sound_volume / 100.0)
                        BGM_sound.set_volume(self.sound_volume / 100.0)
                    elif sounddown_rect.collidepoint(mouse_x, mouse_y):
                        self.sound_volume = max(0, self.sound_volume - 5)
                        click_sound.set_volume(self.sound_volume / 100.0)
                        BGM_sound.set_volume(self.sound_volume / 100.0)
                    elif fpsup_rect.collidepoint(mouse_x, mouse_y):
                        self.fps_value = min(60, self.fps_value + 5)
                    elif fpsdown_rect.collidepoint(mouse_x, mouse_y):
                        self.fps_value = max(1, self.fps_value - 5)
                    elif back_rect.collidepoint(mouse_x, mouse_y):
                        self.option_screen = False
                        click_sound.play()
                        if self.previous_screen == "home":
                            self.home_screen = True
                        if self.previous_screen == "menu":
                            self.menu_screen = True

                        print("Back 버튼이 클릭되었습니다.")

                elif self.menu_screen:
                    if continue_rect.collidepoint(mouse_x, mouse_y):
                        self.menu_screen = False
                        click_sound.play()
                        if self.previous_screen == "tutorial1":
                            self.tutorial1_screen = True
                        elif self.previous_previous_screen == "tutorial1":
                            self.tutorial1_screen = True

                        elif self.previous_screen == "gamestage1":
                            self.gamestage1_screen = True
                        elif self.previous_previous_screen == "gamestage1":
                            self.gamestage1_screen = True

                        elif self.previous_screen == "gamestage2":
                            self.gamestage2_screen = True
                        elif self.previous_previous_screen == "gamestage2":
                            self.gamestage2_screen = True

                        elif self.previous_screen == "gamestage3":
                            self.gamestage3_screen = True
                        elif self.previous_previous_screen == "gamestage3":
                            self.gamestage3_screen = True
                    elif restart_rect.collidepoint(mouse_x, mouse_y):
                        click_sound.play()
                        # 재시작 로직 추가
                        pass
                    elif option2_rect.collidepoint(mouse_x, mouse_y):
                        self.menu_screen = False
                        self.option_screen = True
                        click_sound.play()
                        self.previous_screen = "menu"

                    elif back2_rect.collidepoint(mouse_x, mouse_y):
                        self.menu_screen = False
                        self.stage_select = True
                        click_sound.play()
                        set_previous_screen()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.tutorial1_screen:
                        self.tutorial1_screen = False
                        self.menu_screen = True
                        print("메뉴 열기")
                        self.previous_screen = "tutorial1"
                    elif self.gamestage1_screen:
                        self.gamestage1_screen = False
                        self.menu_screen = True
                        print("메뉴 열기")
                        self.previous_screen = "gamestage1"
                    elif self.gamestage2_screen:
                        self.gamestage2_screen = False
                        self.menu_screen = True
                        print("메뉴 열기")
                        self.previous_screen = "gamestage2"
                    elif self.gamestage3_screen:
                        self.gamestage3_screen = False
                        self.menu_screen = True
                        print("메뉴 열기")
                        self.previous_screen = "gamestage3"
        if self.home_screen:
            background_image = home_image
            window.blit(background_image, (0, 0))
            window.blit(start_text, start_rect)
            window.blit(story_text, story_rect)
            window.blit(option_text, option_rect)
            window.blit(quit_text, quit_rect)

        if self.stage_select:
            window.blit(stage_image, (0, 0))
            window.blit(stage1_text, stage1_rect)
            window.blit(stage2_text, stage2_rect)
            window.blit(stage3_text, stage3_rect)
            window.blit(back_text, back_rect)

        if self.story_screen:
            window.blit(story_image, (0, 0))
            window.blit(back_text, back_rect)
            draw_text(window, story_content, font, white, story_rect2, 400)

        '''elif self.menu_screen:
            window.blit(menu_image, (0, 0))
            window.blit(continue_text, continue_rect)
            window.blit(restart_text, restart_rect)
            window.blit(option_text, option2_rect)
            window.blit(back_text, back2_rect)'''

        if self.option_screen:
            window.blit(option_image, (0, 0))
            window.blit(sound_text, sound_rect)
            window.blit(fps_text, fps_rect)
            window.blit(size_text, size_rect)
            window.blit(soundup_text, soundup_rect)
            window.blit(sounddown_text, sounddown_rect)
            window.blit(fpsup_text, fpsup_rect)
            window.blit(fpsdown_text, fpsdown_rect)

            # 설정 값 표시
            sound_value_text = font.render(f"{self.sound_volume}", True, white)
            fps_value_text = font.render(f"{self.fps_value}", True, white)
            size_value_text = font.render(f"{window_size[0]} x {window_size[1]}", True, white)

            offset_x = 11 if self.sound_volume >= 100 else 0
            offset2_x = 11 if self.sound_volume < 10 else 0
            offset3_x = 11 if self.fps_value < 10 else 0

            window.blit(sound_value_text, (screen_width // 2 - 15 - offset_x + offset2_x, 240))
            window.blit(fps_value_text, (screen_width // 2 - 15 + offset3_x, 390))
            window.blit(size_value_text, (screen_width // 2 - 90, 540))

            window.blit(back_text, back_rect)
            clock.tick(self.fps_value)

        pygame.display.flip()

    def stage1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click_sound.play()
                    self.state = 'home'
                    self.home_screen = True
                    self.gamestage1_screen = False
                if event.key == pygame.K_SPACE:
                    if self.player1.jump_count == 0:
                        self.player1.single_jump()
                        self.player2.single_jump()

        background, bg_image = get_background("Blue.png")
        self.player1.loop(FPS)
        self.player2.loop(FPS)
        self.enemy.loop(FPS)
        self.fire.loop()

        if (self.player1.hit and self.player1.hit_count == 1) or (self.player2.hit and self.player2.hit_count == 1):
            self.state = "stage1"
            self.level_loader()

        for fruit in self.fruits:
            fruit.loop()
        handle_move(self.player1, self.player2, self.enemy, self.objects)
        draw(window, background, bg_image, self.player1, self.player2, self.enemy, self.objects, self.offset_x,
             self.fruits)

        if get_item(self.player1, self.player2, self.apples, self.bananas, self.fruits) == 0:
            if not self.apples and not self.bananas:
                self.state = "stage2"
                self.level_loader()

                for apple in self.apples:
                    self.fruits.add(apple)
                for banana in self.bananas:
                    banana.banana()
                    self.fruits.add(banana)

    def stage2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click_sound.play()
                    self.state = 'home'
                    self.home_screen = True
                    self.gamestage2_screen = False
                if event.key == pygame.K_SPACE:
                    if self.player1.jump_count == 0:
                        self.player1.single_jump()
                        self.player2.single_jump()

        background, bg_image = get_background("Green.png")
        self.player1.loop(FPS)
        self.player2.loop(FPS)
        self.enemy.loop(FPS)
        self.fire.loop()

        if (self.player1.hit and self.player1.hit_count == 1) or (self.player2.hit and self.player2.hit_count == 1):
            self.state = "stage2"
            self.level_loader()

        for fruit in self.fruits:
            fruit.loop()
        handle_move(self.player1, self.player2, self.enemy, self.objects)
        draw(window, background, bg_image, self.player1, self.player2, self.enemy, self.objects, self.offset_x,
             self.fruits)

        if get_item(self.player1, self.player2, self.apples, self.bananas, self.fruits) == 0:
            if not self.apples and not self.bananas:
                self.state = "stage3"
                self.level_loader()

                for apple in self.apples:
                    self.fruits.add(apple)
                for banana in self.bananas:
                    banana.banana()
                    self.fruits.add(banana)

    def stage3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    click_sound.play()
                    self.state = 'home'
                    self.home_screen = True
                    self.gamestage3_screen = False
                if event.key == pygame.K_SPACE:
                    if self.player1.jump_count == 0:
                        self.player1.single_jump()
                        self.player2.single_jump()

        background, bg_image = get_background("Green.png")
        self.player1.loop(FPS)
        self.player2.loop(FPS)
        self.enemy.loop(FPS)
        self.fire.loop()

        if (self.player1.hit and self.player1.hit_count == 1) or (self.player2.hit and self.player2.hit_count == 1):
            self.state = "stage3"
            self.level_loader()

        for fruit in self.fruits:
            fruit.loop()
        handle_move(self.player1, self.player2, self.enemy, self.objects)
        draw(window, background, bg_image, self.player1, self.player2, self.enemy, self.objects, self.offset_x,
             self.fruits)

        if get_item(self.player1, self.player2, self.apples, self.bananas, self.fruits) == 0:
            if not self.apples and not self.bananas:
                self.state = "stage1"
                self.level_loader()

                for apple in self.apples:
                    self.fruits.add(apple)
                for banana in self.bananas:
                    banana.banana()
                    self.fruits.add(banana)
    def game_clear(self):
        window.fill((255,255,255))
        window.blit(gameover_text, gameover_rect)
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    def level_loader(self):
        if self.state == 'stage1':

            self.player1.rect.x = 100
            self.player1.rect.y = 150
            self.player2.rect.x = 100
            self.player2.rect.y = 400

            self.objects = create_level(level_map_1)
            self.apples = pygame.sprite.Group()
            self.bananas = pygame.sprite.Group()
            self.fruits = pygame.sprite.Group()

            self.apples.add(Fruit(495 + 50 * i, 145, 32, 32) for i in range(2))
            self.apples.add(Fruit(650 + 50 * i, 200, 32, 32) for i in range(2))
            self.apples.add(Fruit(1150 + 50 * i, 300, 32, 32) for i in range(1))
            self.bananas.add(Fruit(440 + 50 * i, 490, 32, 32) for i in range(2))
            self.bananas.add(Fruit(670 + 50 * i, 525, 32, 32) for i in range(1))
            self.bananas.add(Fruit(850 + 50 * i, 490, 32, 32) for i in range(1))
            self.bananas.add(Fruit(1150 + 50 * i, 580, 32, 32) for i in range(1))

            for apple in self.apples:
                self.fruits.add(apple)
            for banana in self.bananas:
                banana.banana()
                self.fruits.add(banana)
        if self.state == 'stage2':

            self.player1.rect.x = 100
            self.player1.rect.y = 600
            self.player2.rect.x = 200
            self.player2.rect.y = 600

            self.objects = create_level(level_map_2)
            self.apples = pygame.sprite.Group()
            self.bananas = pygame.sprite.Group()
            self.fruits = pygame.sprite.Group()

            # 새로운 위치에 아이템 생성
            self.apples.add(Fruit(200 + 50 * i, HEIGHT - block_size - 480, 32, 32) for i in range(4))
            self.apples.add(Fruit(440 + 50 * i, 620, 32, 32) for i in range(1))
            self.bananas.add(Fruit(370 + 50 * i,300, 32, 32) for i in range(2))
            self.bananas.add(Fruit(490 + 50 * i,620, 32, 32) for i in range(1))

            for apple in self.apples:
                self.fruits.add(apple)
            for banana in self.bananas:
                banana.banana()
                self.fruits.add(banana)
        if self.state == 'stage3':
            self.player1.rect.x = 130
            self.player1.rect.y = 500
            self.player2.rect.x = 250
            self.player2.rect.y = 600

            self.objects = create_level(level_map_3)
            self.apples = pygame.sprite.Group()
            self.bananas = pygame.sprite.Group()
            self.fruits = pygame.sprite.Group()

            # 새로운 위치에 아이템 생성
            self.apples.add(Fruit(80 + 50 * i,170, 32, 32) for i in range(3))
            self.apples.add(Fruit(1160 + 50 * i,106, 32, 32) for i in range(1))
            self.apples.add(Fruit(1160 + 50 * i,650, 32, 32) for i in range(1))

            self.bananas.add(Fruit(450 + 50 * i, 480, 32, 32) for i in range(2))
            self.bananas.add(Fruit(900 + 50 * i, HEIGHT - block_size - 200, 32, 32) for i in range(3))
            self.bananas.add(Fruit(1110 + 50 * i, 650, 32, 32) for i in range(1))

            for apple in self.apples:
                self.fruits.add(apple)
            for banana in self.bananas:
                banana.banana()
                self.fruits.add(banana)

    def state_manager(self):
        if self.state == 'home':
            self.home()
        if self.state == 'stage1':
            self.stage1()
        if self.state == 'stage2':
            self.stage2()
        if self.state == 'stage3':
            self.stage3()
