import pygame
import sys
import random
import time
from pygame import mixer

pygame.init()
mixer.init()

width, height = 1440, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bank Robbery")

background = pygame.image.load("./assets/Desktop - 1.png")
background = pygame.transform.scale(background, (1440, 800))
player_image_normal = pygame.image.load("./assets/синой игрок.png")
player_image_frozen = pygame.image.load("./assets/Мертвый Синий игрок.png")
second_player_image_normal = pygame.image.load("./assets/Желтый игрок.png")
second_player_image_frozen = pygame.image.load("./assets/Мертвый желтый игрок.png")
car_image = pygame.image.load("./assets/синяя машина.png")
white_car_image = pygame.image.load("./assets/Белая машина.png")
second_car_image = pygame.image.load("./assets/Красная машинга.png")
yellow_car_image = pygame.image.load("./assets/Желтая машина.png")
table_with_money = pygame.image.load("./assets/Стол с деньгами.png")
player_with_money = pygame.image.load("./assets/Синой игрок с деньгами.png")
second_player_with_money = pygame.image.load("./assets/Желтый игрок с деньгами.png")
Car_with_money = pygame.image.load("./assets/Машинка белого игрока.png")
Second_car_with_money = pygame.image.load("./assets/Машинка желтого игрока.png")
first_car_x, first_car_y = 380, -300
second_car_x, second_car_y = 700, -height
x, y = 310, 230
x2, y2 = 310, 430
speed = 10
table_x = 1100
table_y = 100
Cwm_x, cwm_y = 0, 200
cwm2_x, cwm2_y = 0, 400
blue_score = 0
yellow_score = 0
first_car_speed, second_car_speed = 10, 10
freeze_duration = 2
freeze_start_time_player1 = 0
freeze_start_time_player2 = 0

font = pygame.font.Font(None, 25)  # Задаем шрифт и размер текста

clock = pygame.time.Clock()
facing_horizontal1 = False
facing_horizontal2 = False
random_car_image = random.choice([car_image, white_car_image])
random_sec_car_image = random.choice([second_car_image, yellow_car_image])

start_time = time.time()
game_duration = 60

pygame.mixer.music.load("./assets/game.mp3")
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)
collision_sound = pygame.mixer.Sound("./assets/money.mp3")
collision_car_sound = pygame.mixer.Sound('./assets/collision.mp3')
def freeze_player(player):
    if player == 1:
        global freeze_start_time_player1
        collision_car_sound.play()
        freeze_start_time_player1 = time.time()
    elif player == 2:
        global freeze_start_time_player2
        collision_car_sound.play()
        freeze_start_time_player2 = time.time()


def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)

    # Проверка наличия заморозки
    is_frozen_player1 = time.time() - freeze_start_time_player1 < freeze_duration
    is_frozen_player2 = time.time() - freeze_start_time_player2 < freeze_duration

    if not is_frozen_player1:
        if keys[pygame.K_a] and x > 0:
            x -= speed
            facing_horizontal1 = False
        if keys[pygame.K_d] and x < width - 350:
            facing_horizontal1 = True
            x += speed
        if keys[pygame.K_w] and y > 0:
            y -= speed
        if keys[pygame.K_s] and y < height-100:
            y += speed

    if not is_frozen_player2:
        if keys[pygame.K_LEFT] and x2 > 0:
            x2 -= speed
            facing_horizontal2 = False
        if keys[pygame.K_RIGHT] and x2 < width - 350:
            facing_horizontal2 = True
            x2 += speed
        if keys[pygame.K_UP] and y2 > 0:
            y2 -= speed
        if keys[pygame.K_DOWN] and y2 < height-100:
            y2 += speed

    player_rect1 = pygame.Rect(x, y, player_image_normal.get_width() - 200, player_image_normal.get_height() - 200)
    player_rect2 = pygame.Rect(x2, y2, second_player_image_normal.get_width() - 200,
                               second_player_image_normal.get_height() - 200)
    first_car_rect = pygame.Rect(first_car_x, first_car_y, 200, car_image.get_height() - 400)
    second_car_rect = pygame.Rect(second_car_x, second_car_y, 200, second_car_image.get_height() - 400)
    table_rect = pygame.Rect(table_x, table_y, table_with_money.get_width() - 300, table_with_money.get_height())
    Car_w_money_rect = pygame.Rect(Cwm_x, cwm_y, Car_with_money.get_width()-200, Car_with_money.get_height())
    Sec_car_w_money_rect = pygame.Rect(cwm2_x, cwm2_y, Second_car_with_money.get_width()-100,
                                       Second_car_with_money.get_height())

    # Проверка столкновения с первой машиной
    if not is_frozen_player1 and is_collision(player_rect1, first_car_rect):
        freeze_player(1)
        player_image_normal = pygame.image.load("./assets/синой игрок.png")

    # Проверка столкновения с второй машиной
    if not is_frozen_player1 and is_collision(player_rect1, second_car_rect):
        freeze_player(1)
        player_image_normal = pygame.image.load("./assets/синой игрок.png")

    # Проверка столкновения с первой машиной для второго игрока
    if not is_frozen_player2 and is_collision(player_rect2, first_car_rect):
        freeze_player(2)
        collision_car_sound.play()
        second_player_image_normal = pygame.image.load("./assets/Желтый игрок.png")

    # Проверка столкновения с второй машиной для второго игрока
    if not is_frozen_player2 and is_collision(player_rect2, second_car_rect):
        freeze_player(2)
        collision_car_sound.play()
        second_player_image_normal = pygame.image.load("./assets/Желтый игрок.png")

    if not is_frozen_player1  and is_collision(player_rect1, table_rect):
        player_image_normal = player_with_money
        

    if not is_frozen_player2 and is_collision(player_rect2, table_rect):
        second_player_image_normal = second_player_with_money
        
        
    if not is_frozen_player1  and is_collision(player_rect1, Car_w_money_rect) and player_image_normal == player_with_money:
        collision_sound.play()
        player_image_normal = pygame.image.load("./assets/синой игрок.png")
        blue_score += 100
    
    if not is_frozen_player1  and is_collision(player_rect2, Sec_car_w_money_rect) and second_player_image_normal == second_player_with_money:
        collision_sound.play()
        second_player_image_normal = pygame.image.load("./assets/Желтый игрок.png")
        yellow_score += 100
        
    screen.blit(background, (0, 0))
    screen.blit(table_with_money, (table_x, table_y))
    screen.blit(Car_with_money, (Cwm_x, cwm_y))
    screen.blit(Second_car_with_money, (cwm2_x, cwm2_y))
    
    if remaining_time == 0:
        pygame.mixer.music.stop()
        # Время вышло, определение победителя
        if blue_score > yellow_score:
            winner_text = pygame.image.load("./assets/Blue Player Wins.png")
        elif yellow_score > blue_score:
            winner_text = pygame.image.load("./assets/Yellow Player Wins.png")
        else:
            winner_text = pygame.image.load("./assets/Friendship.png")

        screen.blit(winner_text, (300, 0))
        mixer.music.load("./assets/win.mp3")
        mixer.music.play()
        pygame.display.flip()
        pygame.time.delay(5000)  # Отображаем результаты на 5 секунд перед завершением игры
        running = False

    if is_frozen_player1:
        screen.blit(player_image_frozen,(x,y))
    elif not is_frozen_player1:
        if facing_horizontal1:
            player_image_flipped = pygame.transform.flip(player_image_normal, True, False)
            screen.blit(player_image_flipped, (x, y))
        else:
            screen.blit(player_image_normal, (x, y))

    if is_frozen_player2:
        screen.blit(second_player_image_frozen,(x2,y2))
    elif not is_frozen_player2:
        if facing_horizontal2:
            second_player_image_flipped = pygame.transform.flip(second_player_image_normal, True, False)
            screen.blit(second_player_image_flipped, (x2, y2))
        else:
            screen.blit(second_player_image_normal, (x2, y2))

    first_car_y += first_car_speed
    screen.blit(random_car_image, (first_car_x, first_car_y))

    if first_car_y > height:
        first_car_y = -300
        first_car_x = 380
        first_car_speed = random.randint(5, 20)
        random_car_image = random.choice([car_image, white_car_image])

    screen.blit(random_sec_car_image, (second_car_x, second_car_y))
    second_car_y -= second_car_speed
    if second_car_y < -height:
        second_car_y = height
        second_car_x = 680
        second_car_speed = random.randint(5, 20)
        random_sec_car_image = random.choice([second_car_image, yellow_car_image])

    # Отображение счета
    score_text = font.render(f"Blue Score: {blue_score} | Yellow Score: {yellow_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    clock.tick(60)
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
