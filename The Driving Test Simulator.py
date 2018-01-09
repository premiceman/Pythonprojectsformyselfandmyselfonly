###-------------------------------------------------------------------PREM VYAS----------------------------------------------------------------------------------------
###-------------------------------------------------------------------BEGINNING OF PROGRAM-----------------------------------------------------------------------------
#--------------------------------------------------------------Importing python and pygame modules---------------------------------------------------------------------
import pygame                                                       
import time
import sys
import random

#--------------------------------------------------------------Initiating the pygame functionality---------------------------------------------------------------------

pygame.init()

#-----------------------------------------------------------------------Defining colours-------------------------------------------------------------------------------

white = (255,255,255)                                               
black = (0,0,0)
deepred = (153,0,0)
red = (255,0,0)                                                     
skyblue = (0,191,255)
deepblue = (0,0,255)
brown = (90,58,37)
midgreen= (92,193,17)
deepgreen = (34,177,76)
lightgreen = (51,255,51)
lightbrown = (185,122,87)
deepyellow = (204, 204, 0)
yellow = (255,255,0)
lightyellow = (255,255,51)
green = (0,255,0)
lightred = (255,51,51)
blue = (0, 0, 255)
lightblue = (0, 170, 255)
purple = (172, 16, 131)

#------------------------------------------------------------------Defining the screen dimensions---------------------------------------------------------------------- 
display_width = 800
display_height = 600

#-------------------------------------------------------------------Defining of the Game Surface-----------------------------------------------------------------------

#This sets the display that appears, assigned to the variable name 'gameScreen'
gameScreen = pygame.display.set_mode((display_width,display_height))
#This defines the name/title of the game
pygame.display.set_caption('The Driving Test')
#Creating the game Icon
icon = pygame.image.load("symbol2.png")
pygame.display.set_icon(icon)

#-----------------------------------------------------------------------------Sprites-----------------------------------------------------------------------------------

#Sprites had been made using GIMP 2 software and the internet available png's
#These png's have been saved in the same directory as the project file
#The following lines of code import the png's and assign them variable names
treeimg = pygame.image.load("tree3.png")
carimg = pygame.image.load("car.png")
bgimg = pygame.image.load("bg2.png")
lineimg = pygame.image.load("line.png")
logimg = pygame.image.load("log2.png")
gameintrobg = pygame.image.load("gameintroback3.png")
endscreenbg = pygame.image.load("endscreen2.png")
infobg = pygame.image.load("info2.png")
infobg2 = pygame.image.load("infoscreen3.png")
Q1 = pygame.image.load("Question1.png")
Q2 = pygame.image.load("Question2.png")
Q3 = pygame.image.load("Question3.png")
Q4 = pygame.image.load("Question4.png")
Q5 = pygame.image.load("Question5.png")
Q6 = pygame.image.load("Question6.png")
Q7 = pygame.image.load("Question7.png")
Q8 = pygame.image.load("Question8.png")
right = pygame.image.load("Correct.png")
wrong = pygame.image.load("Incorrect.png")
score1 = pygame.image.load("score1.png")
score2 = pygame.image.load("score2.png")
score3 = pygame.image.load("score3.png")
score4 = pygame.image.load("score4.png")
score5 = pygame.image.load("score5.png")
score6 = pygame.image.load("score6.png")
score7 = pygame.image.load("score7.png")
score8 = pygame.image.load("score8.png")
score9 = pygame.image.load("score9.png")
score10 = pygame.image.load("score10.png")
score11 = pygame.image.load("score11.png")
score12 = pygame.image.load("score12.png")
score13 = pygame.image.load("score13.png")
score14 = pygame.image.load("score14.png")
score15 = pygame.image.load("score15.png")
score16 = pygame.image.load("score16.png")
score17 = pygame.image.load("score17.png")
score18 = pygame.image.load("score18.png")
score19 = pygame.image.load("score19.png")
score20 = pygame.image.load("score20.png")
pausebg = pygame.image.load("pausescreen.png")
#pygame.display.update is appears throughout the program such that the program can update the GameScreen with the code it is dealing with
pygame.display.update()

#-----------------------------------------------------------------------Music load and play-------------------------------------------------------------------------------

pygame.mixer.music.load("bgmusic.wav")
pygame.mixer.music.play(-1)
pygame.display.update()


#--------------------------------------------------------------------Globally defined variables------------------------------------------------------------------------
#Controls the closing of functions and loops.
#global closed
closed = False
#Counters
global maincount
maincount = 0
global scorecount
scorecount = 0
#Variables that control game screen modes
gameExit = False                                                    
gameOver = False
compgameExit = False                                                    
compgameOver = False
blitzgameExit = False                                                    
blitzgameOver = False
infoScreen = False
infoscreen2 = False
#Variables that deal with question asking
global asked
asked = True
global Ans
Ans = False
hitA = False
hitB = False
hitC = False
#Variables controling text      
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
font = pygame.font.SysFont(None, 25)
#This later helps with FPS and can be manipulated such that the program can stop for a fixed amount of time
clock = pygame.time.Clock()
#This FPS value controls the frames per second of the application
FPS = 60

#----------------------------------------------------------------------Game Intro function-----------------------------------------------------------------------------

def game_intro():
    intro = True
    #This provides the background for the game introduction
    gameScreen.blit(gameintrobg, (0,0))
    #main loop of event control for the introduction
    while not closed and intro == True:                
        #Defined buttons that have assigned actions elsewhere in the program
        button("FREE", 50,400,150,50, deepgreen, green, action = "play")
        if closed:
            return
        button("INFO", 325,400,150,50, deepyellow, yellow, action = "info")
        if closed:
            return
        button("QUIT", 600,400,150,50, deepred, red, action = "quit")
        if closed:
            return
        button("COMPETITION", 50,500,350,50, blue, lightblue, action = "compplay")
        if closed:
            return
        button("BLITZ", 500,500,200,50, purple, deepblue, action = "blitzplay")
        if closed:
            return
        #Defines a quit from the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
        #Used throughout the program to update the applicatioon with different events
        pygame.display.update()

#----------------------------------------------------------------------Printing to the Screen--------------------------------------------------------------------------

#This function allows you to print text to the screen, and allows you to define a message, position and a colour
def message_to_screen(msg, colour, position):
    screen_text = font.render(msg, True, colour)
    #gameScreen.blit(screen_text, position)

#This funtion is an extention on the font definitions above in the program
#This allows us to define a small text, medium text and a large text for use later on in the program
def text_object(msg,colour, size):
    if size == "small":
        textSurface = smallfont.render(msg, True, colour)
    elif size == "medium":
        textSurface = medfont.render(msg, True, colour)
    elif size == "large":
        textSurface = largefont.render(msg, True, colour)
    return textSurface, textSurface.get_rect()

#---------------------------------------------------------------------------Buttons------------------------------------------------------------------------------------

#This function allows you to print text inside your button expressing to the user what the button does
def text_to_button(msg, colour, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurface, textRect = text_object(msg,colour,size)
    textRect.center = ((buttonx+buttonwidth/2)), buttony + (buttonheight/2)
    gameScreen.blit(textSurface, textRect)

#This is the main function for the actual button itself. within this comes the ability for the button to change colour when scrolled upon
#This also allows for the assignment of actions and the consequence of hitting the button with tha action asigned to it
def button(text, x, y, width, height, inactive_colour, active_colour, text_colour = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameScreen, active_colour, (x,y,width,height))
        global closed
        global asked
        if click[0] == 1 and action != None:
            #Defining of the actions of each button.
            if action == "quit":
                closed = True
                pygame.quit() 
                return
            if action == "info":
                infoScreen = True
                info()
                return
            if action == "next":
                infoScreen2 = True
                infoScreen = False
                info2()
                return
            if action == "play":
                intro = False
                scorecount = 0
                gameLoop()           
                return
            if action == "compplay":
                intro = False
                scorecount = 0
                compgameLoop()
                return
            if action == "blitzplay":
                intro = False
                scorecount = 0
                blitzgameLoop()
                return
            if action == "tryagain":
                scorecount = 0
                gameOver = False
                gameLoop()
                return
            if action == "comptryagain":
                scorecount = 0
                compgameOver = False
                compgameLoop()
                return
            if action == "blitztryagain":
                scorecount = 0
                compgameOver = False
                blitzgameLoop()
                return
            if action == "back":
                intro = True
                infoScreen = False
                game_intro()
                return
            if action == "menu":
                infoScreen = False
                intro = True
                gameOver = False
                game_intro()
                return
            if action == "A":
                hitA = True
                checkABC(maincount, True, False, False)
                asked = False
                return
            if action == "B":
                hitB = True
                checkABC(maincount, False, True, False)
                asked = False
                return
            if action == "C":
                hitC = True
                checkABC(maincount, False, False, True)
                asked = False
                return
            if action == "Acomp":
                hitA = True
                compcheckABC(maincount, True, False, False)
                asked = False
                return
            if action == "Bcomp":
                hitB = True
                compcheckABC(maincount, False, True, False)
                asked = False
                return
            if action == "Ccomp":
                hitC = True
                compcheckABC(maincount, False, False, True)
                asked = False
                return
            if action == "Ablitz":
                hitA = True
                blitzcheckABC(randqn, True, False, False)
                asked = False
                return
            if action == "Bblitz":
                hitB = True
                blitzcheckABC(randqn, False, True, False)
                asked = False
                return
            if action == "Cblitz":
                hitC = True
                blitzcheckABC(randqn, False, False, True)
                asked = False
                return
            
    else:
        pygame.draw.rect(gameScreen, inactive_colour, (x,y,width,height))
    text_to_button(text,black,x,y,width,height)

#--------------------------------------------------------------------------CHECK FUNCTIONS------------------------------------------------------------------------------

#Validation of answer given to questions within the 'FREE' mode of the game
#This function recieves input from the buttons
def checkABC(qnno, hitA, hitB, hitC):
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
            global scorecount
    if qnno == 1:    
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount = 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
    elif qnno == 20:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
    elif qnno == 30:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 40:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 50:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 60:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 70:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 80:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1        
    pygame.display.update()

    
#Validation of answer given to questions within the 'COMPETITION' mode of the game
#This function recieves input from the buttons
def compcheckABC(qnno, hitA, hitB, hitC):
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            global scorecount
            quit()
    if qnno == 1:    
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount = 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
    elif qnno == 5:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
    elif qnno == 10:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 15:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 20:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 25:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 30:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 35:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1        
    pygame.display.update()

#Validation of answer given to questions within the 'BLITZ' mode of the game
#This function recieves input from the buttons
def blitzcheckABC(qnno, hitA, hitB, hitC):
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
    global scorecount
    global maincount
    if maincount == 0:
        scorecount = 0
    if qnno == 1:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount = 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
    elif qnno == 2:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount = 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
    elif qnno == 3:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount = 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
            scorecount = 0
    elif qnno == 4:
        if hitA == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 5:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
        if hitC == True:
            gameScreen.blit(wrong, (0,0))
    elif qnno == 6:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 7:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1
    elif qnno == 8:
        if hitA == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitB == True:
            gameScreen.blit(wrong, (0,0))
            clock.tick(120)
        if hitC == True:
            gameScreen.blit(right, (0,0))
            clock.tick(120)
            scorecount += 1        
    pygame.display.update()

#------------------------------------------------------------------------INFORMATION SCREEN----------------------------------------------------------------------------

#This is the function that deals with the first page of the information screen
def info():
    infoScreen = True
    gameScreen.blit(infobg, (0,0))

    while infoScreen == True:
        for event in pygame.event.get():
            #defining a quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Buttons within the information screen page 2, the other leads to the menu
            button("BACK", 600,550,150,50, deepred, red, action = "back")
            if closed:
                return
            button("NEXT", 600,0,150,50, deepyellow, yellow, action = "next")
            if closed:
                return
            pygame.display.update()

#This is the second page of the information screen
def info2():
    infoScreen2 = True
    gameScreen.blit(infobg2, (-50,0))

    while infoScreen2 == True:
        for event in pygame.event.get():
            #defining a quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Contains one button that leads back to the menu
            button("BACK", 600,550,150,50, deepred, red, action = "back")
            if closed:
                return
            pygame.display.update()

#--------------------------------------------------------------------------------PAUSE SCREEN--------------------------------------------------------------------------
#This function deals with the screen that comes up when you press p in the game
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #Background screen blitted onto screen            
        gameScreen.blit(pausebg, (-100,0))
        
        pygame.display.update()
        #Waits 10 units of time before continuing
        clock.tick(10)

#------------------------------------------------------------------------------QUESTION FUNCTION-----------------------------------------------------------------------

#This is the function that deals with the question blitting for the 'Free' mode area of the game
def question():
    #Calling global variables
    global asked
    asked = True
    global scorecount
    while asked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()       
            if maincount == 1:        
                gameScreen.blit(Q1, (0,0))
            elif maincount == 20:
                gameScreen.blit(Q2, (0,0))
            elif maincount == 30:
                gameScreen.blit(Q3, (0,0))
            elif maincount == 40:
                gameScreen.blit(Q4, (0,0))
            elif maincount == 50:
                gameScreen.blit(Q5, (0,0))
            elif maincount == 60:
                gameScreen.blit(Q6, (0,0))
            elif maincount == 70:
                gameScreen.blit(Q7, (0,0))
            elif maincount == 80:
                gameScreen.blit(Q8, (0,0))
            
            
            pygame.display.update()
                
            #Buttons specific to the free mode screen
            button("A", 50,400,150,50, deepgreen, green, action = "A")
            if closed:
                return
            button("B", 325,400,150,50, deepyellow, yellow, action = "B")
            if closed:
                return
            button("C", 600,400,150,50, skyblue, deepblue, action = "C")
            if closed:
                return
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()

            pygame.display.update()
        pygame.display.update()
        clock.tick(10)
    
#This is the function that deals with the question blitting for the competition area of the game
def compquestion():
    global asked
    asked = True
    global scorecount
    while asked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Ddifference is that the maincount values that need to be considered here are different to the ones that need to be considered
            #in the free mode one or the blitz one
            if maincount == 1:        
                gameScreen.blit(Q1, (0,0))
            elif maincount == 5:
                gameScreen.blit(Q2, (0,0))
            elif maincount == 10:
                gameScreen.blit(Q3, (0,0))
            elif maincount == 15:
                gameScreen.blit(Q4, (0,0))
            elif maincount == 20:
                gameScreen.blit(Q5, (0,0))
            elif maincount == 25:
                gameScreen.blit(Q6, (0,0))
            elif maincount == 30:
                gameScreen.blit(Q7, (0,0))
            elif maincount == 35:
                gameScreen.blit(Q8, (0,0))
            
            
            pygame.display.update()
                
            #Buttons specific to the competition mode
            button("A", 50,400,150,50, deepgreen, green, action = "Acomp")
            if closed:
                return
            button("B", 325,400,150,50, deepyellow, yellow, action = "Bcomp")
            if closed:
                return
            button("C", 600,400,150,50, skyblue, deepblue, action = "Ccomp")
            if closed:
                return
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()

            pygame.display.update()
        pygame.display.update()
        clock.tick(10)
    
#This function deals with the question blitting for the blitz mode of the game, it takes one arguement: randqn
def blitzquestion(randqn):
    global asked
    asked = True
    global scorecount
    while asked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if randqn == 1:        
                gameScreen.blit(Q1, (0,0))
            elif randqn == 2:
                gameScreen.blit(Q2, (0,0))
            elif randqn == 3:
                gameScreen.blit(Q3, (0,0))
            elif randqn == 4:
                gameScreen.blit(Q4, (0,0))
            elif randqn == 5:
                gameScreen.blit(Q5, (0,0))
            elif randqn == 6:
                gameScreen.blit(Q6, (0,0))
            elif randqn == 7:
                gameScreen.blit(Q7, (0,0))
            elif randqn == 8:
                gameScreen.blit(Q8, (0,0))

            
            
            pygame.display.update()
                
            #Again the buttons are specific to this function
            button("A", 50,400,150,50, deepgreen, green, action = "Ablitz")
            if closed:
                return
            button("B", 325,400,150,50, deepyellow, yellow, action = "Bblitz")
            if closed:
                return
            button("C", 600,400,150,50, skyblue, deepblue, action = "Cblitz")
            if closed:
                return
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()

            pygame.display.update()
        pygame.display.update()
        clock.tick(10)


    
    
#--------------------------------------------------------------------------THE FREE MODE GAME LOOP-------------------------------------------------------------------------------

def gameLoop():
    #These variables will allow us to position images and move them
    #lead_x and lead_y are positioners
    #lead_x_change and lead_y_change help move the images
    lead_x = display_width/2
    lead_y = 250
    lead_x_change = 0
    lead_y_log = 800
    scorecount = 0
    #This clock helps us bring the factor of time which will help us with our FPS
    clock = pygame.time.Clock()
    #Variable created that we will use for our FPS
    FPS = 60
    #Using the imported background that was given the variable name 'bgimg', The gameScreen is set that backdrop
    #The bit function allows for things to be added to the screen. Its almost like an immediate assist to the .update function
    #A tuple with the start position is also given(0,0) being the top left of the screen.
    #The background was also made in GIMP 2 at 800x600 pixels wide
    gameScreen.blit(bgimg, (0,0))
    #Variables that allow the game to be exited and stopped are set. These boolean values allow us to easily add a 'stop' or 'game over'
    #to the game. These loops also allow the program to run for a period of time defined for how long a condition is met
    gameExit = False
    gameOver = False
    #Here is whwere the actual game begins. So while not gameExit means while it is false
    #GameExit is already set to false so the game will continue to run until a condition is met
    counter = 0
    q = False
    global maincount
    global asked
    global closed
    maincount = 0
    while not gameExit:
        #This is the event handling side of the program, getting the evennts that occur in the queue
        for event in pygame.event.get():
            #This allows for the recognition for the quit functionality in pygame. So it says is the program is prompted to quit
            #the game loop will be broken by setting gameExit to True
            if event.type == pygame.QUIT:                               
                gameExit = True
            #Teling the program that the event type will be a KEYDOWN 
            if event.type == pygame.KEYDOWN:
                #The following conditionals are for the controlls of the car. Saying if a button (LEFT, RIGHT etc) is pressed
                #The value for lead_x_change will change resulting in a change of the percieved speed or direction of the vihicle
                if event.key == pygame.K_RIGHT:
                    lead_x_change -= 5
                    maincount += 1
                    asked = False
                if event.key == pygame.K_LEFT:
                    lead_x_change += 5
                    maincount+=1
                    asked = False
                if event.key == pygame.K_UP:
                    lead_y = 250
                    maincount += 1
                if event.key == pygame.K_DOWN:
                    lead_y = 400
                    maincount += 1
                if event.key == pygame.K_p:
                    pause()
                #This is going to be the counter that leads to the asking of questions
                if maincount == 1:
                    question()
                if maincount == 20:
                    question()
                if maincount == 30:
                    question()
                if maincount == 40:
                    question()
                if maincount == 50:
                    question()
                if maincount == 60:
                    question()
                if maincount == 70:
                    question()
                if maincount == 80:
                    question()
        
                    

        # Defines boundries on the screen, such that should the pixel move beyond a certain point, it will be moved back to the
        #other side of the screen (note it is outside the keydown loop)
        #These boundries are defined for the x and y axis, the x axis is used for the animated background creating the percieved motion
        #of the car. The y sxis is used for the car staying on the road
        #Means if a boundry is crossed on the y axis, the gameover will be initiated, whereas the x axis will just itterate through
        maincounter = 0
        if lead_x <= 0:
            lead_x = display_width
        if lead_x > display_width:
            lead_x = 0
        if lead_x_change == 0:
            lead_y_change = 0
        if lead_y < 200:
            gameOver = True
        if lead_y > 500:
            gameOver = True
        #This section of the code deals with the obstacle the car has to face and itterates it through such that it appears that there are multiple obstacles.
        #I used the imported random module to randomise the positioning of the log between 2 positions
        if lead_x == display_width:
            logpos =  random.randrange(1,3,1)
            if logpos == 1:
                lead_y_log = 250
            if logpos == 2:
                lead_y_log = 400
                counter += 1
            else:
                counter += 1
            if counter == 10:
                counter = 0

        #This is the collision detection part of the code. This ensures that the log sprite does not lie anywhere within the car sprite
        global closed
        if lead_x > 100 and lead_x < 498 and lead_y == lead_y_log:
            gameOver = True
            endscreen()
            closed = True
            return
        
        #This allows the car to chnage speed, so every time the key is pressed the speed of the car or the speed of the percieved turn chnages
        #by the defined factor
        lead_x += lead_x_change
        #This blits the background to the screen
        gameScreen.blit(bgimg, (0,0))                                           
        #The following are all the different objects on the screen being blitted onto the screen. These are done so using positions
        #within the tuple. By using variables such as lead_x and lead_y, we can cause motion on the screen
        gameScreen.blit(treeimg, (lead_x, -2))
        gameScreen.blit(treeimg, (lead_x + 100, -2))
        gameScreen.blit(treeimg, (lead_x + 200, -2))
        gameScreen.blit(treeimg, (lead_x + 300, -2))
        gameScreen.blit(treeimg, (lead_x + 400, -2))
        gameScreen.blit(treeimg, (lead_x + 500, -2))
        gameScreen.blit(treeimg, (lead_x + 600, -2))
        gameScreen.blit(treeimg, (lead_x + 700, -2))
        gameScreen.blit(treeimg, (lead_x + 800, -2))
        gameScreen.blit(treeimg, (lead_x - 100, -2))
        gameScreen.blit(treeimg, (lead_x - 200, -2))
        gameScreen.blit(treeimg, (lead_x - 300, -2))
        gameScreen.blit(treeimg, (lead_x - 400, -2))
        gameScreen.blit(treeimg, (lead_x - 500, -2))
        gameScreen.blit(treeimg, (lead_x - 600, -2))
        gameScreen.blit(treeimg, (lead_x - 700, -2))
        gameScreen.blit(treeimg, (lead_x - 800, -2))
        gameScreen.blit(lineimg, (lead_x, 400))
        gameScreen.blit(lineimg, (lead_x + 400, 400))
        gameScreen.blit(lineimg, (lead_x - 400, 400))
        gameScreen.blit(lineimg, (lead_x - 800, 400))
        gameScreen.blit(logimg, (lead_x, lead_y_log))
        gameScreen.blit(carimg, (100, lead_y))
        pygame.display.update()
        #Using the predifined FPS value, and the clock function, we are able to 
        clock.tick(FPS)
        if gameOver == True:
            endscreen()
            closed = True
            return


#-------------------------------------------------------------------------COMPETITION GAME LOOP------------------------------------------------------------------------
        
def compgameLoop():
    #This game loop deals with the competition mode of the game
    #The structures used in this game loop are not too disimilar to the ones used in the free mode game loop, as a result, refer to that loop
    #for comments. All unique features in this loop will however be commented.
    lead_x = display_width/2
    lead_y = 250
    lead_x_change = 0
    lead_y_log = 800
    scorecount = 0
    clock = pygame.time.Clock()
    FPS = 60
    gameScreen.blit(bgimg, (0,0))
    #new globally controlled variables
    compgameExit = False
    compgameOver = False
    #exclusive to this loop and the blitz loop, deals with horizontal control
    keyhit = 0
    counter = 0
    q = False
    global asked
    global maincount
    global closed
    maincount = 0
    while not compgameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                compgameExit = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if keyhit < 1 or keyhit == 1:
                        lead_x_change -= 5
                        maincount += 1
                        keyhit += 1
                    else:
                        lead_x_change += 0
                    asked = False
                if event.key == pygame.K_LEFT:
                    lead_x_change += 0
                    asked = False
                if event.key == pygame.K_UP:
                    lead_y = 250
                    maincount += 1
                if event.key == pygame.K_DOWN:
                    lead_y = 400
                    maincount += 1
                if event.key == pygame.K_p:
                    pause()
                if maincount == 1:
                    compquestion()
                if maincount == 5:
                    compquestion()
                if maincount == 10:
                    compquestion()
                if maincount == 15:
                    compquestion()
                if maincount == 20:
                    compquestion()
                if maincount == 25:
                    compquestion()
                if maincount == 30:
                    compquestion()
                if maincount == 35:
                    compquestion()
        
                    

        # Defines boundries on the screen, just like the previous game Loop, only this time, every iteration, the lead_x_change value increments
        maincounter = 0
        if lead_x <= 0:
            lead_x = display_width
            lead_x_change -= 2
        if lead_x > display_width:
            lead_x = 0
        if lead_x_change == 0:
            lead_y_change = 0
        if lead_x == display_width:
            logpos =  random.randrange(1,3,1)
            if logpos == 1:
                lead_y_log = 250
            if logpos == 2:
                lead_y_log = 400
                counter += 1
            else:
                counter += 1
            if counter == 10:
                counter = 0

        global closed
        if lead_x > 100 and lead_x < 498 and lead_y == lead_y_log:
            compgameOver = True
            compendscreen()
            closed = True
            return
        
        lead_x += lead_x_change
        gameScreen.blit(bgimg, (0,0))                                           
        gameScreen.blit(treeimg, (lead_x, -2))
        gameScreen.blit(treeimg, (lead_x + 100, -2))
        gameScreen.blit(treeimg, (lead_x + 200, -2))
        gameScreen.blit(treeimg, (lead_x + 300, -2))
        gameScreen.blit(treeimg, (lead_x + 400, -2))
        gameScreen.blit(treeimg, (lead_x + 500, -2))
        gameScreen.blit(treeimg, (lead_x + 600, -2))
        gameScreen.blit(treeimg, (lead_x + 700, -2))
        gameScreen.blit(treeimg, (lead_x + 800, -2))
        gameScreen.blit(treeimg, (lead_x - 100, -2))
        gameScreen.blit(treeimg, (lead_x - 200, -2))
        gameScreen.blit(treeimg, (lead_x - 300, -2))
        gameScreen.blit(treeimg, (lead_x - 400, -2))
        gameScreen.blit(treeimg, (lead_x - 500, -2))
        gameScreen.blit(treeimg, (lead_x - 600, -2))
        gameScreen.blit(treeimg, (lead_x - 700, -2))
        gameScreen.blit(treeimg, (lead_x - 800, -2))
        gameScreen.blit(lineimg, (lead_x, 400))
        gameScreen.blit(lineimg, (lead_x + 400, 400))
        gameScreen.blit(lineimg, (lead_x - 400, 400))
        gameScreen.blit(lineimg, (lead_x - 800, 400))
        gameScreen.blit(logimg, (lead_x, lead_y_log))
        gameScreen.blit(carimg, (100, lead_y))
        pygame.display.update()
        clock.tick(FPS)
        if compgameOver == True:
            compendscreen()
            closed = True
            return

#-----------------------------------------------------------------------BLITZ GAME LOOP--------------------------------------------------------------------------------

def blitzgameLoop():
    #This is the game loop that controls the blitz area of the game. This again is not too disimilar to the above 2 game loops
    #Any individual features will be commented on
    lead_x = display_width/2
    lead_y = 250
    lead_x_change = 0
    lead_y_log = 800
    scorecount = 0
    clock = pygame.time.Clock()
    FPS = 60
    gameScreen.blit(bgimg, (0,0))
    blitzgameExit = False
    blitzgameOver = False
    counter = 0
    keyhit = 0
    q = False
    global asked
    global randqn
    global maincount
    global closed
    maincount = 0
    while not blitzgameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                blitzgameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if keyhit < 1 or keyhit == 1:
                        lead_x_change -= 5
                        #global maincount
                        maincount += 1
                        keyhit += 1
                    else:
                        lead_x_change += 0
                    #global asked
                    asked = False
                if event.key == pygame.K_LEFT:
                    lead_x_change += 0
                if event.key == pygame.K_UP:
                    lead_y = 250
                    #global maincount
                    maincount += 1
                if event.key == pygame.K_DOWN:
                    lead_y = 400
                    #global maincount
                    maincount += 1
                if event.key == pygame.K_p:
                    pause()

        #From here on to the screen blits, the code changes. We are now no longer fully dependant on the maincount value for our questions
        #Instead the maincount just assists us in out randomisation of the questions.
        #The variable randqn is then fed through the blitz specific question function as an expected arguement to the function
        #This block deals with the first question
        if maincount == 1:
            #global randqn
            randqn = random.randrange(1,3,1)
            if randqn == 1:
                maincount = 2
                blitzquestion(1)
            if randqn == 2:
                maincount = 2
                blitzquestion(2)
            if randqn == 3:
                maincount = 2
                blitzquestion(3)

        #This deals with the randomisation of the rest of the questions.
        if maincount == 5:
            #global randqn
            randqn = random.randrange(4,8,1)
            if randqn == 4:
                maincount = 2
                blitzquestion(4)
            if randqn == 5:
                maincount = 2
                blitzquestion(5)
            if randqn == 6:
                maincount = 2
                blitzquestion(6)
            if randqn == 7:
                maincount = 2
                blitzquestion(7)
            if randqn == 8:
                maincount = 2
                blitzquestion(8)
                    

        maincounter = 0
        if lead_x <= 0:
            lead_x = display_width
            lead_x_change -= 1
        if lead_x > display_width:
            lead_x = 0
        if lead_x_change == 0:
            lead_y_change = 0
        if lead_y < 200:
            gameOver = True
        if lead_y > 500:
            gameOver = True
        if lead_x == display_width:
            logpos =  random.randrange(1,3,1)
            if logpos == 1:
                lead_y_log = 250
            if logpos == 2:
                lead_y_log = 400
                counter += 1
            else:
                counter += 1
            if counter == 10:
                counter = 0

        if lead_x > 100 and lead_x < 498 and lead_y == lead_y_log:
            blitzgameOver = True
            blitzendscreen()
            #global closed
            closed = True
            return
        
        lead_x += lead_x_change
        gameScreen.blit(bgimg, (0,0))                                           
        gameScreen.blit(treeimg, (lead_x, -2))
        gameScreen.blit(treeimg, (lead_x + 100, -2))
        gameScreen.blit(treeimg, (lead_x + 200, -2))
        gameScreen.blit(treeimg, (lead_x + 300, -2))
        gameScreen.blit(treeimg, (lead_x + 400, -2))
        gameScreen.blit(treeimg, (lead_x + 500, -2))
        gameScreen.blit(treeimg, (lead_x + 600, -2))
        gameScreen.blit(treeimg, (lead_x + 700, -2))
        gameScreen.blit(treeimg, (lead_x + 800, -2))
        gameScreen.blit(treeimg, (lead_x - 100, -2))
        gameScreen.blit(treeimg, (lead_x - 200, -2))
        gameScreen.blit(treeimg, (lead_x - 300, -2))
        gameScreen.blit(treeimg, (lead_x - 400, -2))
        gameScreen.blit(treeimg, (lead_x - 500, -2))
        gameScreen.blit(treeimg, (lead_x - 600, -2))
        gameScreen.blit(treeimg, (lead_x - 700, -2))
        gameScreen.blit(treeimg, (lead_x - 800, -2))
        gameScreen.blit(lineimg, (lead_x, 400))
        gameScreen.blit(lineimg, (lead_x + 400, 400))
        gameScreen.blit(lineimg, (lead_x - 400, 400))
        gameScreen.blit(lineimg, (lead_x - 800, 400))
        gameScreen.blit(logimg, (lead_x, lead_y_log))
        gameScreen.blit(carimg, (100, lead_y))
        pygame.display.update()
        clock.tick(FPS)
        if blitzgameOver == True:
            blitzendscreen()
            closed = True
            return

        
#------------------------------------------------------------------------THE END SCREEN LOOPS---------------------------------------------------------------------------

#This is the endscreen associated to the main game loop for free mode.
def endscreen():
    gameOver = True
    while gameOver == True:
        gameScreen.blit(endscreenbg, (0,0))

        button("TRY AGAIN", 50,400,150,50, deepgreen, green, action = "tryagain")
        if closed:
            return
        button("MAIN MENU", 325,400,150,50, deepblue, skyblue, action = "menu")
        if closed:
            return
        button("QUIT", 600,400,150,50, deepred, red, action = "quit")
        if closed:
            return
        #Scores are blitted depending o how many questions the user got right
        if scorecount == 1:
            gameScreen.blit(score1, (220,200))
        if scorecount == 2:
            gameScreen.blit(score2, (220,200))
        if scorecount == 3:
            gameScreen.blit(score3, (220,200))
        if scorecount == 4:
            gameScreen.blit(score4, (220,200))
        if scorecount == 5:
            gameScreen.blit(score5, (220,200))
        if scorecount == 6:
            gameScreen.blit(score6, (220,200))
        if scorecount == 7:
            gameScreen.blit(score7, (220,200))
        if scorecount == 8:
            gameScreen.blit(score8, (220,200))
        if scorecount == 9:
            gameScreen.blit(score9, (220,200))
        if scorecount == 10:
            gameScreen.blit(score10, (220,200))
        if scorecount == 11:
            gameScreen.blit(score11, (220,200))
        if scorecount == 12:
            gameScreen.blit(score12, (220,200))
        if scorecount == 13:
            gameScreen.blit(score13, (220,200))
        if scorecount == 14:
            gameScreen.blit(score14, (220,200))
        if scorecount == 15:
            gameScreen.blit(score15, (220,200))
        if scorecount == 16:
            gameScreen.blit(score16, (220,200))
        if scorecount == 17:
            gameScreen.blit(score17, (220,200))
        if scorecount == 18:
            gameScreen.blit(score18, (220,200))
        if scorecount == 19:
            gameScreen.blit(score19, (220,200))
        if scorecount == 20:
            gameScreen.blit(score20, (220,200))


        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#This is the endscreen associated with the competition mode on the game
def compendscreen():
    compgameOver = True
    while compgameOver == True:
        gameScreen.blit(endscreenbg, (0,0))

        button("TRY AGAIN", 50,400,150,50, deepgreen, green, action = "comptryagain")
        if closed:
            return
        button("MAIN MENU", 325,400,150,50, deepblue, skyblue, action = "menu")
        if closed:
            return
        button("QUIT", 600,400,150,50, deepred, red, action = "quit")
        if closed:
            return
        if scorecount == 1:
            gameScreen.blit(score1, (220,200))
        if scorecount == 2:
            gameScreen.blit(score2, (220,200))
        if scorecount == 3:
            gameScreen.blit(score3, (220,200))
        if scorecount == 4:
            gameScreen.blit(score4, (220,200))
        if scorecount == 5:
            gameScreen.blit(score5, (220,200))
        if scorecount == 6:
            gameScreen.blit(score6, (220,200))
        if scorecount == 7:
            gameScreen.blit(score7, (220,200))
        if scorecount == 8:
            gameScreen.blit(score8, (220,200))
        if scorecount == 9:
            gameScreen.blit(score9, (220,200))
        if scorecount == 10:
            gameScreen.blit(score10, (220,200))
        if scorecount == 11:
            gameScreen.blit(score11, (220,200))
        if scorecount == 12:
            gameScreen.blit(score12, (220,200))
        if scorecount == 13:
            gameScreen.blit(score13, (220,200))
        if scorecount == 14:
            gameScreen.blit(score14, (220,200))
        if scorecount == 15:
            gameScreen.blit(score15, (220,200))
        if scorecount == 16:
            gameScreen.blit(score16, (220,200))
        if scorecount == 17:
            gameScreen.blit(score17, (220,200))
        if scorecount == 18:
            gameScreen.blit(score18, (220,200))
        if scorecount == 19:
            gameScreen.blit(score19, (220,200))
        if scorecount == 20:
            gameScreen.blit(score20, (220,200))


        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#This is the endscreen associated with the blitz mode on the game
def blitzendscreen():
    compgameOver = True
    while compgameOver == True:
        gameScreen.blit(endscreenbg, (0,0))

        button("TRY AGAIN", 50,400,150,50, deepgreen, green, action = "blitztryagain")
        if closed:
            return
        button("MAIN MENU", 325,400,150,50, deepblue, skyblue, action = "menu")
        if closed:
            return
        button("QUIT", 600,400,150,50, deepred, red, action = "quit")
        if closed:
            return
        if scorecount == 1:
            gameScreen.blit(score1, (220,200))
        if scorecount == 2:
            gameScreen.blit(score2, (220,200))
        if scorecount == 3:
            gameScreen.blit(score3, (220,200))
        if scorecount == 4:
            gameScreen.blit(score4, (220,200))
        if scorecount == 5:
            gameScreen.blit(score5, (220,200))
        if scorecount == 6:
            gameScreen.blit(score6, (220,200))
        if scorecount == 7:
            gameScreen.blit(score7, (220,200))
        if scorecount == 8:
            gameScreen.blit(score8, (220,200))
        if scorecount == 9:
            gameScreen.blit(score9, (220,200))
        if scorecount == 10:
            gameScreen.blit(score10, (220,200))
        if scorecount == 11:
            gameScreen.blit(score11, (220,200))
        if scorecount == 12:
            gameScreen.blit(score12, (220,200))
        if scorecount == 13:
            gameScreen.blit(score13, (220,200))
        if scorecount == 14:
            gameScreen.blit(score14, (220,200))
        if scorecount == 15:
            gameScreen.blit(score15, (220,200))
        if scorecount == 16:
            gameScreen.blit(score16, (220,200))
        if scorecount == 17:
            gameScreen.blit(score17, (220,200))
        if scorecount == 18:
            gameScreen.blit(score18, (220,200))
        if scorecount == 19:
            gameScreen.blit(score19, (220,200))
        if scorecount == 20:
            gameScreen.blit(score20, (220,200))


        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        


        

#------------------------------------------------------------------------Calling the functions--------------------------------------------------------------------------

#Here the funtions are executed in order such that the game can flow properly
game_intro()
###--------------------------------------------------------------------------END OF PROGRAM--------------------------------------------------------------------------------

