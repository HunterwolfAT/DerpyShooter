# Level.py
#
# Description:
# This contains all the sprites of the levels, the collision data for the enviroment and the spawn
# behaviour for enemys!

import pygame

from path import *
from Sprites import *
from enemies import *

class level():
	def __init__(self, name, enemiespawner=None):
		self.name = name
		self.sp_ground = pygame.image.load(pathtoscript + "level1_ground.png")
		self.sp_back1 = pygame.image.load(pathtoscript + "level1_back1.png")
		self.sp_back2 = pygame.image.load(pathtoscript + "level1_back2.png")
		self.sp_back3 = pygame.image.load(pathtoscript + "level1_back3.png")
		self.sp_back4 = pygame.image.load(pathtoscript + "level1_back4.png")
		self.sp_sky = pygame.image.load(pathtoscript + "level1_background.png")
		
		self.groundpos = 0
		self.back1pos = 0
		self.back2pos = 0
		self.back3pos = 0
		self.back4pos = 0
		self.skypos = 0

		self.enemiespawner = enemiespawner
	
	def update(self):
		self.groundpos -= 30
		self.back1pos -= 5
		self.back2pos -= 4
		self.back3pos -= 3
		self.back4pos -= 2
		self.skypos -= 1

		if self.groundpos <= -850: self.groundpos = 0
		if self.back1pos <= -850: self.back1pos = 0
		if self.back2pos <= -850: self.back2pos = 0
		if self.back3pos <= -850: self.back3pos = 0
		if self.back4pos <= -850: self.back4pos = 0
		if self.skypos <= -850: self.skypos = 0

	def draw(self, screen):
		screen.blit(self.sp_sky, (self.skypos, 0))
		screen.blit(self.sp_sky, (self.skypos+850, 0))
		screen.blit(self.sp_back4, (self.back4pos, 190))
		screen.blit(self.sp_back4, (self.back4pos+850, 190))
		screen.blit(self.sp_back3, (self.back3pos, 190))
		screen.blit(self.sp_back3, (self.back3pos+850, 190))
		screen.blit(self.sp_back2, (self.back2pos, 250))
		screen.blit(self.sp_back2, (self.back2pos+850, 250))
		screen.blit(self.sp_back1, (self.back1pos, 255))
		screen.blit(self.sp_back1, (self.back1pos+850, 255))
		screen.blit(self.sp_ground, (self.groundpos, 340))
		screen.blit(self.sp_ground, (self.groundpos+850, 340))


class Level1Enemies():
	def __init__(self):
		self.gildasprite = load_animated_sprite(146, 130, pathtoscript + "gilda.png")
		self.boxxysprite = load_animated_sprite(106, 102, pathtoscript + "boxxy.png")

		self.enemyspawners = []

		self.enemyspawners.append(EnemySpawner(self.makeGilda, 3000, 40, 5, 40))
		self.enemyspawners.append(EnemySpawner(self.makeGilda, 11000, 310, 5, 40))
		self.enemyspawners.append(EnemySpawner(self.makeBoxxy, 19000, 270, 4, 25))
		self.enemyspawners.append(EnemySpawner(self.makeBoxxyDecsent, 19000, 50, 4, 25))
		self.enemyspawners.append(EnemySpawner(self.makeGilda, 28000, 40, 5, 35))
		self.enemyspawners.append(EnemySpawner(self.makeGilda, 28000, 300, 5, 35))
	
	def makeGilda(self, yposition):
		return enemy("Gilda", self.gildasprite, 4, (1000, yposition), (-5, 0)) 

	def makeBoxxy(self, yposition):
		return enemy("Boxxy", self.boxxysprite, 6, (1000, yposition), (-3, -1))

	def makeBoxxyDecsent(self, yposition):
		return enemy("Boxxy", self.boxxysprite, 6, (1000, yposition), (-3, 1))
	
	def makeenemies(self, time):
		newenemys = []
		for spawner in self.enemyspawners:
			resultenemy = spawner.Spawn(time)
			if resultenemy is not None:
				newenemys.append(resultenemy)
			if spawner.counter == spawner.repeat:
				self.enemyspawners.remove(spawner)

		#newenemy = self.firstgildas.Spawn(time)
		return newenemys

class EnemySpawner():

	def __init__(self, makeX, time, pos, repeat, step):
		self.step_max = step
		self.step = 0
		self.makeX = makeX
		self.time = time
		self.pos = pos
		self.repeat = repeat
		self.counter = 0

	def Spawn(self, now):
		self.step -= 1
		newenemy = None
		if self.step <= 0:
			if now > self.time and self.counter < self.repeat:
				#print "MAKING A NEW ENEMY!!"
				self.step = self.step_max
				self.counter += 1
				newenemy = self.makeX(self.pos)
				
		return newenemy
			
