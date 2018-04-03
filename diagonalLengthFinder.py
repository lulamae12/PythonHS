import math, pygame, sys

BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)

def main():
    pygame.font.init()#init font
    ComicSans = pygame.font.SysFont('Comic Sans MS', 20)#set fons to comic with a size of 20
    screen = pygame.display.set_mode((400,400))
    instructionsText = ComicSans.render('Please enter the diagonal Length', False, GREEN) #set font, text and color
    screen.blit(instructionsText,(10,10))#update text and set pos
    pygame.display.set_caption("diagonal Length Finder")
    pygame.display.flip()
    gameRunning = True

    pygame.draw.rect(screen, BLUE, (150, 150, 100, 50), 0)
    pygame.draw.lines(screen, BLACK, False, [(250,200), (150,150)], 1)
    pygame.display.flip()
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                gameRunning == False
main()
#def getdiagonals(diagonal):
