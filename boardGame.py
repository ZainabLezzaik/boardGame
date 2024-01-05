#Zainab Lezzaik
#101263105

#import the libraries that i have to use
import pygame
import random
#initialize the pgame font
pygame.font.init()

#this will create the drawing window for 700 width and 800 height
display = pygame.display.set_mode((700, 800))
width, height = 700, 800

#i have 7 rows and 8 columns
rows, columns = 7, 8
#the square dimension of each is 100
square_dim = 100
#this will get the size of each square (width//rows) and (length//columns)
square_size_height = 800//columns
square_size_width = 700//rows

#this will set the name "Board Game" at the top of the display
pygame.display.set_caption ('Board Game')

#rgb colours that i would use
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (254,239,0)

#Nested FOR loops to make the checker board pattern
display.fill ((255,255,255))
for row in range (rows+1):  
    #i used row % 2 to draw the columns in pattern, this will allow it to step by two when drawing each rect colour
    for cols in range(row % 2, rows+1, 2):
        #draw rectangle with colour white starting from the top left, 
        #the formula row*square_size_width and col*square_size_height will calculate where the top left & right should be
        pygame.draw.rect (display, RED ,(row*square_size_width, cols*square_size_height, square_size_width, square_size_height) )
        pygame.display.update()
        pygame.time.delay(100)

#NUMBERED TILES FEATURE
number_tile = 1
for row in range (0, columns):
    for cols in range (0, rows):
        font_type = pygame.font.SysFont ("Sans Serif", 28)
        text_ren = font_type.render(str(number_tile), True, (0,255,0))
        display.blit(text_ren, ((cols*square_dim)+10, (row*square_dim)+9))
        number_tile+= 1
        pygame.display.update()

#this will copy the entire display with the numbered tile
check = display.copy()

x1 = 50        #initial x position of player 1 on the FIRST TILE
y1 = 50        #initial y position of player 1 on the FIRST TILE
x2 = 50        #initial x position of player 2 on the FIRST TILE
y2 = 50        #initila y position of player 2 on the FIRST TILE

#THIS will draw both players on the first tile for 2 seconds
#this will draw player 1 as a green circle
pygame.draw.circle(display, GREEN, (x1,y1), 35)
#this will draw player 2 as a yellow circle
pygame.draw.circle(display, YELLOW, (x2,y2), 30)
pygame.display.update()
#this will keep everything in the display current
pygame.event.pump ()
pygame.time.delay (2000)

#WHILE loop
flag = True
while flag:
    #roll dice 1 and dice 2 then add them to one dice
    dice1 = random.randint(1,3)
    dice2 = random.randint(1,3)
    dice = dice1 + dice2            #maximum value that we get from rolling a 2 3-sided dices is 6
    print ("You rolled a", dice1, "from the first dice. You rolled a ",dice2, " from the second dice", ".", "Now player 1 will move by", dice, "tiles.")

    #condition if the (position of player 1 + the number of the dice we rolled multiplied by sq dimensions) is higher than the width of the window
    #multiply the value of the dice by the square dimensions which is 100 and add that to the x-posiiton of the player
    x1 += dice*square_dim 
    if x1 > width:
        x1 = x1 - width   #subtract the width size in order to get the new position of the player on the second row
        y1 = y1 + square_dim   #add 100 which is the square dim to the y value of player 1 to get the new y posiiton of player 1
        display.blit(check, (0,0))    #blit the new display
        pygame.draw.circle(display, GREEN, (x1,y1), 33)       #this will draw the new position of player 1
        pygame.draw.circle(display, YELLOW, (x2,y2), 28)        #this will draw player 2 in its old position
        pygame.display.update()
        #this will keep everything current and gets rid of the bugs
        pygame.event.pump ()   
        #this will delay the time by 2 sec                   
        pygame.time.delay (2000)

       #if the new position of the player is within the same row
       #this will draw the new position of player 1 when it doesn't change rows
    else:
        pygame.draw.circle(display, GREEN, (x1,y1), 33)       
        pygame.display.update ()              #update the display
        display.blit (check, (0,0))
        pygame.draw.circle(display, GREEN, (x1,y1), 33)
        pygame.draw.circle(display, YELLOW, (x2,y2), 28)
        pygame.display.update()
        pygame.event.pump ()          #this will keep everything current and gets rid of the bugs
        pygame.time.delay (2000)          #this will delay the time by 2 seconds

    #this checks if player 1 reaches the last tile (square 56), and in case they did it will terminate the game and draw the player on the last square
    #this is the EXACT REQUIREMENT FEATURE, PLAYERS CANNOT MOVE PAST THE BOARD
    #this will DRAW  the WINNER PLAYER on the LAST TILE and it will take the LOSER PLAYER back to the FIRST square/tile  
    if y1 > 700 or (x1>=650 and y1>=750):        
        display.blit(check, (0,0))
        #this will draw the GREEN player on the last square/tile since it will be the winner in this case
        pygame.draw.circle(display, GREEN, (650,750), 33)  
        #this will take back the YELLOW player on the first square/tile since it lost  
        pygame.draw.circle(display, YELLOW, (50,50), 28)
        pygame.display.update()
        pygame.event.pump ()
        #this will print the winner
        print ("The first GREEN Player Won !!")
        break
    else:
        pass

    #condition when player 2 is rolling
    #roll 2 dices then add them together
    dice1_p2 = random.randint(1,3)
    dice2_p2 = random.randint (1,3)
    dice2 = dice1_p2 + dice2_p2
    print ("You rolled a",dice1_p2, "from the first dice.","And you rolled", dice2_p2,"from the second dice.",".", "Now player 2 will move by", dice2, "tiles.")
    
    #condition if the (position of player 2 + the number of the dice we rolled multiplied by sq dimensions) is higher than the width of the window
    #multiply the value of the dice by the square dimensions which is 100 and add that to the x-posiiton of the player
    x2 += dice2 * square_dim
    if x2 > width:
        x2 = x2 - width                         #subtract the width from thr new position of player 2
        y2= y2 + square_dim                     #add the square dimension (100) to the y position of player 2
        display.blit (check, (0,0))
        pygame.draw.circle(display, YELLOW, (x2,y2), 28) #this will draw player 2 at the new position
        pygame.draw.circle(display, GREEN, (x1,y1), 33) #this will draw player 1 at its old position
        pygame.display.update()
        pygame.event.pump ()
        pygame.time.delay (2000)  #delay by 2 sec

    #condition if the new position of player 2 is within the same row 
    #this will draw the new position of player 1 when it doesn't change rows
    else:
        pygame.draw.circle(display, YELLOW, (x2,y2), 28)
        pygame.display.update ()
        display.blit (check, (0,0))
        pygame.draw.circle(display, GREEN, (x1,y1), 33)
        pygame.draw.circle(display, YELLOW, (x2,y2), 28)
        pygame.display.update()
        pygame.event.pump ()        #keep everything current
        pygame.time.delay (2000)        #time delay by 2 seconds
        
    #this checks if player 2 reached the last square/tile and won, and it would terminate the game if they did
    #this is the EXACT REQUIREMENT FEATURE, PLAYERS CANNOT MOVE PAST THE BOARD
    #this will DRAW  the WINNER PLAYER on the LAST TILE and it will take the LOSER PLAYER back to the FIRST square/tile

    if y2 > 700 or (x2>=650 and y2>=750):          
        display.blit(check, (0,0))
        #this will draw the YELLOW circle on the square/tile since it won
        pygame.draw.circle(display, YELLOW, (650,750),28)
        #this will draw thE GREEN circle on the first square/tile since it lost
        pygame.draw.circle (display, GREEN, (50,50), 33)
        print ("The second YELLOW Player won!!")
        pygame.display.update()
        pygame.event.pump()
        break
    else:
        pass

pygame.display.update()

#while loop that terminates when either player reaches the end
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit ()



