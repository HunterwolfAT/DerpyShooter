from Sprites import *
from projectile import *
from path import *
import os



class player:
	def __init__(self):
		self.dead = False
		self.lives = 2
		self.velocity = 0
		self.image = load_animated_sprite(67, 82, pathtoscript + "derpy.png")
		self.derpylive = pygame.image.load(pathtoscript + "live.png")
		self.gameoverimage = pygame.image.load(pathtoscript + "gameover.png")
		#self.rect = pygame.rect(self.position[0], self.position[1], self.image[0].get_width(), self.image[0].get_height())
		self.rect = self.image[0].get_rect()
		self.rect.height /= 2
		self.rect.width /= 2
		self.rect.top = 50
		self.rect.left = 30
		#print self.rect.height
		#print self.rect.width
		self.currentframe = 0
		self.animationtimer = 0
		self.moving = False
		self.maxvelocity = 6
		self.acceleration = 1
		self.inertia = 3
		self.vector = (0,0)
		self.firecharge = 0 	# when the player fires the weapon, this will be set to a value and counts down to zero. 
					#Only then can the weapons be fired again
		self.deadtimer = 0
	
	def draw(self, screen):
		if self.lives >= 0:
			if self.dead and self.deadtimer > 5 and self.deadtimer < 15 or self.dead and self.deadtimer > 25 and self.deadtimer < 35 or self.dead and self.deadtimer > 45 and self.deadtimer < 55 or not self.dead:
				screen.blit(self.image[self.currentframe], (self.rect.left - 20, self.rect.top - 16))

		#Draw "GUI"
		for x in range(self.lives):
			screen.blit(self.derpylive, (30 + (80*x), 420))
		if self.dead and self.lives < 0:
			screen.blit(self.gameoverimage, (180, 160))
		
	
	def startmoving(self):
		self.moving = True
	
	def stopmoving(self):
		self.moving = False

	def setmovevector(self, vector):
		self.vector = vector
	
	def dying(self):
		self.dead = True
		self.lives -= 1
		print "YOU DUN GOOFED!"

	def shoot(self):
		if self.firecharge == 0:
			bubbleimages = load_animated_sprite(30, 30, pathtoscript + "bubble.png")
			newprojectile = Bubble((1,0), 10, bubbleimages, True, self.rect.topright)  
			self.firecharge = 16
			return newprojectile

		return False

	def move(self):
		self.rect.left += self.vector[0] * self.velocity
		if self.rect.left < 0: self.rect.left = 0
		if self.rect.left > (800-self.rect.width): self.rect.left = (800 - self.rect.width)
		self.rect.top += self.vector[1] * self.velocity
		if self.rect.top < 0: self.rect.top = 0
		if self.rect.top > (480 - self.rect.height): self.rect.top = (480 - self.rect.height)

	def update(self):
		#Play animation
		#self.image[self.currentframe]
		self.animationtimer += 1
		if (self.animationtimer == 3):
			self.currentframe += 1
			self.animationtimer = 0
			if self.currentframe >= len(self.image): self.currentframe = 0

		#If the Play is moving, slowly get faster
		if self.moving:
			self.velocity += self.acceleration
			if self.velocity >= self.maxvelocity:
				self.velocity = self.maxvelocity
		else:
			self.velocity -= self.inertia
			if self.velocity < 0:
				self.velocity = 0

		self.move()

		if self.firecharge > 0:
			self.firecharge -= 1

		#If the player died and still has lives left, respawn him after a while
		if self.dead:
			self.deadtimer += 1
			if self.deadtimer >= 60 and self.lives >= 0:
				self.deadtimer = 0
				self.dead = False
