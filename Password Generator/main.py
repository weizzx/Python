import pygame
from pygame.locals import *
import pass_gen

pygame.init()


screen_width = 260
screen_height = 70

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Password Generator')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = ("#ffffe4")
black = (0, 0, 0)
white = ("#ffffe4")

#define global variable
clicked = False

class button():
		
	#colours for button and text
	button_col = ("#22222")
	click_col = ("#444444")
	text_col = black
	width = 260
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, "#444444", button_rect, 5)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



b_pass_gen = button(0, 0, 'Generate Password')


run = True
while run:

	screen.fill(bg)

	if b_pass_gen.draw_button():
		password = pass_gen.GenPass()
		print(password)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()