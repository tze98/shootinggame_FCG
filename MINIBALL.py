import pygame
from pygame.locals import *
from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import*
import random
import math

# CREATE WHITE BALL
class Ball(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.radius=2

    def make_ball(self):
        self.x = random.randrange(-37, 0)
        self.y = random.randrange(-17, 17)
        self.change_x = random.uniform(-0.2, 0.2)
        if self.change_x == 0:
            self.change_y = random.uniform(0, 0.2)
        else:
            self.change_y = random.uniform(-0.2, 0.2)

    def draw(self):
        self.move()
        glColor3f(1, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(self.x,self.y, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex3f(x + self.x, y + self.y, 0)
        glEnd()

    def move(self):
        self.x+=self.change_x
        self.y+=self.change_y
        if self.y < -17.5 or self.y > 17.5:
            self.change_y *=-1
        if self.x < -37.5 or self.x > 37.5:
            self.change_x *=-1

# CREATE RED BALL
class RedBall(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.radius=2

    def make_ball(self):
        self.x = random.randrange(-37, 0)
        self.y = random.randrange(-17, 17)
        self.change_x = random.uniform(-0.2, 0.2)
        if self.change_x == 0:
            self.change_y = random.uniform(0, 0.2)
        else:
            self.change_y = random.uniform(-0.2, 0.2)

    def draw(self):
        self.move()
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(self.x,self.y, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex3f(x + self.x, y + self.y, 0)
        glEnd()

    def move(self):
        self.x+=self.change_x
        self.y+=self.change_y
        if self.y < -17.5 or self.y > 17.5:
            self.change_y *=-1
        if self.x < -37.5 or self.x > 37.5:
            self.change_x *=-1

# CREATE PURPLE BALL FOR PLAYER
class PurpleBall(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=0.3
        self.change_x=0
        self.change_y=0
        self.shot=False
        self.ans=0
        self.radius = 1

    def draw(self):
        self.move()
        glColor3f(0.5, 0, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(self.x, self.y, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex3f(x + self.x, y + self.y, 0)
        glEnd()

    def move(self):
        if self.shot:
            self.y+=self.change_y
            if self.y>19:
                self.shot=False
                self.change_y=0
                self.y=-20
        self.x+=self.change_x
        if self.x>37.5 or self.x<-37.5:
            self.change_x=0

# MAIN PAGE
def select(music):
    sel=True
    mode=1
    while sel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        glColor3f(0.5, 0, 1)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-35, 15, 0.0)
        glScalef(8 / 152.38, 10 / 152.38, 0.1 / 152.38)
        title = " SHOOTING GAME "
        for i in range(len(title)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(title[i]))
        glPopMatrix()

        # EASY MODE
        glBegin(GL_QUADS)
        glColor3f(0.6, 0.6, 1)
        glVertex3f(-20, 10, 0)
        glVertex3f(19, 10, 0)
        glVertex3f(19, 5, 0)
        glVertex3f(-20, 5, 0)
        # NORMAL MODE
        glColor3f(0.8, 0.6, 1)
        glVertex3f(-20, 0, 0)
        glVertex3f(19, 0, 0)
        glVertex3f(19, -5, 0)
        glVertex3f(-20, -5, 0)
        # HARD MODE
        glColor3f(1, 0.6, 0.8)
        glVertex3f(-20, -10, 0)
        glVertex3f(19, -10, 0)
        glVertex3f(19, -15, 0)
        glVertex3f(-20, -15, 0)
        glEnd()

        glColor3f(0, 0, 0)
        glLineWidth(2)
        glPushMatrix()
        glTranslatef(-8, 6.2, 0.0)
        glScalef(2/ 152.38, 4 / 152.38, 0.1 / 152.38)
        title_1 = " EASY MODE "
        for i in range(len(title_1)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_1[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-9, -4, 0.0)
        glScalef(2/ 152.38, 4/ 152.38, 0.1 / 152.38)
        title_2 = " NORMAL MODE "
        for i in range(len(title_2)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_2[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-8, -13.9, 0.0)
        glScalef(2 / 152.38, 4 / 152.38, 0.1 / 152.38)
        title_3 = " HARD MODE"
        for i in range(len(title_3)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_3[i]))
        glPopMatrix()

        # CLICK TO CHOOSE GAME MODE
        mouse_1 = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()

        glColor3f(1, 1, 1)
        # EASY MODE
        if mode == 1:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-21, 11, 0)
            glVertex3f(20, 11, 0)
            glVertex3f(20, 4, 0)
            glVertex3f(-21, 4, 0)
            glEnd()
        # NORMAL MODE
        elif mode == 2:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-21, 1, 0)
            glVertex3f(20, 1, 0)
            glVertex3f(20, -6, 0)
            glVertex3f(-21, -6, 0)
            glEnd()
        # HARD MODE
        elif mode == 3:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-21, -9, 0)
            glVertex3f(20, -9, 0)
            glVertex3f(20, -16, 0)
            glVertex3f(-21, -16, 0)
            glEnd()

        # EASY MODE
        if 600 > mouse_1[0] > 200 and 250 > mouse_1[1] > 200:
            if click_1[0] == 1:
                mode=1
        # NORMAL MODE
        elif 600 > mouse_1[0] > 200 and 350 > mouse_1[1] > 300:
            if click_1[0] == 1:
                mode=2
        # HARD MODE
        elif 600 > mouse_1[0] > 200 and 450 > mouse_1[1] > 400:
            if click_1[0] == 1:
                mode=3

        # PLAY
        if 755 > mouse_1[0] > 647 and 550 > mouse_1[1] > 500:
            glColor3f(0.5, 0, 1)
            if click_1[0]==1:
                sel=False
        else:
            glColor3f(0.5, 0.5, 0.5)
        # PLAY BUTTON
        glBegin(GL_TRIANGLES)
        glVertex3f(25, -18, 0)
        glVertex3f(36, -23, 0)
        glVertex3f(25, -28, 0)
        glEnd()

        # CLICK TO SEE INFORMATION
        mouse_2 = pygame.mouse.get_pos()
        click_2 = pygame.mouse.get_pressed()

        if 60 > mouse_2[0] > 30 and 550 > mouse_2[1] > 500:
            glColor3f(0, 0, 1)
            if click_2[0] == 1:
                help(music)
        else:
            glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-35, -25, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 3 * math.cos(theta)
            y = 3 * math.sin(theta)
            glVertex3f(-35 + x, -25 + y, 0)
        glEnd()

        glColor3f(0, 0, 0)
        glLineWidth(4)
        glPushMatrix()
        glTranslatef(-35.8, -26.5, 0)
        glScalef(3 / 152.38, 4 / 152.38, 0.1 / 152.38)
        hlp = "?"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(hlp[i]))
        glPopMatrix()

        pygame.display.flip()
    return mode

def game(style,music,hitRed,hitWhite,win,lose):
    if style==1:
        num_white=2
        num_red=1
        stage="EASY"
    elif style==2:
        num_white=4
        num_red=1
        stage="NORMAL"
    elif style==3:
        num_white=6
        num_red=1
        stage="HARD"

    chanceBall = 5
    white_list = []
    red_list = []
    current_ball = num_white

    # WHITE BALL
    for ball in range(num_white):
        ball = Ball()
        white_list.append(ball)
        ball.make_ball()

    # RED BALL
    for ball in range(num_red):
        ball = RedBall()
        red_list.append(ball)
        ball.make_ball()

    # PLAYER
    me = PurpleBall(3, -20)

    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # SPACE BAR TO SHOOT
                if event.key == pygame.K_SPACE:
                    me.change_y = me.speed
                    me.shot = True
                # LEFT ARROW TO LEFT
                elif event.key == pygame.K_LEFT:
                    if me.x > -35:
                        me.change_x -= me.speed
                # RIGHT ARROW TO RIGHT
                elif event.key == pygame.K_RIGHT:
                    if me.x < 35:
                        me.change_x += me.speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    me.change_x = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        # SHOW HOW MANY CHANCE LEFT
        glColor3f(1, 1, 1)
        glRasterPos2f(6, 25)
        life = "Chance :"
        for i in range(len(life)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(life[i]))

        # CHANCE BALL
        glColor3f(0.7, 0.4, 1)
        cx = 18
        for i in range(chanceBall+1):
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(cx, 26, 0)
            for i in range(200):
                theta = 2.0 * 3.1415926 * i / 100
                x = 2 * math.cos(theta)
                y = 2 * math.sin(theta)
                glVertex3f(x + cx, y + 26, 0)
            glEnd()
            cx += 4

        # PINK WALL
        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3f(0.8, 0, 0.4)
        glVertex3f(-40, 20, 0)
        glVertex3f(-40, -23, 0)
        glVertex3f(40, -23, 0)
        glVertex3f(40, 20, 0)
        glEnd()

        for wballs in white_list:
            wballs.draw()
            # WHEN HIT PURPLE BALL
            if -(2 + 6) < wballs.y - me.y < 2 and -2 < wballs.x - me.x < 6 + 2:
                hitWhite.play()
                chanceBall -= 1
                wballs.x = random.randrange(-37, 37)
                wballs.y = random.randrange(-17, 17)

        for rballs in red_list:
            rballs.draw()
            # WHEN HIT PURPLE BALL
            if -(2 + 6) < rballs.y - me.y < 2 and -2 < rballs.x - me.x < 6 + 2:
                hitRed.play()
                endGame(1, style, music, hitRed, hitWhite, win, lose)
                rballs.x = random.randrange(-37, 37)
                rballs.y = random.randrange(-17, 17)

        me.draw()

        # GAME OVER WHEN CHANCE BECOME ZERO
        if chanceBall < 0:
            endGame(0, style, music, hitRed, hitWhite, win, lose)

        pygame.display.flip()

# INFORMATION
def help(music):
    current = False
    while not current:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.8,0.9,1)
        glBegin(GL_QUADS)
        glVertex3f(-35, -25, 0)
        glVertex3f(-35, 25, 0)
        glVertex3f(35, 25, 0)
        glVertex3f(35 , -25, 0)
        glEnd()

        glColor3f(0, 0, 1)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-20, 15, 0)
        glScalef(8 / 152.38, 10 / 152.38, 0.1 / 152.38)
        hlp = "INFORMATION"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(hlp[i]))
        glPopMatrix()

        longText = ['',
                    '\n  PRESS RIGHT AND LEFT ARROW TO MOVE THE PURPLE BALL ',
                    '\n  PRESS SPACE KEY TO SHOOT THE PURPLE BALL ',
                    '\n  HIT THE RED BALL TO WIN ',
                    '\n  YOU HAVE 6 CHANCES FOR EACH MODE ',
                    '\n  WHEN HIT WHITE BALL WILL LOSE ONE CHANCE ',
                    '\n  EASY MODE FOR 2 WHITE BALL ',
                    '\n  NORMAL MODE FOR 4 WHITE BALL ',
                    '\n  HARD MODE FOR 6 WHITE BALL ',
                    '',
                    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n']
        ypos=13
        for i in range(len(longText)):
            glRasterPos2f(-32, ypos)
            for j in range(len(longText[i])):
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(longText[i][j]))
            ypos-=4

        # CLICK FOR INFORMATION
        mouse_3 = pygame.mouse.get_pos()
        click_3 = pygame.mouse.get_pressed()

        if 727 > mouse_3[0] > 608 and 537 > mouse_3[1] > 470:
            glColor3f(0, 0, 1)
            if click_3[0]==1:
                current = False
                main(music)
        else:
            glColor3f(0.5,0.5,0.5)
        glBegin(GL_QUADS)
        glVertex3f(21, -24, 0)
        glVertex3f(33, -24, 0)
        glVertex3f(33, -17, 0)
        glVertex3f(21, -17, 0)
        glEnd()
        glColor3f(0, 0, 0)
        glPushMatrix()
        glLineWidth(3)
        glTranslatef(21.5, -22, 0)
        glScalef(5 / 152.38, 5 / 152.38, 0.1 / 152.38)
        resume = "DONE"
        for i in range(len(resume)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(resume[i]))
        glPopMatrix()

        pygame.display.flip()

# GAME OVER WINDOW
def endGame(winGame, style,music,hitRed,hitWhite,win,lose):
    current = True
    if winGame==0:
        lose.play()
    elif winGame==1:
        win.play()

    while current:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1, 0.8, 0.9)
        glBegin(GL_QUADS)
        glVertex3f(-15, -15, 0)
        glVertex3f(-15, 15, 0)
        glVertex3f(15, 15, 0)
        glVertex3f(15, -15, 0)
        glEnd()

        glLineWidth(10)
        # WHEN LOSE
        if winGame == 0:
            glColor3f(0, 0, 0)
            glPushMatrix()
            glLineWidth(3)
            glTranslatef(-11, 5, 0)
            glScalef(5 / 152.38, 10 / 152.38, 0.1 / 152.38)
            youLose = "YOU LOSE"
            for i in range(len(youLose)):
                glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(youLose[i]))
            glPopMatrix()

        # WHEN WIN
        elif winGame == 1:
            glColor3f(0, 0, 0)
            glPushMatrix()
            glLineWidth(3)
            glTranslatef(-10, 5, 0)
            glScalef(5 / 152.38, 10 / 152.38, 0.1 / 152.38)
            youWin = "YOU WIN"
            for i in range(len(youWin)):
                glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(youWin[i]))
            glPopMatrix()

        if style == 1:
            modeGame = "EASY"
        elif style == 2:
            modeGame = "NORMAL"
        elif style == 3:
            modeGame = "HARD"

        glColor3f(0, 0, 0)
        glRasterPos2f(-8, 0)
        mg = "MODE : " + modeGame
        for i in range(len(mg)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(mg[i]))

        mouse_5 = pygame.mouse.get_pos()
        click_5 = pygame.mouse.get_pressed()

        # HOME BUTTON
        if 400 > mouse_5[0] > 250 and 390 > mouse_5[1] > 350:
            glColor3f(1, 0, 0.5)
            if click_5[0] == 1:
                current = False
                main(music)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-8, -8, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 5 * math.cos(theta)
            y = 5 * math.sin(theta)
            glVertex3f(-8 + x, -8 + y, 0)
        glEnd()

        glColor3f(0, 0, 0)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-11.5, -9, 0)
        glScalef(3 / 152.38, 4 / 152.38, 0.1 / 152.38)
        hlp = "HOME"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(hlp[i]))
        glPopMatrix()

        # REPLAY BUTTON
        if 500 > mouse_5[0] > 420 and 460 > mouse_5[1] > 340:
            glColor3f(0.5, 0, 1)
            if click_5[0] == 1:
                current = False
                game(style, music, hitRed, hitWhite, win, lose)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_QUADS)
        glVertex3f(13, -3, 0)
        glVertex3f(3, -3, 0)
        glVertex3f(3, -13, 0)
        glVertex3f(13, -13, 0)
        glEnd()

        glColor3f(0, 0, 0)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(4, -9, 0)
        glScalef(2.5 / 152.38, 4 / 152.38, 0.1 / 152.38)
        hlp = "REPLAY"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(hlp[i]))
        glPopMatrix()

        pygame.display.flip()

def main(playSound):
    glutInit(sys.argv)
    pygame.init()
    size = (800,600)
    pygame.display.set_mode(size,DOUBLEBUF | OPENGL)
    gluPerspective(45, (size[0] / size[1]), 0.1,100)
    glTranslatef(0, 0, -73)
    pygame.display.set_caption("SHOOTING GAME")

    done = False
    clock = pygame.time.Clock()
    hitRed = pygame.mixer.Sound("red.wav")
    hitWhite = pygame.mixer.Sound("white.wav")
    win = pygame.mixer.Sound("win.wav")
    lose = pygame.mixer.Sound("lose.wav")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        style=select(playSound)
        game(style,playSound,hitRed,hitWhite,win,lose)
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main(1)

