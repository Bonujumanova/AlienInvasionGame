import pygame
import sys
from dataclasses import dataclass
from random import randint

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # default is (0,0), so it's fullscreen
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
SCREEN_HEIGHT = SCREEN_HEIGHT - 100

#длина и ширина экрана
#------------------------ CONSTANTS SECTION START ------------------------#
#SCREEN_WIDTH      = 1600
#SCREEN_HEIGHT     = 1200

ALIEN_SHIP_WIDTH  = 120
ALIEN_SHIP_HEIGHT = 120

ROCKET_WIDTH      = 70
ROCKET_HEIGHT     = 110

ROCKET_START_X    = SCREEN_WIDTH // 2-25

BULLET_OFFSET     = 35
BULLET_RADIUS     = 10

COLOR_RED_BURGUNDY = (154, 0, 0)
COLOR_SKY_BLUE     = (153, 204, 255)


MOVE_STEP          = 3

# количество кораблей
ALIEN_SHIP_NUM     = SCREEN_WIDTH  //  ( 2 * ALIEN_SHIP_WIDTH)

#------------------------ CONSTANTS SECTION END   ------------------------#

#------------------------ DATACLASSES SECTION START ------------------------#

@dataclass
class Player:
    x : int
    y : int

@dataclass
class Enemy:
    x        : int  = 0 
    y        : int  = 0
    is_alive : bool = True
    bullet   : str  = None

@dataclass
class Bullet:
    x         : int  = 0
    y         : int  = 1080
    is_active : bool = False

@dataclass
class Alien_bullet:
    x : int
    y : int

#------------------------ DATACLASSES SECTION END   ------------------------#
#
Player1 = Player(0, 0)
Player1.x = SCREEN_WIDTH//2
# 20 - потому что корабль уходит за экран по оси y
Player1.y = SCREEN_HEIGHT - 20
# 

Bullet1   = Bullet(0, 0)
Bullet1.x = Player1.x  + BULLET_OFFSET
Bullet1.y = Player1.y

#


#
'''
alien_ship_list = []
for items in range(ALIEN_SHIP_NUM):
    alien_ship_list.append(Enemy())
'''

alien_ship_list = []
for items in range(ALIEN_SHIP_NUM):
    new_alien = Enemy()
    new_alien2 = Enemy()
    new_alien2. y = 200               # Создать экземпляр датакласса Enemy
    new_alien.bullet = Bullet()       # Создать экземпляр датакласса Bullet, который принадлежит экземпляру датакласса Enemy
    new_alien2.bullet = Bullet()
    alien_ship_list.append(new_alien) # Поместить созданный обьект в список
    alien_ship_list.append(new_alien2)
print(alien_ship_list)
# 
bullet_list = []

# Список пуль игрока
player_bulet_list = []

aviable_space_x = SCREEN_WIDTH - ( ALIEN_SHIP_WIDTH)
alien_number = 0
alien_number2 = 0
for alien in alien_ship_list:
    if alien.y == 200:
        alien.x = ALIEN_SHIP_WIDTH + 2 * ALIEN_SHIP_WIDTH * alien_number2
        alien_number2 += 1
    else:
        alien.x = ALIEN_SHIP_WIDTH + 2 * ALIEN_SHIP_WIDTH * alien_number
        alien_number +=1


# создаю игровое окно
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



# загружаю косм. корабль, задаю его координаты
img_rocket = pygame.image.load("/home/bonu/Desktop/Rocket/images/rocket-png-40816.bmp")
img_rocket = pygame.transform.scale(img_rocket, (ROCKET_WIDTH, ROCKET_HEIGHT ))

img_finish_game = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(6).png")
w = 120
h = 120



#загружаю кнопку restart
restart_img = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(12).png")
restart_img = pygame.transform.scale(restart_img, (200, 200))

# Выход из игры 
exit_game_img = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(13).png")
exit_game_img = pygame.transform.scale(exit_game_img, (250,  180))

# Загружаю корабль врага
alien_ship = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(2).png")
alien_ship = pygame.transform.scale(alien_ship, (ALIEN_SHIP_WIDTH, ALIEN_SHIP_HEIGHT))

# Задний фон начального экрана
start_background = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(9).png")
start_background = pygame.transform.scale(start_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Загрузка картинки Play
play_image = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(3).png")
play_image = pygame.transform.scale(play_image, (250, 180))
X_play_image = SCREEN_WIDTH//2 - (250//2)
Y_play_image = SCREEN_HEIGHT//2 - (180 // 2)

#X_coord_ship = ROCKET_START_X
#Y_coord_ship = 0
# Ограничение вывода кадров в сек
clock = pygame.time.Clock()
fps = 60
# Подсчет секунд
count_sek = 0

#загружаю музыку и задаю громкость(0 - 1)
start_music = pygame.mixer.music.load("/home/bonu/Documents/♪ ALIENS THE MUSICAL - Animation Parody.mp3")
pygame.mixer.music.set_volume(0.03)

# Назначаю флаги, отвечающие за движение направо, налево
Sprite_moving_right = False
Sprite_moving_left = False
# Назначаю флаг стрельбы из ракеты
Sprite_is_shooting = False
# Флаг, который позволяетт отображать пока еще незастрелянный корабль
alien_ship_dead = False
player_is_alive = True

start_game = False

start_music_play = True
stop_music_play = False
exit_game = False
restart_game = False
#Координаты пули ракеты
#X_shoot = Player1.x  + BULLET_OFFSET
#Y_shoot = Player1.y

alien_bullet_move = None
bullet_is_launched = False

# движение направо
def move_player_right(boolean_meaning):
    global Player1
    if boolean_meaning == True and Player1.x  + ROCKET_WIDTH < SCREEN_WIDTH:
        Player1.x += MOVE_STEP

# Движение налево
def move_player_left(boolean_meaning):
    global Player1
    if boolean_meaning == True and Player1.x  > 0:
        Player1.x -= MOVE_STEP

# Движение пуль ракеты
def move_bullet(y_coord):
    if y_coord > -10:
        y_coord -= MOVE_STEP
    return y_coord

'''# флотилия инопланитян
def find_alien_ship_coords():
    global SCREEN_WIDTH
    global alien_ship_coords
    global ALIEN_SHIP_WIDTH
    global Alien_ship
    aviable_space_x = SCREEN_WIDTH - ( ALIEN_SHIP_WIDTH)
    number_aliens_x = aviable_space_x // ( 2 * ALIEN_SHIP_WIDTH)
    alien_ship_coords= []
    for alien_number in range(number_aliens_x):
        Alien_ship.x = ALIEN_SHIP_WIDTH + 2* ALIEN_SHIP_WIDTH * alien_number
        alien_ship_coords.append(Alien_ship.x)
'''
    
#Запускаю окошко
while True:
    count_sek += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #джижение направо или налево при зажатии на соотвеств. клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Sprite_moving_right = True
            if event.key == pygame.K_LEFT:
                Sprite_moving_left = True
            if event.key == pygame.K_UP:
                # Рисую пули
                Bullet1.x = Player1.x + BULLET_OFFSET
                Bullet1.y = Player1.y
                Sprite_is_shooting = True
                player_bulet_list.append(Bullet(Bullet1.x, Bullet1.y))
          
                pygame.mixer.music.load("/home/bonu/Desktop/Rocket/Alien_sound/laser-blast-descend_gy7c5deo.mp3")
                pygame.mixer.music.play()

             
        if event.type == pygame.KEYUP:
            Sprite_moving_right = False
            Sprite_moving_left = False
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos 
            if X_play_image < mouse[0] < X_play_image + 250 and Y_play_image < mouse[1] < Y_play_image+180:
                start_game = True


            # нажатие на кнопки после окончания игры
            if player_is_alive == False:
                if SCREEN_WIDTH // 2 + 300 < mouse[0] < SCREEN_WIDTH // 2 + 300 + 250 and SCREEN_HEIGHT // 2 - 80 < mouse[1] < SCREEN_HEIGHT // 2 - 100 +180:
                    exit_game = True
                if SCREEN_WIDTH // 2 - 500 < mouse[0] < SCREEN_WIDTH // 2 - 500 + 200 and SCREEN_HEIGHT // 2 - 80 < mouse[1] < SCREEN_HEIGHT // 2 - 80 + 200:
                    restart_game = True
    if exit_game == True:
        pygame.quit()
        sys.exit()

    if restart_game == True:
        # =============================================Restart Game Code Start=========================================================
        @dataclass
        class Player:
            x : int
            y : int

        @dataclass
        class Enemy:
            x        : int  = 0 
            y        : int  = 0
            is_alive : bool = True
            bullet   : str  = None

        @dataclass
        class Bullet:
            x         : int  = 0
            y         : int  = 1080
            is_active : bool = False

        @dataclass
        class Alien_bullet:
            x : int
            y : int

        #------------------------ DATACLASSES SECTION END   ------------------------#
        #
        Player1 = Player(0, 0)
        Player1.x = SCREEN_WIDTH//2
        Player1.y = SCREEN_HEIGHT - 20
        # 

        Bullet1   = Bullet(0, 0)
        Bullet1.x = Player1.x  + BULLET_OFFSET
        Bullet1.y = Player1.y

        #
        '''
        alien_ship_list = []
        for items in range(ALIEN_SHIP_NUM):
            alien_ship_list.append(Enemy())
        '''

        alien_ship_list = []
        for items in range(ALIEN_SHIP_NUM):
            new_alien = Enemy()               # Создать экземпляр датакласса Enemy
            new_alien.bullet = Bullet()       # Создать экземпляр датакласса Bullet, который принадлежит экземпляру датакласса Enemy
            alien_ship_list.append(new_alien) # Поместить созданный обьект в список


        bullet_list = []

        # Список пуль игрока
        player_bulet_list = []

        aviable_space_x = SCREEN_WIDTH - ( ALIEN_SHIP_WIDTH)
        alien_number = 0
        for alien in alien_ship_list:
            alien.x = ALIEN_SHIP_WIDTH + 2 * ALIEN_SHIP_WIDTH * alien_number
            alien_number += 1

        # создаю игровое окно
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 

        # загружаю косм. корабль, задаю его координаты
        img_rocket = pygame.image.load("/home/bonu/Desktop/Rocket/images/rocket-png-40816.bmp")
        img_rocket = pygame.transform.scale(img_rocket, (ROCKET_WIDTH, ROCKET_HEIGHT ))

        img_finish_game = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(6).png")
        w = 120
        h = 120

        #загружаю кнопку restart
        restart_img = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(12).png")
        restart_img = pygame.transform.scale(restart_img, (200, 200))

        # Выход из игры 
        exit_game_img = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(13).png")
        exit_game_img = pygame.transform.scale(exit_game_img, (250,  180))

        # Загружаю корабль врага
        alien_ship = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(2).png")
        alien_ship = pygame.transform.scale(alien_ship, (ALIEN_SHIP_WIDTH, ALIEN_SHIP_HEIGHT))

        # Задний фон начального экрана
        start_background = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(9).png")
        start_background = pygame.transform.scale(start_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


        # Загрузка картинки Play
        play_image = pygame.image.load("/home/bonu/Desktop/Rocket/images/pngwing.com(3).png")
        play_image = pygame.transform.scale(play_image, (250, 180))
        X_play_image = SCREEN_WIDTH//2 - (250//2)
        Y_play_image = SCREEN_HEIGHT//2 - (180 // 2)

        #X_coord_ship = ROCKET_START_X
        #Y_coord_ship = 0
        # Ограничение вывода кадров в сек
        clock = pygame.time.Clock()
        fps = 60
        # Подсчет секунд
        count_sek = 0

        start_music = pygame.mixer.music.load("/home/bonu/Documents/♪ ALIENS THE MUSICAL - Animation Parody.mp3")


        # Назначаю флаги, отвечающие за движение направо, налево
        Sprite_moving_right = False
        Sprite_moving_left = False
        # Назначаю флаг стрельбы из ракеты
        Sprite_is_shooting = False
        # Флаг, который позволяетт отображать пока еще незастрелянный корабль
        alien_ship_dead = False
        player_is_alive = True

        start_game = False

        start_music_play = True
        stop_music_play = False
        exit_game = False
        restart_game = False
        #Координаты пули ракеты
        #X_shoot = Player1.x  + BULLET_OFFSET
        #Y_shoot = Player1.y

        alien_bullet_move = None
        bullet_is_launched = False
        
    # RESTART code end
    # =============================================-=========================================================


    if start_music_play == True and start_game == False and stop_music_play == False:
        pygame.mixer.music.play(-1)
        start_music_play = False
        
    if stop_music_play == True and start_game == False:
        pygame.mixer.music.unload()
        
        

    # заполнили цветом задний фон, вывели картинку на экран, обновили экран
    #screen.fill(COLOR_SKY_BLUE)
    if start_game == True:
        pygame.mixer.music.rewind
        stop_music_play = True
        
        screen.fill((COLOR_SKY_BLUE))
        for i in alien_ship_list:
            if i.is_alive == True:
                if (count_sek % 15 == 0):
                    i.y += 3
                screen.blit(alien_ship, (i.x, i.y))
                

                rand = randint(1,1000)
                if rand == 500 and i.bullet.is_active == False:
                    i.bullet.x = i.x+ALIEN_SHIP_WIDTH//2
                    i.bullet.y = i.y + 120
                    i.bullet.is_active = True
                    bullet_list.append((i.bullet))
                    bullet_is_launched = True
                    #pygame.draw.circle(screen, COLOR_RED_BURGUNDY, (i.x+ALIEN_SHIP_WIDTH//2,  alien_bullet_move),BULLET_RADIUS, 0)

            if (i.x < Bullet1.x < i.x + ALIEN_SHIP_WIDTH) and \
                (i.y < Bullet1.y < i.y +ALIEN_SHIP_HEIGHT):
                i.is_alive = False
                
        # else:
                #screen.blit(img_rocket, (Player1.x , Player1.y))

        for i in bullet_list:
            i.y += 6
            pygame.draw.circle(screen, COLOR_RED_BURGUNDY, (i.x,  i.y),BULLET_RADIUS, 0)
            # проверкавражеская пуля попала или нет на корабль игрока
            if Player1.x <= i.x<= Player1.x + ROCKET_WIDTH and Player1.y <= i.y:
                player_is_alive = False
    

            if i.y > SCREEN_HEIGHT:
                i.is_active = False
                bullet_list.remove(i)
        if player_is_alive == True:
            screen.blit(img_rocket, (Player1.x , Player1.y))
        else:
            for i in range(1, 10):
                if w <= 360:
                    w += i
                
            if w <= 700:
                img_finish_game = pygame.transform.scale(img_finish_game, (w, w))
                screen.blit(img_finish_game, (SCREEN_WIDTH //2 - w//2 , SCREEN_HEIGHT//2 - w//2))
            else:
                
                screen.blit(img_finish_game, (SCREEN_WIDTH //2 - w//2 , SCREEN_HEIGHT//2 - w//2))  
            screen.blit(img_finish_game, (SCREEN_WIDTH //2 - w//2 , SCREEN_HEIGHT//2 - w//2))  
            screen.blit(restart_img, (SCREEN_WIDTH // 2 - 500, SCREEN_HEIGHT // 2 - 80))
            screen.blit(exit_game_img, ((SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT // 2 - 100)))
            alien_ship_list.clear()




            # Вывод bullet инопланитян
        ''' alien_bullet_move = move_alien_bullet(y_coord_alien_ship, SCREEN_HEIGHT)
            pygame.draw.circle(screen, COLOR_RED_BURGUNDY, (Alien_bullet1.x, alien_bullet_move),BULLET_RADIUS, 0)'''
            
    
        
        # Вызов функций
        move_player_right(Sprite_moving_right)
        move_player_left(Sprite_moving_left)
        
        # Вывод пули, которую выстрелили и она летит вверх
        if Sprite_is_shooting == True and player_is_alive == True:

            # вызов функции стрельбы из ракеты
            

            for player_bullet in player_bulet_list:
                player_bullet.y -= 3
                pygame.draw.circle(screen, COLOR_RED_BURGUNDY, (player_bullet.x, player_bullet.y),BULLET_RADIUS, 0)
                if player_bullet.y < 0:
                    player_bulet_list.remove(player_bullet)
        for i in player_bulet_list:
            for j in alien_ship_list:
                if j.x < i.x < j.x + ALIEN_SHIP_WIDTH and j.y < i.y < j.y + ALIEN_SHIP_HEIGHT:
                    j.is_alive = False
                    
    else:
        screen.blit(start_background, (0, 0))
        screen.blit(play_image, (X_play_image , Y_play_image))
        

    
    #find_alien_ship_coords()
    # Вывод 60 кадров в сек
    clock.tick(fps)
    pygame.display.flip()
