import sys, pygame
pygame.init()

size = width, height = 400, 400
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)


ball = pygame.image.load("greenball.png")
ball = pygame.transform.scale(ball, (25, 25))
ballrect = ball.get_rect()
ball2 = pygame.image.load("greenball.png")
ball2 = pygame.transform.scale(ball2, (208, 25))
ball2rect = ball.get_rect()
x = 1
while True:

    mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    ball2rect = ball2rect.move(speed)
    if ball2rect.left < 0 or ball2rect.right > width:
        speed[0] = -speed[0]
    if ball2rect.top < 0 or ball2rect.bottom > height:
        speed[1] = -speed[1]
    while x == 1 and mouse1:
        screen.blit(ball2, ball2rect)
        pygame.display.flip()
        x = 0
    if x == 0 and mouse1 != True:
        x = 1

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
