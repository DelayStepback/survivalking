import socket
import json
from resources.units import *
import random
import errno


class ServExcept(Exception):
    def __init__(self):
        pass


class World:
    def __init__(self, lvl, count, time_set=5):
        pygame.init()
        self.level = lvl
        self.walls = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.crown = None
        self.time_god_mod = 0
        self.crown_mode = False
        self.king = None
        self.generate(self.level)
        self.count_of_player = count
        self.time_g_over = time_set * 1000
        self.game_mode = True
        self.close_time = 0

    def generate(self, lvl):
        x = y = 0
        for st in lvl:
            for sym in st:
                if sym == '-':
                    w = Wall(x, y)
                    self.walls.add(w)
                x += 50
            y += 50
            x = 0

    def make_pl(self, ind, pl_adr):
        x, y = self.new_coord()
        a = Player(x, y, ind, pl_adr)
        self.players.add(a)
        self.all_sprites.add(a)
        self.all_players.add(a)
        print('player', a.get_pos())

        return a

    def new_coord(self):
        i = random.randint(2, len(self.level) - 3)
        j = random.randint(2, len(self.level) - 3)
        while self.level[i][j] == '-' or self.level[i+1][j] == '-' or self.level[i-1][j] == '-':
            j = random.randint(2, len(self.level) - 3)

        x = i * 50
        y = j * 50
        return x, y

    def crown_respawn(self):
        coord = self.new_coord()
        x, y = coord
        print(x)
        print(y)
        w = Crown(x, y)
        self.all_sprites.add(w)
        self.crown = w
        self.crown_mode = True

    def del_pl(self, player):
        if self.king == player:
            self.king = None

        player.kill()

    def update(self, keys):
        current_time = pygame.time.get_ticks()
        if self.game_mode:
            self.move(keys)

            if not self.crown_mode:

                if len(self.all_players) == self.count_of_player:

                    if self.king is None:
                        self.crown_respawn()

                    else:
                        hit_king = pygame.sprite.spritecollide(self.king, self.players, False)
                        if hit_king and not self.king.god_mode:
                            self.time_god_mod = current_time + 5000
                            player = hit_king[0]
                            player.make_king(current_time + self.time_g_over)
                            self.king.make_player()
                            self.players.add(self.king)
                            self.players.remove(player)
                            self.king = player

                        if self.king.win_time < current_time:
                            self.game_mode = False
                            self.close_time = current_time + 5000

                        elif self.king.god_mode:
                            if current_time > self.time_god_mod:
                                self.king.god_mode_off()
                else:
                    if self.king is not None:
                        self.king.make_player()
                        self.players.add(self.king)
                        self.crown_mode = False
                        self.king = None

            else:
                if len(self.all_players) == self.count_of_player:
                    hit_crown = pygame.sprite.spritecollide(self.crown, self.players, False)
                    if hit_crown:
                        self.time_god_mod = current_time + 5000
                        player = hit_crown[0]
                        player.make_king(current_time + self.time_g_over)
                        self.players.remove(player)
                        self.all_sprites.remove(self.crown)
                        self.king = player
                        self.crown.kill()  # тут нужно удалить корону полностью, пока эта хрень не работает
                        self.crown_mode = False
                else:
                    self.crown.kill()
                    self.crown_mode = False
                    self.crown = None
        else:
            if current_time > self.close_time:
                raise ServExcept

    def return_players(self):
        if self.game_mode:
            data = {'status': 'upd', 'units': [], 'tk': -1}

            for elem in self.all_sprites:
                idd = elem.get_pos()
                if idd == 1:
                    data['units'].insert(0, [elem.rect.x, elem.rect.y, idd])
                else:
                    data['units'].append([elem.rect.x, elem.rect.y, idd])
            if self.king is not None:
                data['tk'] = (self.time_g_over - self.king.win_time + pygame.time.get_ticks()) // 1000
        else:
            data = {'status': 'end', 'tk': -1}

        return data

    def move(self, keys):
        for p in self.all_players:
            try:
                p.update(self.walls, keys[p.id])
            except KeyError:
                pass


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d


def dict_to_binary(the_dict):
    st = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in st)
    return binary


class Server:
    def __init__(self, host, port, world):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        flag = True
        while flag:
            try:
                self.server.bind((self.host, self.port))
                flag = False
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    self.port += 1

                else:
                    raise ServExcept
        self.player_key = {}
        self.outgoing = {}
        self.world = world
        self.count_pl = self.world.count_of_player
        self.num = 1
        self.afk_time = 30000
        self.id_set = {i for i in range(1, self.count_pl + 1)}

    def handle(self):
        d = self.server.recvfrom(1024)
        msg = binary_to_dict(d[0])
        time = pygame.time.get_ticks()
        code = msg['code']
        client_ = d[1]
        if code == 0:

            if client_ not in self.outgoing:
                if len(self.outgoing) < self.world.count_of_player:
                    id_p = self.id_set.pop()
                    return_msg = {'status': 'new_c', 'id': id_p}
                    self.outgoing[client_] = [self.world.make_pl(id_p, client_), time + self.afk_time]

                    self.server.sendto(dict_to_binary(return_msg).encode('utf-8'), client_)
                    self.num += 1
                else:
                    return_msg = {'status': 'full'}
                    self.server.sendto(dict_to_binary(return_msg).encode('utf-8'), client_)
            else:
                return_msg = {'status': 'new_c', 'id': self.outgoing[client_][0].mode//100}
                self.server.sendto(dict_to_binary(return_msg).encode('utf-8'), client_)
        elif code == 404:
            try:

                pl = self.outgoing[client_][0]
                print(pl)
                self.id_set.add(pl.mode//100)
                self.world.del_pl(pl)
            except KeyError:
                pass

            try:

                self.outgoing.pop(client_, )
                self.player_key.pop(client_, )
            except KeyError:
                pass

        else:
            try:
                self.outgoing[client_][1] = time + self.afk_time
                self.player_key[client_] = msg['keys']
            except KeyError:
                pass

    def get_world_info(self):
        if self.player_key:
            self.world.update(self.player_key)

        return self.world.return_players()

    def kick_afk(self):
        remove_list = []
        for p in self.outgoing:
            if pygame.time.get_ticks() >= self.outgoing[p][1]:
                remove_list.append(p)

        for el in remove_list:
            pl = self.outgoing[el][0]
            self.world.del_pl(pl)
            self.id_set.add(pl.mode // 100)
            try:

                self.outgoing.pop(el, )
                self.player_key.pop(el, )
            except KeyError:
                pass

    def send(self, data):
        for p in self.outgoing:
            try:
                self.server.sendto(dict_to_binary(data).encode('utf-8'), p)
            except ConnectionError as e:
                print('Send:', e)
                pass

    def get_atr(self):
        print(self.outgoing, self.player_key, self.get_world_info(), self.id_set)
