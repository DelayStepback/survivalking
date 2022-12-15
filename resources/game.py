import pygame
import pygame.mixer
from resources.menu import *


class Game():
    def __init__(self):

        # pygame initilization
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('SURVIVAL KING')
        pygame.display.set_icon(pygame.image.load("images\\icon.ico"))
        # pygame.mouse.set_visible(False)

        # fonts
        self.font_2 = 'fonts\\19151.ttf'
        self.font_3 = 'fonts\\17838.ttf'
        self.font_gotic = 'fonts\\gotic.ttf'

        # background
        self.bg_1 = pygame.image.load("images\\background\\bg_1.png")
        self.bg_2 = pygame.image.load('images\\background\\bg_2.jpg')
        self.bg_3 = pygame.image.load('images\\background\\bg_3.jpg')
        self.bg_4 = pygame.image.load('images\\background\\bg_4.png')
        self.bg_5 = pygame.image.load('images\\background\\bg_5.png')
        self.bg_6 = pygame.image.load('images\\background\\bg_6.jpg')
        self.bg_7 = pygame.image.load('images\\background\\bg_7.png')

        self.story_bg0 = pygame.image.load('images\\background\\story0.jpg')
        self.story_bg1 = pygame.image.load('images\\background\\story1.jpg')
        self.story_bg2 = pygame.image.load('images\\background\\story2.jpg')
        self.story_bg3 = pygame.image.load('images\\background\\story3.jpg')
        self.story_bg4 = pygame.image.load('images\\background\\story4.jpg')

        # pic
        self.sword = pygame.image.load('images\\other\\sword.png')
        self.sword_vert = pygame.image.load('images\\other\\sword vert.png')


        # sound
        self.story_voice_eng_1 = pygame.mixer.Sound('sounds\\story_eng\\1\\1.wav')
        self.story_voice_eng_1_fon = pygame.mixer.Sound('sounds\\story_eng\\1\\fon.mp3')
        self.story_voice_eng_2 = pygame.mixer.Sound('sounds\\story_eng\\2\\2.wav')
        self.story_voice_eng_2_fon = pygame.mixer.Sound('sounds\\story_eng\\2\\fon.mp3')
        self.story_voice_eng_3 = pygame.mixer.Sound('sounds\\story_eng\\3\\3.wav')
        self.story_voice_eng_3_fon = pygame.mixer.Sound('sounds\\story_eng\\3\\fon.mp3')
        self.story_voice_eng_4 = pygame.mixer.Sound('sounds\\story_eng\\4\\4.wav')
        self.story_voice_eng_4_fon = pygame.mixer.Sound('sounds\\story_eng\\4\\fon.mp3')

        self.stories_eng = [self.story_voice_eng_1, self.story_voice_eng_2, self.story_voice_eng_3, self.story_voice_eng_4]
        self.stories_eng_fon = [self.story_voice_eng_1_fon, self.story_voice_eng_2_fon, self.story_voice_eng_3_fon, self.story_voice_eng_4_fon]


        self.menu_click_sound = pygame.mixer.Sound('sounds\\hit_menu.wav')
        self.menu_click_sound_2 = pygame.mixer.Sound('sounds\\hit_menu_2.wav')
        self.standart_sound_vol = 0.35
        pygame.mixer.Sound.set_volume(self.menu_click_sound, self.standart_sound_vol)


        # music load (once-first)
        self.track_names = ['soundtracks\\soundtrack_1', 'soundtracks\\soundtrack_2', 'soundtracks\\soundtrack_3',
                            'soundtracks\\soundtrack_4', 'soundtracks\\soundtrack_5']

        self.curr_i = 3
        self.vol_music = 0.1
        self.status_music = True

        # menu active
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.START_KEY, self.BACK_KEY, self.ESCP = False, False, False, False, False, False, False

        # init window
        self.DISPLAY_W, self.DISPLAY_H = 780, 540  # 780, 540
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = '8bit.TTF'

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # All menus
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.input_ip = Input_IPMenu(self)
        self.story = Story(self)

        self.volume = VolumeMenu(self)
        self.controls = ControlsMenu(self)

        self.select_start = Select_start(self)
        self.info = Info(self)
        self.connect_ip = Connect_IPMenu(self)
        self.hosting = Hosting(self)
        self.hosting_already = False

        self.curr_menu = self.main_menu

        # FOR IP
        self.keys_nums = [pygame.K_0, pygame.K_1,
                          pygame.K_2, pygame.K_3,
                          pygame.K_4, pygame.K_5,
                          pygame.K_6, pygame.K_7,
                          pygame.K_8, pygame.K_9,
                          pygame.K_PERIOD, pygame.K_COLON]
        self.your_ip = '127.0.0.1'
        self.your_port = '7777'

        # inform for server
        self.time_set = 15
        self.count_players = 2


        # client
        self.lost_connection = False


        self.clock = pygame.time.Clock()



        self.mouse_pos = (0,0)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

                if event.key == pygame.K_ESCAPE:
                    self.ESCP = True

                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True

                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

                if event.key in self.keys_nums:
                    self.NOW_KEY_PRESSED = True
                    self.NOW_KEY = event.unicode
        self.mouse_pos = pygame.mouse.get_pos()

    def reset_keys(self):
        self.ESCP, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.NOW_KEY_PRESSED = False, False, False, False, False, False, False, False

    def draw_text(self, text, size, x, y, color=(255, 255, 255), ff='fonts/8bit.TTF'):
        font = pygame.font.Font(ff, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
