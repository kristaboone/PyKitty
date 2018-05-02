import pygame,os
from pygame.locals import *

path_to_images= os.getcwd() + '\images\\' 

class Param():
	def __init__(self, integer, string):
		self.int_val= integer
		self.str_val= string

class Color():	
	black= Param(0, 'B')
	jet_black= Param(1, 'JB')
	orange= Param(2, 'O')
	spotted= Param(3, 'SP')
	white= Param(4,'W')
	
	list= [black, jet_black, orange, spotted, white]

class Direction():
	invalid= Param(-1, 'NULL')
	north= Param(0, 'N')
	south= Param(1, 'S')
	east= Param(2, 'E')
	west= Param(3, 'W')
	
	list= [invalid, north, south, east, west]

class Kitteh(object):
	def __init__(self, color, initial_pos):
		
		self.x= initial_pos[0]
		self.y= initial_pos[1]
		
		self.img_cnt= 1
		self.img_inc= True
		self.lst_dir= Direction.south
		
		self.color= self.setColor(color)
		self.loadNewImage(self.color, self.lst_dir, self.img_cnt)
	
	def get_x_pos(self):
		return self.x
		
	def move_kitteh(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		surface.blit(self.curr_img, (self.x, self.y))
	
	def setColor(self, c):
		for color in Color.list:
			if c == color.int_val or c == color.str_val:
				return color
			
	def handleKeys(self):
		key= pygame.key.get_pressed()
		dir= Direction.invalid
		dist= 5
		
		if key[pygame.K_UP]:
			self.y -= dist
			dir= Direction.north
		elif key[pygame.K_DOWN]:
			self.y += dist
			dir= Direction.south
		elif key[pygame.K_RIGHT]:
			self.x += dist
			dir= Direction.east
		elif key[pygame.K_LEFT]:
			self.x -= dist
			dir= Direction.west
		
		if not dir == Direction.invalid:
			if self.img_cnt == 1:
				self.img_cnt+= 1
			elif self.img_cnt == 2:
				if self.img_inc:
					self.img_cnt+= 1
					self.img_inc= False
				elif not self.img_inc:
					self.img_cnt-= 1
					self.img_inc= True
			elif self.img_cnt == 3:
				self.img_cnt-= 1
			
			self.lastDir= dir
			self.lastImgCount= self.img_cnt
			self.loadNewImage(self.color, self.lastDir, self.img_cnt)
			return True

		else:
			return False
			
	def loadNewImage(self, color, direction, number):
		self.curr_img= pygame.image.load(path_to_images + color.str_val + '_' + direction.str_val + str(number) + '.png')
