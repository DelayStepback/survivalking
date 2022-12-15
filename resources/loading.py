import pygame 



def load_info():
    return pygame.image.load('images\\skin\\info.jpg').convert()

def load_bg():
    background = pygame.image.load('images\\skin\\MakingMap.png').convert()
    return background

def load_wall():
    wall = pygame.image.load('images\\skin\\wall.png').convert()
    return wall

def load_skins():
    '''
    load_skins() - возвращает скины в массиве двумерном от 0 до 3 - житель
    от 4-7 король. 
    '''
    # Загрузка всей игровой графики
    walkUp = [
    pygame.image.load('images\\skin\\village\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\back_stand.png').convert_alpha()]

    walkRight = [
    pygame.image.load('images\\skin\\village\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\village\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\village\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\village\\front_stand.png').convert_alpha()]
    
    # король скин
    walkUP_K = [
    pygame.image.load('images\\skin\\king\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\back_stand.png').convert_alpha()]
    
    walkRight_K = [
    pygame.image.load('images\\skin\\king\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\right_stand.png').convert_alpha()]
    
    walkLeft_K = [
    pygame.image.load('images\\skin\\king\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\left_stand.png').convert_alpha()]
    
    walkDown_K = [
    pygame.image.load('images\\skin\\king\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\king\\front_stand.png').convert_alpha()]




    walk = [walkLeft, walkRight, walkDown, walkUp,
    walkLeft_K, walkRight_K, walkDown_K, walkUP_K]
    return walk

def load_god():
    walkUP_K = [
    pygame.image.load('images\\skin\\god\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\back_stand.png').convert_alpha()]
    
    walkRight_K = [
    pygame.image.load('images\\skin\\god\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\right_stand.png').convert_alpha()]
    
    walkLeft_K = [
    pygame.image.load('images\\skin\\god\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\left_stand.png').convert_alpha()]
    
    walkDown_K = [
    pygame.image.load('images\\skin\\god\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\god\\front_stand.png').convert_alpha()]

    return [walkLeft_K, walkRight_K, walkDown_K, walkUP_K]



def load_crown():
    return pygame.image.load('images\\skin\\crown\\crown.png').convert_alpha()

def load_alh():
    walkUp = [
    pygame.image.load('images\\skin\\alh\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\alh\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\alh\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\alh\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\alh\\front_stand.png').convert_alpha()]
     
    walk = [walkLeft, walkRight, walkDown, walkUp]
    
    return walk

def load_knight():
    walkUp = [
    pygame.image.load('images\\skin\\knight\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\knight\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\knight\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\knight\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\knight\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]


def load_lady():
    walkUp = [
    pygame.image.load('images\\skin\\lady\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\lady\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\lady\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\lady\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\lady\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]


def load_priest():
    walkUp = [
    pygame.image.load('images\\skin\\priest\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\priest\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\priest\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\priest\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\priest\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]

def load_ghost():
    walkUp = [
    pygame.image.load('images\\skin\\ghost\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\ghost\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\ghost\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\ghost\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\ghost\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]

def load_witch():
    walkUp = [
    pygame.image.load('images\\skin\\witch\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\witch\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\witch\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\witch\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\witch\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]


def load_jester():
    walkUp = [
    pygame.image.load('images\\skin\\jester\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\back_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\back_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\back_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\back_stand.png').convert_alpha()]
    
    walkRight = [
    pygame.image.load('images\\skin\\jester\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\right_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\right_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\right_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\right_stand.png').convert_alpha()]
    
    walkLeft = [
    pygame.image.load('images\\skin\\jester\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\left_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\left_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\left_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\left_stand.png').convert_alpha()]
    
    walkDown = [
    pygame.image.load('images\\skin\\jester\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\front_stand.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\front_move_1.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\front_move_2.png').convert_alpha(),
    pygame.image.load('images\\skin\\jester\\front_stand.png').convert_alpha()]


    return [walkLeft, walkRight, walkDown, walkUp]
