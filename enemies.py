# Enemies.py
#
# Description:
# This file contains all the different enemy types!

import pygame
from path import *
from Sprites import *

class enemy():
	def __init__(self, name, images, hp, position, velocity, movement=None, weapons=None):
		self.name = name
		self.images = images
		self.currentframe = 0
		self.animationtimer = 0
		self.rect = images[0].get_rect()
		self.rect.top = position[1]
		self.rect.left = position[0]
		self.velocity = velocity
		self.hp = hp
		self.movement = movement
		self.weapons = weapons
		self.dead = False
	
	def update(self):
		#Play animation
		self.animationtimer += 1
		if (self.animationtimer == 3):
			self.currentframe += 1
			self.animationtimer = 0
			if self.currentframe >= len(self.images): self.currentframe = 0	


		self.rect.top += self.velocity[1]
		self.rect.left += self.velocity[0]

		if self.dead:
			self.velocity = (0, self.velocity[1]+1)
			if self.rect.top > 480:
				return True		# Return True wenn enemy was shot and fell out of the game
		return False
	
	def is_dying(self):
		self.dead = True
		self.velocity = (0, -10)
	
	def draw(self, screen):
		screen.blit(self.images[self.currentframe], self.rect.topleft)
