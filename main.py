import pygame
import random
import time

# Define colors and screen size
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 170)
black = (0, 0, 0)
white = (255, 255, 255)
white_2 = (230, 230, 230)

dark_red = (150, 0, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

size = width, height = 1000, 700
true = True
# initialize pygame and create window
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 320
pygame.display.set_caption("Atari Tennis")

# Definitions

font = 14

cx, cy, cw, ch = 980, 350, 10, 100
cxspeed, cyspeed = 0, 0

px, py, pw, ph = 10, 350, 10, 100

pxspeed, pyspeed = 0, 0

bx, by = 500, 350
bxspeed, byspeed = 2, 1

color = white

center = (500, 350)

Ppoint = 0
Cpoint = 0
spx = 0.8
spxd = 0.0

r = 10

score = pygame.font.SysFont('segoeuisymbol', 50)
player_racket = pygame.draw.rect(screen, color, [px, py, pw, ph])
CPU_racket = pygame.draw.rect(screen, color, [cx, cy, cw, ch])


# Sound
def victory():
    Victory = ("Victory.mp3")
    pygame.mixer.music.load(Victory)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def title():
    Title = ("Megaman 3.mp3")
    pygame.mixer.music.load(Title)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


##def song_two():
##    song_two = random.choice(["Base 2.mp3","Mario Galaxy.mp3","Title.mp3"])
##    pygame.mixer.music.load(song_two)
##    pygame.mixer.music.set_volume(0.5)
##    pygame.mixer.music.play(-1)

def song_one():
    song_one = random.choice(
        ["Mario Galaxy.mp3", "Title.mp3", "Megaman 2.mp3", "Hangar.mp3", "Gaur Plains.mp3", "Final Battle.mp3"])
    pygame.mixer.music.load(song_one)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(message, x, y, w, h, inactive_c, active_c, action=None):
    global spx, spxd

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    spx = 0.8
    spxd = 0.0

    if message == "Hard":
        spx = 1.4

    if message == "":
        spx = 2.1
        speed = 400

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_c, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, inactive_c, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def game_intro():
    title()
    global Ppoint, Cpoint, bx, by
    bx, by = 500, 350

    Ppoint, Cpoint = 0, 0

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(" Atari Tennis", largeText)
        TextRect.center = ((width / 2), (height / 2))
        screen.blit(TextSurf, TextRect)

        button("Easy", 150, 550, 100, 50, blue, bright_blue, game_loop)
        button("Hard", 750, 550, 100, 50, red, bright_red, game_loop)
        button("", 500, 600, 20, 10, dark_red, bright_red, game_loop)

        pygame.display.update()
        clock.tick(20)


def game_loop():
    global cx, cy, cw, ch, cxspeed, cyspeed, px, py, pw, ph, pxspeed, \
        pyspeed, bx, by, bxspeed, byspeed, color, player_racket, \
        clock, CPU_racket, screen, Ppoint, Cpoint, speed, spx, spxd

    song_one()

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_intro()

            # keydown event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pyspeed = -2
                if event.key == pygame.K_a:
                    pyspeed = -10
                if event.key == pygame.K_s:
                    pyspeed = 2
                if event.key == pygame.K_d:
                    pyspeed = 10

            # keyup event
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pyspeed = 0
                if event.key == pygame.K_a:
                    pyspeed = 0
                if event.key == pygame.K_s:
                    pyspeed = 0
                if event.key == pygame.K_d:
                    pyspeed = 0

            # CPU

            # key up event

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cyspeed = -2
                if event.key == pygame.K_LEFT:
                    cyspeed = -10
                if event.key == pygame.K_DOWN:
                    cyspeed = 2
                if event.key == pygame.K_RIGHT:
                    cyspeed = 10

            # keyup event
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    cyspeed = 0
                if event.key == pygame.K_LEFT:
                    cyspeed = 0
                if event.key == pygame.K_DOWN:
                    cyspeed = 0
                if event.key == pygame.K_RIGHT:
                    cyspeed = 0

        # cannot pass the boundaries
        if py > height - 100:
            py = 600

        if py < 0:
            py = 0

        if cy > height - 100:
            cy = 600

        if cy < 0:
            cy = 0

        # To move
        py = py + pyspeed

        cy = cy + cyspeed

        # BALL

        ball = pygame.Rect(bx - r, by - r, 2 * r, 2 * r)

        # touches rackets
        if ball.colliderect(CPU_racket):
            bxspeed = -bxspeed
            spxd += 0.05

        if ball.colliderect(player_racket):
            bxspeed = -bxspeed
            spxd += 0.05

        # bounces if touches bottom or top
        if ball.top < 0 or ball.bottom > height:
            byspeed = -byspeed

        # Increase velocity of ball
        bx = bx + bxspeed * (spx + spxd)
        by = by + byspeed

        # Ball passes player's racket
        if ball.left < 0:
            bx = px + 20  # serve ball where player is
            by = py + 50  # serve ball where player is
            bxspeed = -bxspeed
            spxd = 0.0
            Cpoint += 1
        # Ball passes CPU's racket
        if ball.right > 1000:
            bx = cx - 10  # serve ball where CPU is
            by = cy + 50  # serve ball where CPU is
            bxspeed = -bxspeed
            spxd = 0.0
            Ppoint += 1

        # draw section

        screen.fill(black)

        player_racket = pygame.draw.rect(screen, color, [px, py, pw, ph])

        CPU_racket = pygame.draw.rect(screen, color, [cx, cy, cw, ch])

        pygame.draw.circle(screen, white, ball.center, r)

        pygame.draw.rect(screen, white_2, [500, 0, 5, 700], 5)

        scores = score.render(str(Ppoint), 3, white)
        scores2 = score.render(str(Cpoint), 3, white)

        # Display message fo winner

        if Ppoint == 7:
            victory()
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Player 1 Wins", largeText, white)
            TextRect.center = ((width / 2), (height / 2))
            screen.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(6)
            game_intro()

        elif Cpoint == 7:
            victory()
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Player 2 Wins", largeText, white)
            TextRect.center = ((width / 2), (height / 2))
            screen.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(6)
            game_intro()

        # put scores in screen
        screen.blit(scores, (400, 60))
        screen.blit(scores2, (570, 60))

        ##        if Ppoint == 6 or Cpoint == 6:
        ##            song_two()
        ##

        pygame.display.update()

        clock.tick(speed)


pygame.display.flip()

game_intro()

game_loop()

pygame.quit()
