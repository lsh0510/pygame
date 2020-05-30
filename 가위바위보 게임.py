import pygame
import random


weight,height=690,480
screen=pygame.display.set_mode((weight,height))
pygame.display.set_caption("가위바위보게임")

WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

start_screen=pygame.image.load("image/screen.PNG")
start_button=pygame.image.load("image/start.PNG")
bot=pygame.image.load("image/rsp/bot.PNG")

paper=pygame.image.load("image/rsp/보.PNG")
rock=pygame.image.load("image/rsp/바위.PNG")
scissor=pygame.image.load("image/rsp/가위.PNG")

StartScreen = True
MainScreen = False

class button():
   
   def __init__(self,x,y,wid,hei):
      self.x = x
      self.y = y
      self.wid = wid
      self.hei = hei
      
   def isover(self,pos):
      if pos[0]>self.x and pos [0]<self.wid:
         if pos[1]>self.y and pos[1]<self.hei:
            return True

playButton=button(100,400,200,460)
rockbutton=button(200,250,400,450)
scissorbutton=button(0,250,200,450)
paperbutton=button(400,250,600,450)

while True:
   botscreen=random.choice([rock,scissor,paper])
   if StartScreen == True:
      screen.fill(WHITE)
      screen.blit(bot,(0,100))
      screen.blit(scissor,(0,250))
      screen.blit(rock,(200,250))
      screen.blit(paper,(400,250))
   
      
      
  
   for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
      
     
      if event.type == pygame.MOUSEBUTTONDOWN:
         if rockbutton.isover(pos):
            StartScreen = False
            MainScreen = True
            if MainScreen == True:
               screen.blit(botscreen,(0,0))
           
         elif scissorbutton.isover(pos):
            StartScreen = False
            MainScreen = True
            if MainScreen == True:
               screen.blit(botscreen,(0,0))
         elif paperbutton.isover(pos):
            StartScreen = False
            MainScreen = True
            if MainScreen == True:
               screen.blit(botscreen,(0,0))
      if event.type == pygame.QUIT:
         pygame.quit()
         exit(0)  
   pygame.display.flip()
pygame.init()
