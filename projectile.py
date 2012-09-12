""" Projectile.py
#
# Description:
# This class defines the projectiles the player and the enemies can shoot
# 
#
"""

from Sprites import *

class Bubble( object ):
	def __init__(self, vector, velocity, image, fromplayer, startposition):
		self.damage = 2 #Beause this is the bubble weapon!
		self.vector = vector
		self.velocity = velocity
		self.images = image
		self.currentframe = 0
		self.fromplayer = fromplayer
		#self.rect = pygame.Rect(startposition[0], startposition[1], image[0].width, image[0].height)
		self.rect = self.images[0].get_rect()
		self.rect.topleft = (startposition[0], startposition[1])
	
	def checkcollision(self, playerrect, enemies):
		if self.fromplayer:
			counter = 0
			for enemy in enemies:
				if self.rect.colliderect(enemy.rect) and not enemy.dead:
					return counter + 1 # +1 damit wenn 0 zurueck gegeben wird es nicht mit False verwechselt wird
				counter += 1
		else:
			if self.rect.colliderect(playerrect):
				return True
		#No collision
		return False


	def move(self):
		self.rect.top += self.vector[1] * self.velocity
		self.rect.left += self.vector[0] * self.velocity
