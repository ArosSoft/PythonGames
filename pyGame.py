import pygame
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A big Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font(r'c:\Windows\Fonts\times.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (400, 200)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('Вы разбились')


def game_loop():
    x = 200
    y = 200
    dx = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -2
                elif event.key == pygame.K_RIGHT:
                    dx = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0

                    # print(event)
        x += dx

        if x < 0 or x > 800: crash()

        gameDisplay.fill(white)
        car(x, y)

        pygame.display.update()

        clock.tick(60)


game_loop()
pygame.quit()
quit()
