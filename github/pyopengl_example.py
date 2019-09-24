#!/usr/bin/python
'''Use evaluators to draw a Bezier curve.'''

from Window import *

class BezierCurve(Window):

	def __init__(self):
		self.width  = 1024
		self.height = 1024
		self.keybindings = {chr(27):exit}
		glutInit()
		glutInitWindowSize(self.width, self.height)
		glutCreateWindow('flamengo')
		# Just request them all and don't worry about it.
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA|GLUT_DEPTH)
		glClearColor(0, 0, 0, 0)
		# glutReshapeFunc(self.reshape)
		# glutKeyboardFunc(self.keyboard)
		glutDisplayFunc(self.display)
		# glutMouseFunc(self.mouse)
		glShadeModel(GL_FLAT)
		glutInit()
		self.controlPoints = ((1, 1, 0),( -2/5.0, 4/5.0, 0), (2/50.0, -4/5.0, 0), (4/5.0, 4/5.0, 0))
		glClearColor(0, 0, 0, 0)
		glShadeModel(GL_FLAT)
		glMap1f(GL_MAP1_VERTEX_3, 0, 1, self.controlPoints)
		glEnable(GL_MAP1_VERTEX_3)

	def display(self):
		'''Display the control points as dots.'''
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 1, 1)
		glBegin(GL_LINE_STRIP)
		for i in range(32):
			glEvalCoord1f(float(i)/31)
		glEnd()
		glPointSize(50)
		glColor3f(1, 1, 0)
		glBegin(GL_POINTS)
		for point in self.controlPoints:
			glVertex3fv(point)
		glEnd()
		glFlush()

if __name__ == '__main__':
	BezierCurve()
	glutMainLoop()