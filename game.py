import os, pygame, sys
from kitteh import Kitteh
from pygame.locals import *

cwd= os.getcwd()
lv_file= cwd+'\images\\living.jpg' 		# Livingroom background
bth_file= cwd+'\images\\bath.jpg'		# Bathroom background
bg_file= cwd+'\images\\bedroom.jpg' 	# Bedroom background
mus_file= cwd+'\music\\music.mp3'		# Background image file

running= True
pygame.init()
pygame.key.set_repeat(100, 100)

# Load music
pygame.mixer.music.load(mus_file)
pygame.mixer.music.play(loops=-1)

# Background images
bedroom= pygame.image.load(bg_file)
living= pygame.image.load(lv_file)
bathroom= pygame.image.load(bth_file)

# Create Display
pygame.display.set_caption('Kitteh\'s Room')
screen= pygame.display.set_mode((bedroom.get_width(),bedroom.get_height()), HWSURFACE|DOUBLEBUF)
screen.blit(bedroom, (0,0))
room= 'bedroom'
pygame.display.flip()

# Create Kitteh
kitteh1= Kitteh(0, [50,100])

# Run Game
while(running):	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False
		if event.type == pygame.KEYDOWN:
			if kitteh1.handleKeys():
				if room == 'bedroom':
					screen.blit(bedroom, (0,0))
				elif room == 'living':
					screen.blit(living, (0,0))
				elif room == 'bathroom':
					screen.blit(bathroom, (0,0))

	kitteh1.draw(screen)
	kitteh_x = kitteh1.get_x_pos()
	
	if room == 'bedroom' and kitteh_x <= 0:
		screen= pygame.display.set_mode((living.get_width(), living.get_height()), HWSURFACE|DOUBLEBUF)
		screen.blit(living, (0,0))
		pygame.display.flip()
		room = 'living'
		kitteh1.move_kitteh(living.get_width()-10, living.get_height()-30)
	elif room == 'bedroom' and kitteh_x > bedroom.get_width():
		screen= pygame.display.set_mode((bathroom.get_width(), bathroom.get_height()), HWSURFACE|DOUBLEBUF)
		screen.blit(bathroom, (0,0))
		pygame.display.flip()
		room = 'bathroom'
		kitteh1.move_kitteh(5, bathroom.get_height()-30)
	elif room == 'bathroom' and kitteh_x <= 0:
		screen= pygame.display.set_mode((bedroom.get_width(), bedroom.get_height()), HWSURFACE|DOUBLEBUF)
		screen.blit(bedroom, (0,0))
		pygame.display.flip()
		room = 'bedroom'
		kitteh1.move_kitteh(bedroom.get_width()-10, bedroom.get_height()-30)
	elif room == 'living' and kitteh_x > living.get_width():
		screen= pygame.display.set_mode((bedroom.get_width(), bedroom.get_height()), HWSURFACE|DOUBLEBUF)
		screen.blit(bedroom, (0,0))
		pygame.display.flip()
		room = 'bedroom'
		kitteh1.move_kitteh(5, bedroom.get_height()-30)
	
	pygame.display.update()