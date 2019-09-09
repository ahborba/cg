from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

w, h = 400, 400

# ---Section 1---
def corpo_gato():
    for i in range(0,int(0.3*h)):
        print(i)
        circle(int(w/2),h-i,20)


def circle(posx, posy, radius):
    sides = 32
    # radius = 0.85*w
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides) + posx
        sine = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


def square(x, y, width, height):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)  # Begin the sketch
    glVertex2f(x, y)  # Coordinates for the bottom left point
    glVertex2f(x+width, y)  # Coordinates for the bottom right point
    glVertex2f(x+width, y+height)  # Coordinates for the top right point
    glVertex2f(x, y+height)  # Coordinates for the top left point
    glVertex2f(x-100, y+10)  # Coordinates for the top left point
    glEnd()  # Mark the end of drawing

# This alone isn't enough to draw our square

# ---Section 2---

# Add this function before Section 2 of the code above i.e. the showScreen function


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    # Remove everything from screen (i.e. displays all white)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Reset all graphic/shape's position
    glLoadIdentity()
    iterate()
    glColor3f(255.0, 255.0, 255.0)  # Set the color to pink
    # Draw a square using our function
    # square(100,100,200,200)
    # fundo da tela
    circle(int(w/2),int(h/2),int(0.43*w))
    corpo_gato()
    glutSwapBuffers()

# ---Section 3---


glutInit()
glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
glutInitWindowSize(w, h)   # Set the w and h of your window
# Set the position at which this windows should appear
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")  # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)  # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
