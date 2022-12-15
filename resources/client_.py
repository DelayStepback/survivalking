from random import randint
from resources.loading import *
from pygame.locals import *
import socket
import pygame, sys
import json

import time  # test

tym = time.localtime()
opt = time.strftime("%H:%M:%S", tym)
name_client = 'SURVIVAL KING'


class ClientExcept(Exception):
    def __init__(self):
        pass

def main(host, port):


    skin_players = dict()

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    out = {'code': 0}
    keys = [False, False, False, False]
    clock = pygame.time.Clock()
    timeout = 1 / 60
    keys_old = [True, True, True, True]

    def dict_to_binary(the_dict):
        str = json.dumps(the_dict)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary

    def binary_to_dict(the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)
        return d

    class Camera:
        def __init__(self, camera_func, width, height):
            self.camera_func = camera_func
            self.state = Rect(0, 0, width, height)  # iширина окна

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.camera_func(self.state, target.rect)

    def camera_func(camera, target_rect):
        l = -target_rect.x + WIDTH / 2
        t = -target_rect.y + HEIGHT / 2
        w, h = camera.width, camera.height
        l = min(0, l)
        l = max(-(camera.width - WIDTH), l)
        t = max(-(camera.height - HEIGHT), t)
        t = min(0, t)

        return pygame.Rect(l, t, w, h)

    def update_players(units, hero):
        """
        Обновляет список того, что нужно рисовать
        """
        if len(units) > len(hero) - 1:
            for p in units:
                i = 0
                while i < len(hero) and hero[i].id != p[2] // 100:
                    i += 1
                t = i == len(hero)
                if t:
                    if p[2] // 100 == 0:
                        c = crown(p[0], p[1], p[2] // 100)
                        all_sprites.add(c)
                        all_players.add(c)
                        hero.append(c)
                    else:
                        a = Player(10, 10, p[2] // 100)
                        all_sprites.add(a)
                        all_players.add(a)
                        hero.append(a)

                        skin_players[a.id] = all_skin[a.id-1] 
                        a.dur_skin = all_skin[a.id-1]
        # удаление лишних игрок
        del_list = []
        if len(units) < len(hero):
            for ply in hero:
                if finde(units, ply.id, 1):
                    del_list.append(ply.id)

        for j in del_list:
            delete(hero, j)
        


    def update_players_status(units, hero):
        '''
        Обновляет статусы игроков 
        '''
        for pl in units:
            god = pl[2] // 10 % 10 == 1
            if pl[2] % 10 >= 5 or god:
                for p in hero:
                    if p.id == pl[2] // 100 and god:
                        p.make_god()
                    elif p.id == pl[2] // 100:
                        p.make_king()
                    else:
                        p.make_player()
            else:
                for p in hero:
                    if p.id == pl[2] // 100 and p.id != 0:
                        p.make_player()

    def delete(hero, id_del):
        '''
        удаляет спрайт по ID
        '''
        for h in hero:
            if h.id == id_del:
                hero.remove(h)
                h.kill()

    def finde(hero, id, f):
        '''
        если не найдено такого id, то передает TRUE
        идет по units
        '''

        pr = True
        i = 0
        while i < len(hero) and pr:
            if f == 1:
                k = hero[i][2] // 100
            elif f == 2:
                k = hero[i][2] // 10 % 10
            else:
                k = hero[i][2] % 10

            pr = k != id
            i += 1

        return pr

    def finde_sprite(hero, id):
        """
        ищет нужный спрайт по id
        """
        for player in hero:
            if player.id == id:
                return player

    def take_mesage(me, win, crown, start):
        if start:
            if me.king or me.god:
                return 'you king!'
            else:
                if not crown:
                    return 'Find crown!'
                else:
                    return 'Find king!'
        else:
            return 'Wait players...'

    class Player(pygame.sprite.Sprite):
        """
        Player(pygame.sprite.Sprite) - объект игрока для отрисовки 
        """

        def __init__(self, x, y, id):
            pygame.sprite.Sprite.__init__(self)
            self.dur_skin = vill_skins
            self.image = pygame.transform.scale(vill_skins[2][2], (45, 100))
            self.rect = pygame.Rect(x, y, 45, 100)
            self.id = id
            self.animcount = 0
            self.king = False
            self.god = False
            self.mee = False  # Я это Я?

            # мувы 
            self.left_m = False
            self.right_m = False
            self.up_m = False
            self.down_m = False

        def update(self):
            self.dur_skin = skin_players[self.id]
            if self.king and not self.god:
                self.dur_skin = king_skins
            elif self.god: 
                self.dur_skin = god_skin
            else: 
                self.dur_skin = skin_players[self.id]
            

    
            if self.animcount + 1 > 30:
                self.animcount = 0

            if self.left_m:
                self.image = pygame.transform.scale(self.dur_skin[0][self.animcount // 5], (45, 100))
                self.animcount += 1
            elif self.right_m:
                self.image = pygame.transform.scale(self.dur_skin[1][self.animcount // 5], (45, 100))
                self.animcount += 1
            elif self.down_m:
                self.image = pygame.transform.scale(self.dur_skin[2][self.animcount // 5], (45, 100))
                self.animcount += 1
            elif self.up_m:
                self.image = pygame.transform.scale(self.dur_skin[3][self.animcount // 5], (45, 100))
                self.animcount += 1
            else:
                self.image = pygame.transform.scale(self.dur_skin[2][2], (45, 100))

        def status_move(self, stat):
            st = stat
            if st == 0 or st == 5:
                self.left_m = False
                self.right_m = False
                self.up_m = False
                self.down_m = False
                self.animcount = 0
            if st == 1 or st == 6:
                self.left_m = True
                self.right_m = False
                self.up_m = False
                self.down_m = False
            if st == 2 or st == 7:
                self.left_m = False
                self.right_m = True
                self.up_m = False
                self.down_m = False
            if st == 3 or st == 8:
                self.left_m = False
                self.right_m = False
                self.up_m = True
                self.down_m = False
            if st == 9 or st == 4:
                self.left_m = False
                self.right_m = False
                self.up_m = False
                self.down_m = True

        def make_king(self):
            self.king = True
            self.god = False

        def make_player(self):
            self.god = False
            self.king = False

        def make_god(self):
            self.king = True
            self.god = True

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)  # требуется в Pygame для всех спрайтов
            self.image = pygame.transform.scale(load_wall(), (50, 50))
            self.rect = pygame.Rect(x, y, 50, 50)  # координаты и размеры

    class crown(pygame.sprite.Sprite):
        def __init__(self, x, y, id):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(load_crown(), (50, 100))
            self.rect = pygame.Rect(x, y, 30, 30)
            self.id = id

        def update(self):
            pass

    all_walls = pygame.sprite.Group()  # группа стен
    all_sprites = pygame.sprite.Group()  # множество спрайтов

    level = [
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
    ch_wal = True
    x = y = 0
    for st in level:
        for sym in st:
            if sym == '-':
                w = Wall(x, y)
                all_walls.add(w)
                all_sprites.add(w)
                if ch_wal:
                    m_walls = w
                    ch_wal = False
            x += 50
        y += 50
        x = 0
    total_width = len(level[0]) * 50  # Высчитываем фактическую ширину уровня
    total_height = len(level) * 50  # высоту

    camera = Camera(camera_func, total_width, total_height)

    # {'status': 'upd', 'units': [[350, 200, 1], [50, 50, 100], [50, 50, 200]]}

    all_players = pygame.sprite.Group()  # множество игроков

    hero = []  # список игрокоы
    PAS = True
    WIN = False
    Game = True
    fir = True
    start = False  # началась игра?
    flag = True
    first_packet = dict_to_binary(out)
    timeout = 2
    i = 0

    while flag:
        client.sendto(first_packet.encode('utf-8'), (host, port))
        client.settimeout(timeout)
        try:
            d = client.recvfrom(1024)
            msg = binary_to_dict(d[0])
            if msg['status'] == 'new_c':

                my_id = msg['id']
                flag = False
                
            elif msg['status'] == 'full':
                print('Сервер полон')
                window = pygame.display.set_mode((780, 540))
                raise ClientExcept

        except socket.timeout:
            i += 1
            if i == 3:
                window = pygame.display.set_mode((780, 540))
                raise ClientExcept
        except ConnectionError:
            pass
    # загрузим скины
    animcount = 0  # для анимации
    WIDTH = 700
    HEIGHT = 700
    BLUE = (0, 0, 255)
    GREY = (220, 220, 220)

    window = pygame.display.set_mode((WIDTH, HEIGHT + 30))
    screen = pygame.Surface((WIDTH, HEIGHT))
    pygame.display.set_caption(name_client)
    pygame.display.set_icon(pygame.image.load("images\\icon.ico"))

    info_string = pygame.Surface((700, 30))

    pygame.font.init()
    inf_font = pygame.font.Font('fonts\\17838.ttf', 25)
    win_font = pygame.font.Font('fonts\\19151.ttf', 70)

    # загрузка фона
    background = load_bg()
    background_rect = background.get_rect()

    back_info = load_info()

    # загрузка скинов
    # walk = [walkLeft, walkRight, walkDown, walkUp,walkLeft_K, walkRight_K, walkDown_K, walkUP_K]
    skins = load_skins()
    king_skins = skins[4:]
    god_skin = load_god()

    vill_skins = skins[:4]
    alh_skin = load_alh()
    lady_skin = load_lady()
    knight_skin = load_knight()
    ghost_skin = load_ghost()
    priest_skin = load_priest()
    witch_skin = load_witch()
    jester_skin = load_jester()
    all_skin = [vill_skins, priest_skin, witch_skin, jester_skin,
                alh_skin, lady_skin, knight_skin, ghost_skin]

    b_ = True
    while b_:
        client.settimeout(timeout)
        try:
            d = client.recvfrom(2048)
            msg = binary_to_dict(d[0])
            print('msg:', msg)
            out['code'] = 2
            if msg['status'] == 'upd':

                update_players(msg['units'], hero)


                if PAS:
                    for her in hero:
                        if her.id == my_id:
                            her.mee = True
                            pas = her
                    PAS = False

                update_players_status(msg['units'], hero)
                print(hero)

                king_in = False
                tr = 0
                while tr < len(hero) and not king_in:
                    if hero[tr].id != 0:
                        king_in = hero[tr].king or hero[tr].god 
                    tr += 1

                if not finde(msg['units'], 0, 1) or king_in:  # значит нашлась корона впервые или есть король
                    start = True
                else:
                    start = False

                for t in msg['units']:
                    try:
                        igrok = finde_sprite(hero, t[2] // 100)
                        if igrok.id != 0:
                            igrok.status_move(t[2] % 10)  # передаем мувы
                            igrok.update()  # обовляем движения
                        igrok.rect.x = t[0]
                        igrok.rect.y = t[1]
                    except:
                        pass

                mesage_info = take_mesage(pas, WIN, finde(msg['units'], 0, 1), start)

            elif msg['status'] == 'end':
                if pas.king or pas.god:
                    mesage_info = "You win!"
                    start = False
                else:
                    mesage_info = 'Game over!'
                    start = False


        except socket.timeout:

            '''
            Тут нужно выйти в меню и написать, что связь с сервером потеряна
            '''

            print('Соединение с сервером разорвано')
            window = pygame.display.set_mode((780, 540))
            raise ClientExcept


        for event in pygame.event.get():
            if event.type == QUIT:
                out['code'] = 404
                client.sendto(dict_to_binary(out).encode('utf-8'), (host, port))
                b_ = False
                window = pygame.display.set_mode((780, 540))

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    out['code'] = 404
                    client.sendto(dict_to_binary(out).encode('utf-8'), (host, port))
                    b_ = False
                    window = pygame.display.set_mode((780, 540))

                if event.key == K_LEFT:  keys[0] = True
                if event.key == K_RIGHT: keys[1] = True
                if event.key == K_UP:    keys[2] = True
                if event.key == K_DOWN:  keys[3] = True
            if event.type == KEYUP:
                if event.key == K_LEFT:  keys[0] = False
                if event.key == K_RIGHT: keys[1] = False
                if event.key == K_UP:    keys[2] = False
                if event.key == K_DOWN:  keys[3] = False

        if keys != keys_old:
            out['keys'] = keys
            print(out)
            outb = dict_to_binary(out).encode('utf-8')
            client.sendto(outb, (host, port))

        keys_old = keys.copy()

        window.blit(screen, (0, 30))

        if not PAS:
            camera.update(pas)

        screen.blit(background, camera.apply(m_walls))

        for e in all_sprites:
            screen.blit(e.image, camera.apply(e))

        # info
        info_string.blit(back_info,(0,0))

        if not start:
            count_players = 'Players:' + str(len(hero))
        else:
            count_players = 'game start!'

        if not PAS:
            info_string.blit(inf_font.render(mesage_info, 2, (255, 255, 255)), (80, 0))
            info_string.blit(inf_font.render(count_players, 2, (255, 255, 255)), (520, 0))

            if mesage_info == 'You win!':
                colores = (255, randint(40, 75), randint(0, 20))
                window.blit(win_font.render('You win!', 2, colores), (190, 350))
            
            elif mesage_info == 'Game over!':
                coloress = (255, randint(40, 75), randint(0, 20))
                window.blit(win_font.render('Game over!', 2, coloress), (190, 350))
            

            if msg['tk'] != -1:
                info_string.blit(inf_font.render(str(msg['tk']), 2, (255, 0, 0)), (340, 0))





        window.blit(info_string, (0, 0))

        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
