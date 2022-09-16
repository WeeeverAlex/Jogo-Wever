import pygame
import random 
from button import Button

#inicialize pygame
pygame.init()
pygame.font.init()

#-----------------------------------------------ASSETS CREDITS---------------------------------#
#I'm using some assets from a youtube video https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=30s, 
#which are Fly1.png, music.wav, Pyxeltype.ttf, player_walk_1.png and heart.png
#----------------------------------------------------------------------------------------------#


#----------------------ASSETS----------------------#
#screen
x= 1280
y= 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Loving Flies")

#music
pygame.mixer.music.load("audio/music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#background
bg3 = pygame.image.load("graphics/bg3.png")
bg2 = pygame.image.load("graphics/bg2.png")
bg = pygame.image.load("graphics/bg.jpg").convert()
bg = pygame.transform.scale(bg, (x, y))

#enemie
fly = pygame.image.load("graphics/Fly/fly1.png").convert_alpha()
pos_fly_x = 500
pos_fly_y = 350

#player
player = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player = pygame.transform.scale(player, (60, 60))
pos_player_x = 200
pos_player_y = 300

#trigger
heart = pygame.image.load("graphics/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (30, 30))
vel_heart_x = 0
pos_heart_x = 200
pos_heart_y = 300

#numbers on screen
points = 0
life = 4

#loading whiles
love = False
game = True

#rects
player_rect = player.get_rect()
fly_rect = fly.get_rect()
heart_rect = heart.get_rect()

#font
font = pygame.font.SysFont("font/Pixeltype.ttf", 50)
#-----------------------------------------------------#


#----------------------functions----------------------#

#Font for menu
def get_font(size):
    return pygame.font.SysFont("font/Pixeltype.ttf", size)

#Enemy Respawn
def respawn():
    #position of the enemy (respawn)
    x = 1400
    y = random.randint(0, 500)
    return [x, y]

#Heart Respawn
def hearts():
    #position of the hearts (respawn)
    love = False
    respawn_heart_x = pos_player_x
    respawn_heart_y = pos_player_y
    vel_heart_x = 0
    return [respawn_heart_x, respawn_heart_y, vel_heart_x, love]

#collisions
def collision():
    global points, life
    #writing on the screen commands
    if player_rect.colliderect(fly_rect) or fly_rect.x <= 60:
        life -= 1
        return True
    elif heart_rect.colliderect(fly_rect):
        points += 1
        return True
    else:
        return False

 # writing on the screen the options      
def write(msg, size, color):
    font = pygame.font.SysFont("font/Pixeltype.ttf", size, True, False)
    message = f'{msg}'
    new_text = font.render(message, True, color)
    return new_text

#used an old code(from my last pygame) and adapt it for the main menu part
def main_menu():
    menu = True
    while menu:
        screen.blit(bg2, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 80))
        PLAY_BUTTON = Button(image=None, pos=(640, 250),text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 350),text_input="OPTIONS", font=get_font(75), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 450),text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")
        screen.blit(MENU_TEXT, MENU_RECT)
        Wever = get_font(20).render("Game made by Alexandre Wever", True, "White")
        Wever_rect = Wever.get_rect(center=(1150, 570))
        screen.blit(Wever, Wever_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu = False
                    # It should be game() but I need to fix the bug (need to transform the game into a function, 
                    # but I need to transform everything into variables! So I will do it later)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
        pygame.display.update()

#used an old code(from my last pygame) and adapt it for the option part
def options():
    option = True
    while option:
        screen.blit(bg2, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONPAGE_TEXT = get_font(100).render("OPTIONS", True, "White")
        OPTIONPAGE_RECT = OPTIONPAGE_TEXT.get_rect(center=(640, 80))
        screen.blit(OPTIONPAGE_TEXT, OPTIONPAGE_RECT)
        OPTIONS_TEXT = get_font(45).render("Press W to go up and S to go down", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 250))
        OPTIONS_TEXT2 = get_font(45).render("Press SPACE to give the fly some love", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 300))
        Wever = get_font(20).render("Game made by Alexandre Wever", True, "White")
        Wever_rect = Wever.get_rect(center=(1150, 570))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        screen.blit(Wever, Wever_rect)
        OPTIONS_BACK = Button(image=None, pos=(640, 460),text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    option = False
        pygame.display.update()

#Gameover Screen
def gameover():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.blit(bg2, (0, 0))

        #write on screen
        score_board = write(f'Score: {points}', 50, (255, 255, 255))
        game_over = write('GAME OVER', 100, (225, 225, 225)) 
        end = write('PRESS RETURN TO END GAME', 40, (225, 225, 225))
        screen.blit(game_over, (400, 200))
        screen.blit(score_board, (560, 300))
        screen.blit(end, (400, 450))
        pygame.display.update()

        #if keys pressed return to the main menu    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            gameover = False
            # I need to fix the bug that I previously mentioned for it to work, 
            # but I will let main_menu() here for me to remember to do it later!
            pygame.quit()
            return  
#--------------------------------------------------------------------#  

          
#----------------------------GAME LOGIC----------------------------#
main_menu()

while game:

    screen.blit(bg, (0, 0))

    #making background move
    pos_x = x % bg.get_rect().width
    screen.blit(bg, (pos_x - bg.get_rect().width, 0))
    if pos_x < 1280:
        screen.blit(bg, (pos_x, 0))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if life <=  0 or event.type == pygame.QUIT:
            game = False
            gameover()   

    if game == False:
        break       

    #commands(flyings and shooting keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pos_player_y > 1:
        pos_player_y -= 3
        if not love:
            pos_heart_y -= 3

    if keys[pygame.K_s] and pos_player_y < 550:
        pos_player_y += 3
        if not love:
            pos_heart_y += 3

    if keys[pygame.K_SPACE]:
        love = True
        vel_heart_x = 4
            
    #enemy_respawn
    if pos_fly_x == 50:
        pos_fly_x = respawn()[0]
        pos_fly_y = respawn()[1]    
    
    #heart_respawn
    if pos_heart_x == 1100:
        pos_heart_x, pos_heart_y, vel_heart_x, love = hearts()

    #trigger_respawn
    if pos_fly_x == 50 or collision():
        pos_fly_x = respawn()[0]
        pos_fly_y = respawn()[1]

    #connecting rects
    player_rect.x = pos_player_x
    player_rect.y = pos_player_y
    fly_rect.x = pos_fly_x
    fly_rect.y = pos_fly_y
    heart_rect.x = pos_heart_x
    heart_rect.y = pos_heart_y

    #moviments
    x -= 7
    pos_fly_x -= 3
    pos_heart_x += vel_heart_x 

    #score
    score = font.render((f"Score:  {points}"), True, (255, 255, 255))
    screen.blit(score, (1000, 50))

    player_life = font.render((f"Life:  {life}"), True, (255, 255, 255))
    screen.blit(player_life, (150, 50))

    #images
    screen.blit(fly, (pos_fly_x, pos_fly_y))
    screen.blit(heart, (pos_heart_x, pos_heart_y))
    screen.blit(player, (pos_player_x, pos_player_y))

    pygame.display.update()

#--------------------------------------------------------------------#


#--------------------------------------------Things I need to fix and add to the game-----------------------------------------#
#1 - When you die, the game goes back to main menu, but you can't play again
#2 - Change the numbers that represent hearts as hearts images
#3 - Make the game harder as you get more points
#4 - For the user to be able to play the game again I need to create Classes where I can call them again and restart the game
#-----------------------------------------------------------------------------------------------------------------------------#
