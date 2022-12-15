import pygame
import resources.serv as serv
import socket


class Menu():
    def __init__(self, game):
        self.tick_i = 0
        self.max_ti = 15
        self.tick_b = True
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.speedanim = 0.25

    def draw_cursor(self):
        self.game.draw_text('X', 15, self.cursor_rect.x - 60, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def anim(self):
        if self.tick_i < self.max_ti and self.tick_b:
            self.tick_i += self.speedanim
        elif self.tick_i + self.speedanim > 0:
            self.tick_b = False
            self.tick_i -= self.speedanim
            if self.tick_i <= 0:
                self.tick_b = True

    def play_music(self, num):
        self.game.curr_i = num
        self.curr_track = self.game.track_names[self.game.curr_i]

        pygame.mixer.music.load(f'{self.curr_track}.mp3')
        self.game.status_music = True
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.game.vol_music)

    def validate_ip(self, s):
        a = s.split('.')
        if len(a) != 4:
            return False
        for x in a:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        # положение старотовых клавиш
        self.state = "Input IP"
        self.ipx, self.ipy = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.storyx, self.storyy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)

        # проигрывание музыки
        if self.game.status_music:
            self.play_music(0)

        self.tick_i = 0
        self.max_ti = 15
        self.tick_b = True
        self.help_tick = 0

    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.anim()
            self.game.check_events()
            self.check_input()

            # вспомогательный тик
            if self.tick_i == 14:
                self.help_tick += 1

            if self.help_tick == 20:
                self.help_tick = 0

            # отрисовка
            self.game.display.blit(self.game.bg_3, (0, 0))  # background

            self.game.display.blit(self.game.sword, (self.mid_w - 40 + self.tick_i * 1.5, self.mid_h-130))
            self.game.display.blit(self.game.sword_vert, (self.mid_w  - self.tick_i * 1.5, self.mid_h - 130))

            if self.help_tick > 10:
                self.game.draw_text("ARROWS, ENTER, BCPS, ESC", 28, self.mid_w, self.mid_h * 2 - 30,
                                    (255 - self.tick_i * 2, 255 - self.tick_i * 2, 255 - self.tick_i * 2),
                                    self.game.font_3)

            if self.state == 'Input IP':
                self.game.draw_text("Start game", 20, self.ipx - self.tick_i * 0.9, self.ipy,
                                    (255, 255 - self.tick_i * 2, 255))
            else:
                self.game.draw_text("Start game", 20, self.ipx, self.ipy)

            if self.state == 'Options':
                self.game.draw_text("Options", 20, self.optionsx - self.tick_i * 0.9, self.optionsy,
                                    (255, 255 - self.tick_i * 2, 255))
            else:
                self.game.draw_text("Options", 20, self.optionsx, self.optionsy)

            if self.state == 'Credits':
                self.game.draw_text("About us", 20, self.creditsx - self.tick_i * 0.9, self.creditsy,
                                    (255, 255 - self.tick_i * 2, 255))
            else:
                self.game.draw_text("About us", 20, self.creditsx, self.creditsy)

            if self.state == 'Story':
                self.game.draw_text("Story", 20, self.storyx - self.tick_i * 0.9, self.storyy,
                                    (255, 255 - self.tick_i * 2, 255))
            else:
                self.game.draw_text("Story", 20, self.storyx, self.storyy)

            self.game.draw_text('Survival King', 60, self.mid_w, self.mid_h - 50,
                                (255 - self.tick_i * 5, 20, 212 - self.tick_i * 10), self.game.font_gotic)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)
                self.state = 'Story'
            elif self.state == 'Input IP':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Story':
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
                self.state = 'Input IP'

            self.game.menu_click_sound.play()
        elif self.game.UP_KEY:
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
                self.state = 'Input IP'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Input IP':
                self.cursor_rect.midtop = (self.storyx + self.offset, self.storyy)
                self.state = 'Story'
            elif self.state == 'Story':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            self.game.menu_click_sound.play()


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:

            if self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Input IP':
                self.game.curr_menu = self.game.select_start
            elif self.state == 'Story':
                self.game.curr_menu = self.game.story
            self.run_display = False



        if self.game.ESCP:
            self.game.running, self.game.playing = False, False
            self.game.curr_menu.run_display = False
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

        self.tick_i = 0
        self.max_ti = 40
        self.tick_b = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.anim()

            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.display.blit(self.game.bg_2, (0, 0))  # background
            self.game.draw_text('Options', 30, self.mid_w, self.mid_h - 60,
                                (255 - self.tick_i * 0.6, 255 - self.tick_i * 0.2, 255))
            if self.state == 'Volume':
                self.game.draw_text("Volume", 20, self.volx - self.tick_i * 0.3, self.voly)
                self.game.draw_text("Controls", 20, self.controlsx, self.controlsy)
            else:
                self.game.draw_text("Volume", 20, self.volx, self.voly)
                self.game.draw_text("Controls", 20, self.controlsx - self.tick_i * 0.3, self.controlsy)
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESCP:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
            self.game.menu_click_sound.play()
        elif self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.controls
            self.run_display = False



class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True

        self.tick_i = 0
        self.max_ti = 230
        self.tick_b = True
        flex_i = 0
        easter_egg = 0

        while self.run_display:

            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY or self.game.ESCP:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.anim()

            # пасхалка
            if self.game.UP_KEY:
                easter_egg += 1

            if self.tick_i == 230:
                easter_egg = 0
                if flex_i < 3:
                    flex_i += 1
                else:
                    flex_i = 0

            family = ['Alexey Soloshenko', 'Ivan Steblivets', 'Kodin Denis', 'Anastasya Kalimanova']
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.game.bg_1, (-self.tick_i, 0))
            self.game.draw_text('Game by', 20, self.mid_w, self.mid_h - 60)
            self.game.draw_text(family[flex_i], 30, self.mid_w, self.mid_h,
                                (255 - self.tick_i * 0.1, 255 - self.tick_i * 0.7, 255 - self.tick_i * 0.7))
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i * 0.3, 255 - self.tick_i * 0.5, 255 - self.tick_i * 0.7))

            # пасхалка
            if easter_egg > 5:
                self.game.draw_text('PROJECT 1', 50, self.mid_w, self.mid_h + 65, (0, 0, 0),
                                    self.game.font_2)
            if easter_egg > 10:
                self.game.draw_text('SURVIVAL KING', 50, self.mid_w, self.mid_h + 115, (0, 0, 0),
                                    self.game.font_2)

            self.blit_screen()

# include classes
class VolumeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True

        vol = int(self.game.vol_music * 100)
        flex = self.mid_w

        self.tick_i = 0
        self.max_ti = 200
        self.tick_b = True

        self.volumex, self.volumey = self.mid_w, self.mid_h

        while self.run_display:
            self.game.check_events()
            if self.game.status_music:
                self.anim()

            if self.game.BACK_KEY or self.game.ESCP:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.game.START_KEY and self.game.status_music:
                self.game.status_music = False
                pygame.mixer.music.pause()
                pygame.mixer.Sound.set_volume(self.game.menu_click_sound, 0)
            elif self.game.START_KEY:
                self.game.status_music = True
                pygame.mixer.music.play()
                pygame.mixer.Sound.set_volume(self.game.menu_click_sound, self.game.standart_sound_vol)

            # track change
            if self.game.RIGHT_KEY:
                if self.game.curr_i == len(self.game.track_names) - 1:
                    self.game.curr_i = 0
                else:
                    self.game.curr_i += 1

                self.play_music(self.game.curr_i)

            if self.game.LEFT_KEY:
                if self.game.curr_i == 0:
                    self.game.curr_i = len(self.game.track_names) - 1
                else:
                    self.game.curr_i -= 1

                self.play_music(self.game.curr_i)

            # volume change =============================
            if self.game.UP_KEY:
                if vol < 100:
                    vol += 10
            elif self.game.DOWN_KEY:
                if vol > 0:
                    vol -= 10

            # для бегунка =============================
            if flex > self.game.DISPLAY_W + 40:
                flex = -40
            else:
                flex += 1

            begun = 'I' * (vol // 10) if self.game.status_music else ''

            # для прозрачности =============================
            if self.game.status_music:
                st_m = 'Playing'
            else:
                st_m = 'Stopped'

            self.game.vol_music = vol * 0.01
            pygame.mixer.music.set_volume(self.game.vol_music)

            self.game.display.blit(self.game.bg_6, (-self.tick_i * 0.8 - 900, - 400))  # background

            self.game.draw_text('Now playing: soundtrack %d' % (self.game.curr_i + 1), 50, self.mid_w,
                                30, (102 - self.tick_i * 0.5, 115, 30 + self.tick_i),
                                self.game.font_3)

            self.game.draw_text('Volume menu', 30, self.volumex, self.volumey - 40)
            self.game.draw_text('%d' % (vol), 25, self.volumex, self.volumey)

            self.game.draw_text('%s' % (st_m), 17, self.mid_w - 70,
                                self.mid_h + 90)
            self.game.draw_text('%s' % ('(press ENTER)'), 11, self.mid_w + 60,
                                self.mid_h + 92 - self.tick_i * 0.04,
                                (102 - self.tick_i * 0.5, 115, 30 + self.tick_i))

            self.game.draw_text(begun, 30, flex, self.mid_h - 100 - self.tick_i * 0.2)
            self.game.draw_text('ESC to return', 15, self.mid_w - self.tick_i * 0.3,
                                self.mid_h * 2 - 30,
                                (102 - self.tick_i * 0.5, 115, 30 + self.tick_i))

            self.blit_screen()


class ControlsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

        self.tick_i = 0
        self.max_ti = 130
        self.tick_b = True

    def display_menu(self):
        self.run_display = True

        cl_up = self.game.WHITE
        cl_down = self.game.WHITE
        cl_left = self.game.WHITE
        cl_right = self.game.WHITE
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY or self.game.ESCP:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.anim()

            if self.game.LEFT_KEY:
                cl_left = (0, 200, 0)
                self.game.menu_click_sound.play()
            elif self.tick_i == 50:
                cl_left = self.game.WHITE
            if self.game.RIGHT_KEY:
                cl_right = (0, 200, 0)
                self.game.menu_click_sound.play()
            elif self.tick_i == 50:
                cl_right = self.game.WHITE
            if self.game.UP_KEY:
                cl_up = (0, 200, 0)
                self.game.menu_click_sound.play()
            elif self.tick_i == 50:
                cl_up = self.game.WHITE
            if self.game.DOWN_KEY:
                cl_down = (0, 200, 0)
                self.game.menu_click_sound.play()
            elif self.tick_i == 50:
                cl_down = self.game.WHITE

            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.game.bg_2, (-self.tick_i, 0))  # background
            self.game.draw_text('Controls menu', 20, self.mid_w, self.mid_h - 30)
            self.game.draw_text('WASD or ARROWS', 15, self.mid_w, self.mid_h)
            self.game.draw_text('^', 55, self.mid_w - 90, self.mid_h + 70, cl_up,
                                self.game.font_2)
            self.game.draw_text('|', 55, self.mid_w - 90, self.mid_h + 70, cl_up,
                                self.game.font_2)
            self.game.draw_text('<-', 55, self.mid_w - 20, self.mid_h + 70, cl_left,
                                self.game.font_2)
            self.game.draw_text('->', 55, self.mid_w + 20, self.mid_h + 70, cl_right,
                                self.game.font_2)
            self.game.draw_text('|', 55, self.mid_w + 90, self.mid_h + 70, cl_down,
                                self.game.font_2)
            self.game.draw_text('v', 55, self.mid_w + 95, self.mid_h + 80, cl_down,
                                self.game.font_2)
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))

            self.blit_screen()


class Select_start(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Host'
        self.volx, self.voly = self.mid_w - 120, self.mid_h - 20
        self.controlsx, self.controlsy = self.mid_w - 40, self.mid_h + 40
        self.infox, self.infoy = self.mid_w + 90, self.mid_h + 100
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

        self.tick_i = 0
        self.max_ti = 40
        self.tick_b = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.anim()

            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.display.blit(self.game.bg_7, (0, 0))  # background
            if self.state == 'Host':
                self.game.draw_text("Host", 30, self.volx + self.tick_i * 0.3, self.voly)

            else:
                self.game.draw_text("Host", 30, self.volx, self.voly)

            if self.state == 'Connect':
                self.game.draw_text("Connect", 30, self.controlsx + self.tick_i * 0.3, self.controlsy)
            else:
                self.game.draw_text("Connect", 30, self.controlsx, self.controlsy)


            if self.state == 'Info':
                self.game.draw_text("READ ME", 25, self.infox + self.tick_i * 0.3, self.infoy)
            else:
                self.game.draw_text("READ ME", 25, self.infox, self.infoy)

            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY or self.game.ESCP:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Host':
                self.state = 'Connect'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Connect':
                self.state = 'Info'
                self.cursor_rect.midtop = (self.infox + self.offset, self.infoy)
            elif self.state == 'Info':
                self.state = 'Host'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

            self.game.menu_click_sound.play()
        elif self.game.UP_KEY:
            if self.state == 'Info':
                self.state = 'Connect'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Host':
                self.state = 'Info'
                self.cursor_rect.midtop = (self.infox + self.offset, self.infoy)
            elif self.state == 'Connect':
                self.state = 'Host'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
            self.game.menu_click_sound.play()

        elif self.game.START_KEY:
            if self.state == 'Host':
                self.game.curr_menu = self.game.input_ip

            elif self.state == 'Connect':
                self.game.curr_menu = self.game.connect_ip


            elif self.state == 'Info':
                self.game.curr_menu = self.game.info
            self.run_display = False


class Info(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)



    def display_menu(self):
        self.run_display = True
        self.tick_i = 0
        self.max_ti = 130
        self.tick_b = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY or self.game.ESCP:
                self.game.curr_menu = self.game.select_start
                self.run_display = False

            self.anim()

            self.game.display.blit(self.game.bg_7, (-self.tick_i*0.7 , -self.tick_i*1.2))  # background

            self.game.draw_text('Who are YOU?...', 60, self.mid_w, 40, (255 - self.tick_i,255,255), self.game.font_2)

            self.game.draw_text('Creator', 40, self.mid_w/2, self.mid_h - 100, (255- self.tick_i,255,255), self.game.font_2)
            self.game.draw_text('open form "Host"', 40, self.mid_w / 2 - self.tick_i*0.2 + 6, self.mid_h - 30, (255, 255, 255), self.game.font_2)
            self.game.draw_text('open new game', 40, self.mid_w / 2 - self.tick_i*0.2 + 6, self.mid_h + 10, (255, 255, 255), self.game.font_2)
            self.game.draw_text('choose "connect"', 40, self.mid_w / 2 - self.tick_i*0.2 + 6, self.mid_h + 50, (255, 255, 255), self.game.font_2)
            self.game.draw_text('set data', 40, self.mid_w / 2 - self.tick_i*0.2 + 6, self.mid_h + 90, (255, 255, 255), self.game.font_2)
            self.game.draw_text('PLAY', 40, self.mid_w / 2 - self.tick_i*0.2 + 6, self.mid_h + 130, (255, 255, 255), self.game.font_2)



            self.game.draw_text('Player', 40, self.mid_w*6/4, self.mid_h- 100, (255- self.tick_i,255,255), self.game.font_2)
            self.game.draw_text('choose "connect"', 40, self.mid_w*6/4 - self.tick_i*0.2 + 6, self.mid_h - 30, (255, 255, 255), self.game.font_2)
            self.game.draw_text('set data from', 40, self.mid_w*6/4 - self.tick_i*0.2 + 6, self.mid_h + 10, (255, 255, 255), self.game.font_2)
            self.game.draw_text('creator', 40, self.mid_w*6/4 - self.tick_i*0.2 + 6, self.mid_h + 50, (255, 255, 255), self.game.font_2)
            self.game.draw_text('set it', 40, self.mid_w*6/4 - self.tick_i*0.2 + 6, self.mid_h + 90, (255, 255, 255), self.game.font_2)
            self.game.draw_text('PLAY', 40, self.mid_w*6/4 - self.tick_i*0.2 + 6, self.mid_h + 130, (255, 255, 255), self.game.font_2)
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))



            self.blit_screen()


class Input_IPMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'IP'
        self.ipx, self.ipy = self.mid_w, self.mid_h - 90
        self.hostx, self.hosty = self.mid_w, self.mid_h + 30
        self.time_setx, self.time_sety = self.mid_w, self.mid_h + 150
        self.offsety = 60
        self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
        self.text = '127.0.0.1'
        self.text_host = 2
        self.text_time = 15
        self.sl = {str(i) for i in range(10)} | {':', '.'}
        self.speedanim = 0.2

    def display_menu(self):
        self.run_display = True

        self.tick_i = 0
        self.tick_b = True
        self.max_ti = 120

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.anim()

            self.clr_anim = (255 - self.tick_i, 255 - self.tick_i * 1.3, 255 - self.tick_i * 1.5)
            self.game.display.blit(self.game.bg_7, (-self.tick_i * 1.3 - 800, -150 - self.tick_i * 0.4))  # background

            # pick count menu
            if self.text_host == 1:
                self.vid_text_host_left = 8
                self.vid_text_host_right = 2
            elif self.text_host == 8:
                self.vid_text_host_left = 7
                self.vid_text_host_right = 1
            else:
                self.vid_text_host_left = self.text_host - 1
                self.vid_text_host_right = self.text_host + 1

            # IP
            if self.state == 'IP':
                self.game.draw_text('Input IP (enter to HOST)', 40, self.ipx + self.tick_i * 0.3 - 20, self.ipy - 60,
                                    self.clr_anim,
                                    self.game.font_2)
            else:
                self.game.draw_text('Input IP (enter to HOST)', 40, self.ipx, self.ipy - 60,
                                    self.game.WHITE,
                                    self.game.font_2)
            self.game.draw_text(self.text, 50, self.ipx, self.ipy, (255, 255, 255), self.game.font_2)

            # COUNT

            if self.state == 'HOST':
                self.game.draw_text('Count players (enter to HOST)', 40, self.hostx - 20 + self.tick_i * 0.3,
                                    self.hosty - 60,
                                    self.clr_anim,
                                    self.game.font_2)
            else:
                self.game.draw_text('Count players (enter to HOST)', 40, self.hostx, self.hosty - 60, self.game.WHITE,
                                    self.game.font_2)

            self.game.draw_text(str(self.vid_text_host_left), 25, self.hostx - 25, self.hosty, (200, 200, 200),
                                self.game.font_2)
            self.game.draw_text(str(self.vid_text_host_right), 25, self.hostx + 25, self.hosty, (200, 200, 200),
                                self.game.font_2)
            self.game.draw_text(str(self.text_host), 45, self.hostx, self.hosty, (255, 255, 255), self.game.font_2)

            if self.state == 'TIME_SET':
                self.game.draw_text('SET TIME (enter to HOST)', 37, self.hostx - 20 + self.tick_i * 0.3,
                                    self.hosty + 60,
                                    self.clr_anim, self.game.font_2)
            else:
                self.game.draw_text('SET TIME (enter to HOST)', 37, self.hostx, self.hosty + 60,
                                    self.game.WHITE, self.game.font_2)

            self.game.draw_text(str(self.text_time), 45, self.time_setx, self.time_sety, (255, 255, 255),
                                self.game.font_2)
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))

            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.ESCP:
            self.game.curr_menu = self.game.select_start
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'IP':
                self.state = 'HOST'
                self.cursor_rect.midtop = (self.hostx + self.offset, self.hosty)
            elif self.state == 'HOST':
                self.state = 'TIME_SET'
                self.cursor_rect.midtop = (self.time_setx + self.offset, self.time_sety)
            elif self.state == 'TIME_SET':
                self.state = 'IP'
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
            self.game.menu_click_sound.play()
        elif self.game.UP_KEY:
            if self.state == 'IP':
                self.state = 'TIME_SET'
                self.cursor_rect.midtop = (self.time_setx + self.offset, self.time_sety)
            elif self.state == 'TIME_SET':
                self.state = 'HOST'
                self.cursor_rect.midtop = (self.hostx + self.offset, self.hosty)
            elif self.state == 'HOST':
                self.state = 'IP'
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
            self.game.menu_click_sound.play()



        elif self.game.START_KEY:
            if ':' in self.text:
                self.game.your_port = self.text[self.text.find(':') + 1:]
                self.game.your_ip = self.text[:self.text.find(':')]
            else:
                self.game.your_ip = self.text
            if self.validate_ip(self.game.your_ip):
                self.game.menu_click_sound.play()

                pygame.mixer_music.pause()
                self.run_display = False

                self.game.count_players = self.text_host
                self.game.time_set = self.text_time

                self.game.curr_menu = self.game.hosting

                self.run_display = False


        if self.game.NOW_KEY_PRESSED:
            if self.state == 'IP':
                if self.text == '127.0.0.1':
                    self.text = ''
                if self.game.NOW_KEY in self.sl:
                    self.text += self.game.NOW_KEY

        if self.state == 'HOST':
            if self.game.RIGHT_KEY:
                if self.text_host < 8:
                    self.text_host += 1
                else:
                    self.text_host = 1
                self.game.menu_click_sound.play()
            elif self.game.LEFT_KEY:
                if self.text_host > 1:
                    self.text_host -= 1
                else:
                    self.text_host = 8
                self.game.menu_click_sound.play()

        if self.state == 'TIME_SET':
            if self.game.RIGHT_KEY:
                if self.text_time < 60:
                    self.text_time += 15
                else:
                    self.text_time = 15
                self.game.menu_click_sound.play()
            elif self.game.LEFT_KEY:
                if self.text_time > 15:
                    self.text_time -= 15
                else:
                    self.text_time = 60
                self.game.menu_click_sound.play()

        if self.game.BACK_KEY:
            if self.state == 'IP':
                self.text = self.text[:-1]


class Connect_IPMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'IP'
        self.ipx, self.ipy = self.mid_w, self.mid_h - 30
        self.portx, self.porty = self.mid_w, self.mid_h + 90
        self.offsety = 60
        self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
        self.text = '127.0.0.1'
        self.text_port = '7777'
        self.sl = {str(i) for i in range(10)} | {'.'}
        self.speedanim = 0.2


    def display_menu(self):
        self.run_display = True

        self.tick_i = 0
        self.tick_b = True
        self.max_ti = 120
        k = 0

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.anim()

            self.clr_anim = (255 - self.tick_i, 255 - self.tick_i * 1.3, 255 - self.tick_i * 1.5)
            self.game.display.blit(self.game.bg_7, (-self.tick_i * 1.3 - 400, -300 - self.tick_i * 0.4))  # background

            # IP
            if self.state == 'IP':
                self.game.draw_text('Input IP (enter to PLAY)', 40, self.ipx + self.tick_i * 0.3 - 20, self.ipy - 60,
                                    self.clr_anim,
                                    self.game.font_2)
            else:
                self.game.draw_text('Input IP (enter to PLAY)', 40, self.ipx, self.ipy - 60,
                                    self.game.WHITE,
                                    self.game.font_2)
            self.game.draw_text(self.text, 50, self.ipx, self.ipy, (255, 255, 255), self.game.font_2)

            # PORT

            if self.state == 'PORT':
                self.game.draw_text('PORT (enter to PLAY)', 40, self.portx + self.tick_i * 0.3 - 20, self.porty - 60,
                                    self.clr_anim,
                                    self.game.font_2)
            else:
                self.game.draw_text('PORT (enter to PLAY)', 40, self.portx, self.porty - 60,
                                    self.game.WHITE,
                                    self.game.font_2)
            self.game.draw_text(self.text_port, 50, self.portx, self.porty, (255, 255, 255), self.game.font_2)
            self.game.draw_text('ESC to return', 10, self.mid_w, self.mid_h * 2 - 30,
                                (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))

            if self.game.lost_connection:
                self.game.draw_text('LOST CONNECTION', 25, self.mid_w - self.tick_i*0.3+ 30, self.mid_h * 2 - 100,
                                    (255, 255- self.tick_i , 255- self.tick_i ))


            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.ESCP:
            self.game.curr_menu = self.game.select_start
            self.run_display = False
            self.game.lost_connection = False
        elif self.game.DOWN_KEY:
            if self.state == 'IP':
                self.state = 'PORT'
                self.cursor_rect.midtop = (self.portx + self.offset, self.porty)
            else:
                self.state = 'IP'
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
            self.game.menu_click_sound.play()
        elif self.game.UP_KEY:
            if self.state == 'IP':
                self.state = 'PORT'
                self.cursor_rect.midtop = (self.portx + self.offset, self.porty)
            else:
                self.state = 'IP'
                self.cursor_rect.midtop = (self.ipx + self.offset, self.ipy)
            self.game.menu_click_sound.play()



        elif self.game.START_KEY:

            self.game.your_ip = self.text
            self.game.your_port = self.text_port

            print(self.game.your_ip, self.game.your_port)


            self.game.lost_connection = False

            if self.validate_ip(self.game.your_ip):
                self.run_display = False
                self.game.playing = True
                self.game.menu_click_sound.play()
        if self.game.NOW_KEY_PRESSED:
            if self.state == 'IP':
                if self.text == '127.0.0.1':
                    self.text = ''
                if self.game.NOW_KEY in self.sl:
                    self.text += self.game.NOW_KEY

            if self.state == 'PORT':
                if self.text_port == '7777':
                    self.text_port = ''
                if self.game.NOW_KEY in self.sl - {'.'}:
                    self.text_port += self.game.NOW_KEY

        if self.game.BACK_KEY:
            if self.state == 'IP':
                self.text = self.text[:-1]
            elif self.state == 'PORT':
                self.text_port = self.text_port[:-1]


class Story(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.slide = 0
        self.tick_i = 0
        self.max_ti = 150
        self.tick_b = True
        self.slidemax = 4

        self.state = "ENG"
        self.rusx, self.rusy = self.mid_w, self.mid_h + 20
        self.engx, self.engy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.engx + self.offset, self.engy)

        self.story_text_rus = [['Великое королевство Rablayim всегда', 'считалось самым процветающим местом...'],
                               ['Но несколько дней назад, знаменитый', 'своими подвигами, король Джосеф, умер...'],
                               'К сожалению, он не оставил за собой наследников...',
                               ['Начался дворцовый переворот,', 'который ещё не видел свет...']]
        self.story_text_eng = ['The Great Kingdom of Rablayim was the most prosperous place...',
                               'But a few days ago, famous for his exploits, King Joseph died...',
                               'Unfortunately, he left no heirs..',
                               'A palace coup has begun, which has not yet seen the light...']



        self.speedanim = 0.1

        self.save_curr_music = self.game.curr_i
    def display_menu(self):
        self.run_display = True

        if self.game.status_music:
            self.play_music(4)
            self.game.vol_music = 0.1

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.anim()

            if self.slide == 1:
                self.slide1()
            elif self.slide == 2:
                self.slide2()
            elif self.slide == 3:
                self.slide3()
            elif self.slide == 4:
                self.slide4()

            if self.slide == 0:
                self.slide0()
                self.draw_cursor()
            self.blit_screen()

    def slide0(self):
        self.game.display.blit(self.game.story_bg0, (-self.tick_i, 0))  # background

        self.game.draw_text('STORY', 60, self.mid_w, self.mid_h - 60,
                            (252, 242, 176 + self.tick_i * 0.2), self.game.font_gotic)

        if self.state == 'RUS':
            self.game.draw_text("RUS", 20, self.rusx - self.tick_i * 0.2, self.rusy)
        else:
            self.game.draw_text("RUS", 20, self.rusx, self.rusy)

        if self.state == 'ENG':
            self.game.draw_text("ENG", 20, self.engx - self.tick_i * 0.2, self.engy)
        else:
            self.game.draw_text("ENG", 20, self.engx, self.engy)

        self.game.draw_text('ESC to menu', 10, self.mid_w, self.mid_h * 2 - 30,
                            (255 - self.tick_i, 255 - self.tick_i, 255 - self.tick_i))

    def slide1(self):
        self.game.display.blit(self.game.story_bg1, (0, -self.tick_i * 0.6 - 280))  # background
        if self.state == 'RUS':
            self.game.draw_text(self.story_text_rus[self.slide - 1][0], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text(self.story_text_rus[self.slide - 1][1], 30, self.rusx - self.tick_i * 0.05,
                                self.rusy + 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Страница %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
        elif self.state == 'ENG':
            self.game.draw_text(self.story_text_eng[self.slide - 1], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Page %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)

    def slide2(self):
        self.game.display.blit(self.game.story_bg2, (-self.tick_i * 0.5 - 400, -700))  # background

        if self.state == 'RUS':

            self.game.draw_text(self.story_text_rus[self.slide - 1][0], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text(self.story_text_rus[self.slide - 1][1], 30, self.rusx - self.tick_i * 0.05,
                                self.rusy + 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Страница %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
        elif self.state == 'ENG':
            self.game.draw_text(self.story_text_eng[self.slide - 1], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Page %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)

    def slide3(self):
        self.game.display.blit(self.game.story_bg3, (-self.tick_i * 0.5, -140))  # background
        if self.state == 'RUS':
            self.game.draw_text(self.story_text_rus[self.slide - 1], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Страница %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
        elif self.state == 'ENG':
            self.game.draw_text(self.story_text_eng[self.slide - 1], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Page %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)

    def slide4(self):
        self.game.display.blit(self.game.story_bg4, (-self.tick_i * 0.5 - 60, 0))  # background
        if self.state == 'RUS':
            self.game.draw_text(self.story_text_rus[self.slide - 1][0], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text(self.story_text_rus[self.slide - 1][1], 30, self.rusx - self.tick_i * 0.05,
                                self.rusy + 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Страница %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
        elif self.state == 'ENG':
            self.game.draw_text(self.story_text_eng[self.slide - 1], 30, self.rusx - self.tick_i * 0.05, self.rusy,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)
            self.game.draw_text('Page %d' % (self.slide), 30, self.mid_w, 30,
                                (252, 242, 176 + self.tick_i * 0.2), self.game.font_2)

    def move_cursor(self):

        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'RUS':
                self.cursor_rect.midtop = (self.engx + self.offset, self.engy)
                self.state = 'ENG'
            else:
                self.cursor_rect.midtop = (self.rusx + self.offset, self.rusy)
                self.state = 'RUS'

    def check_input(self):
        if self.slide == 0:
            self.move_cursor()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
                if self.game.status_music:
                    self.play_music(self.save_curr_music)
                    self.game.vol_music = 0.1
                self.slide = 0

        if self.game.START_KEY and self.slide < self.slidemax:
            self.slide += 1
            if self.slide > 1:
                self.game.stories_eng[self.slide - 2].stop()
                self.game.stories_eng_fon[self.slide - 2].stop()
            self.game.stories_eng[self.slide - 1].play()
            self.game.stories_eng_fon[self.slide - 1].play()

        elif self.game.START_KEY or self.game.ESCP:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            self.game.stories_eng[self.slide - 1].stop()
            self.game.stories_eng_fon[self.slide - 1].stop()
            if self.game.status_music:
                self.play_music(self.save_curr_music)
                self.game.vol_music = 0.1
            self.slide = 0

        if self.game.BACK_KEY and self.slide > 0:
            self.game.stories_eng[self.slide - 1].stop()
            self.game.stories_eng_fon[self.slide - 1].stop()
            self.slide -= 1


class Hosting(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game = game

        self.level = [
            "----------------------------------",
            "-                                -",
            "-                                -",
            "-                       --       -",
            "-            --                  -",
            "-                                -",
            "--                               -",
            "-                                -",
            "-                   ----     --- -",
            "-                                -",
            "--                               -",
            "-                                -",
            "-                            --- -",
            "-                                -",
            "-      ---                       -",
            "-                                -",
            "-                                -",
            "-   -------         ----         -",
            "-                                -",
            "-                         -      -",
            "-                            --  -",
            "-                                -",
            "-                                -",
            "----------------------------------"]

        self.timeout = 1 / 120
        self.test_time = 0

    def display_menu(self):
        flag = True

        self.world = serv.World(self.level, self.game.count_players, self.game.time_set)
        self.run_display = True

        self.host = self.game.your_ip


        # anim
        self.tick_i = 0
        self.tick_b = True
        self.max_ti = 40
        self.server_running = True
        try:
            self.serv = serv.Server(self.host, int(self.game.your_port), self.world)
        except serv.ServExcept:
            self.game.curr_menu = self.game.select_start
            self.server_running = False
            flag = False

        if flag:
            self.port = self.serv.port

            while self.run_display:

                self.game.check_events()
                self.check_input()

                self.anim()

                # ========================================


                if self.server_running:

                    self.serv.server.settimeout(self.timeout)
                    self.start = pygame.time.get_ticks()


                    while pygame.time.get_ticks() - self.start <= 16:
                        try:
                            self.serv.handle()
                        except ConnectionError:
                            pass

                        except socket.timeout:
                            pass
                    else:
                        self.serv.kick_afk()
                        try:
                            self.data = self.serv.get_world_info()
                        except serv.ServExcept:
                            self.game.curr_menu = self.game.select_start
                            self.run_display = False
                            self.server_running = False
                            self.serv.server.close()
                            continue

                        self.serv.send(self.data)

                    if self.test_time < self.start:
                        self.test_time = self.start + 1000
                        self.serv.get_atr()

                # ========================================

                self.game.display.blit(self.game.bg_4, (-150 + self.tick_i * 0.5, -300))
                self.game.draw_text('Now is hosting', 40, self.mid_w + self.tick_i * 0.8,
                                    self.mid_h - 40,
                                    (255, 255, 255))
                self.game.draw_text('----> %s:%s <----' % (self.game.your_ip, self.port), 50,
                                    self.mid_w,
                                    self.mid_h + 30 + self.tick_i * 0.3,
                                    (255 - self.tick_i * 2, 255 - self.tick_i * 5, 150 - self.tick_i * 0.12),
                                    self.game.font_2)
                self.game.draw_text('Wait %d players' % (self.game.count_players), 35,
                                    self.mid_w + self.tick_i * 0.5 - 10,
                                    self.mid_h + 85, (255, 255, 255), self.game.font_2)
                self.game.draw_text('Hard %d seconds' % (self.game.time_set), 25, self.mid_w, self.mid_h + 130,
                                    self.game.WHITE, self.game.font_2)

                self.game.draw_text("tell your IP and PORT to friends", 10, self.mid_w,
                                    self.mid_h * 2 - 30,
                                    (122, 255, 100))
                self.game.draw_text("don't close this window", 8, self.mid_w,
                                    self.mid_h * 2 - 60,
                                    (122, 255, 100))

                self.blit_screen()

    def check_input(self):
        if self.game.ESCP:
            self.game.curr_menu = self.game.select_start
            self.run_display = False
            self.server_running = False
            self.serv.server.close()