import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, atribute, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.rect = pygame.Rect(x, y, 50, 100)
        self.speedx = 0
        self.speedy = 0
        self.default_speed = 8
        self.king = False
        self.god_mode = False
        self.id = id
        self.mode = atribute * 100
        self.pos = self.mode
        self.win_time = 0

    def update(self, walls, keys):
        self.speedx = 0
        self.speedy = 0
        if keys[0] or keys[1] or keys[2] or keys[3]:

            if keys[0]:
                self.speedx = -self.default_speed
                self.pos = self.mode + 1
            elif keys[1]:
                self.speedx = self.default_speed
                self.pos = self.mode + 2
            if keys[2]:
                self.speedy = -self.default_speed
                self.pos = self.mode + 3
            elif keys[3]:
                self.speedy = self.default_speed
                self.pos = self.mode + 4
        else:
            self.pos = self.mode
        self.collide(walls)

    def collide(self, walls):
        self.rect.x += self.speedx
        wl = pygame.sprite.spritecollide(self, walls, False)
        if wl:
            if self.speedx > 0:
                self.rect.right = wl[0].rect.left
            else:
                self.rect.left = wl[0].rect.right

        self.rect.y += self.speedy
        wl = pygame.sprite.spritecollide(self, walls, False)

        if wl:
            if self.speedy > 0:
                self.rect.bottom = wl[0].rect.top
            else:
                self.rect.top = wl[0].rect.bottom

    def make_king(self, t):
        self.win_time = t
        self.default_speed = 12
        self.king = True
        self.god_mode = True

    def god_mode_off(self):
        self.default_speed = 10
        self.god_mode = False

    def make_player(self):
        self.king = False
        self.god_mode = False
        self.default_speed = 8

    def get_pos(self):
        if self.king:
            self.pos += 5
        if self.god_mode:
            self.pos += 5
        return self.pos

    
class Crown(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 40, 80)
        # self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = 1

    def get_pos(self):
        return self.pos


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # требуется в Pygame для всех спрайтов
        self.image = pygame.Surface((50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)  # координаты и размеры
