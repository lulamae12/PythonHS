import math, pygame, sys
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)

def getdiagonal():
    diagonal = input("please enter the diagonal:")
    #using 30 60 90 triangles
    legA = int(diagonal) * .5;#side 'a' of triangle is found by dividing diagnol by 2. this is x in the 30 60 90 equation
    legB = int(diagonal) * 0.866025#side 'b' of triange is x times square root of 3
    print(str(legA))
    print(str(legB))
    legAstr = str(legA)
    legBstr = str(legB)
    main(legAstr, legBstr, diagonal)
def main(legA, legB, diagonal):
    screen = pygame.display.set_mode((400,400))
    pygame.font.init()#init font
    ComicSans = pygame.font.SysFont('Comic Sans MS', 20)#set fons to comic with a size of 20
    screen = pygame.display.set_mode((400,400))
    diagonalLen = ComicSans.render(diagonal, False, GREEN) #set font, text and color
    legA = ComicSans.render(legA, False, GREEN) #set font, text and color
    legB = ComicSans.render(legB, False, GREEN) #set font, text and color
    pygame.display.set_caption("diagonal Length Finder")
    pygame.display.flip()
    gameRunning = True
    pygame.draw.rect(screen, BLUE, (150, 150, 100, 50), 0)
    pygame.draw.lines(screen, BLACK, False, [(250,200), (150,150)], 1)
    screen.blit(diagonalLen,(200,150))#update text and set pos
    screen.blit(legA,(110,160))
    screen.blit(legB,(150,200))
    pygame.display.flip()

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                gameRunning == False


getdiagonal()
