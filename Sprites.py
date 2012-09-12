#This is the SpriteHelper class that helps you load and prepare animated sprites for your pygame games!

import pygame

def load_animated_sprite( h, w, filename):
	images = []
	master_image = pygame.image.load(filename).convert_alpha()
	master_width, master_height = master_image.get_size()
	for i in xrange(int(master_width/w)):
		images.append(master_image.subsurface((i*w,0,w,h)))
	return images
