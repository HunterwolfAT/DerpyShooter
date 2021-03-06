#this is going to be a sidescrolling shooter (also known as 'shmup') with MLP characters!
#The purpose of this game is intirely for fun and educational uses (for example to learn how to write a game)

############################################################
########## DerpyShooter (c) 2012 by Hunterwolf #############
############################################################

import pygame
from player import *
from level import *
from Sprites import *
from sound import *
from enemies import *

pygame.init()
screen = pygame.display.set_mode((800,480)) 

step_size = 1		#Time until game logic
max_frame_time = 50	#Time until frame rendering
enemy_step = 0

soundmanager = sound()

player = player()
gameisrunning = True

projectiles = []
enemies = []

def render(level):
	#screen.fill((0,0,30))
	#Hintergrund malen
	level.draw(screen)
		
	#ENEMYS INCOMING
	for enemy in enemies:
		enemy.draw(screen)

	player.draw(screen)
	
	#Draw projectiles
	for projectile in projectiles:
		screen.blit(projectile.images[projectile.currentframe], projectile.rect.topleft)

	pygame.display.flip()

def update(level):
	global enemy_step
	#Update that shit!
	player.update()
	for enemy in enemies:
		if enemy.update():
			enemies.remove(enemy)
	
	#Did anything hit anything?
	to_delete = []
	for projectile in projectiles:
		projectile.move()
		ishit = projectile.checkcollision(player.rect, enemies)
		if ishit:
			if projectile.fromplayer:
				to_delete.append(projectile)
				enemies[ishit - 1].hp -= projectile.damage
				if enemies[ishit - 1].hp <= 0:
					enemies[ishit - 1].is_dying()
				print "YOUUUU HIT SOMETHING PAL!"
			else:
				print "SHIT YOU DEAD BUDDY!"
	for item in to_delete:
		projectiles.remove(item)
	
	#When an enemy gets past the player and moves left off the screen, delete it too
	#Also, check wether the player touched an enemy
	for enemy in enemies:
		if player.rect.colliderect(enemy.rect) and not enemy.dead and not player.dead:
			player.dying()

		if enemy.rect.left + enemy.rect.width < 0:
			enemies.remove(enemy)

	#Sound stuff!
	soundmanager.startmusic()

	#Move the background along!
	level.update()

def checkenemies(time):
	if level.enemiespawner is not None:
		newenemys = level.enemiespawner.makeenemies(time)
		if len(newenemys) != 0:
			for newenemy in newenemys:
				enemies.append(newenemy)

def checkevents():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False
	
	keys = pygame.key.get_pressed()

	player.vector = (0,0)

	if keys[pygame.K_ESCAPE]:
		return False

	if keys[pygame.K_RIGHT]:
		#player.setmovevector((1,0))
		if (player.vector[0] != 1):
			player.setmovevector((1, player.vector[1]))
		player.startmoving()
	if keys[pygame.K_UP]:
		#player.setmovevector((0,-1))
		if (player.vector[1] != -1):
			player.setmovevector((player.vector[0], -1))
		player.startmoving()
	if keys[pygame.K_DOWN]:
		#player.setmovevector((0,1))
		if (player.vector[1] != 1):
			player.setmovevector((player.vector[0], 1))
		player.startmoving()
	if keys[pygame.K_LEFT]:
		#player.setmovevector((-1,0))
		if (player.vector[0] != -1):
			player.setmovevector((-1, player.vector[1]))
		player.startmoving()
	# SHOOT THINGS!
	if keys[pygame.K_SPACE]:
		if not player.dead:
			newproj = player.shoot()
			if newproj != False:
				projectiles.append(newproj)
	
	return True

#============== THE MAIN PART HERE =======================
now = pygame.time.get_ticks()

level = level("Greenhill Zone", Level1Enemies())

while(gameisrunning):

	currentTicks = pygame.time.get_ticks()

	if currentTicks - now > max_frame_time:
		now = currentTicks - step_size
	
	while(currentTicks - now >= step_size):

		#Game stuff!
		print now
		checkenemies(now)
		gameisrunning = checkevents()
		update(level)
		render(level)

		now += step_size
	else:
		pygame.time.wait(10)
