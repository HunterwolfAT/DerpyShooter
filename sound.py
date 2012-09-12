# Sound.py
#
# Description:
# This class takes care of everything you hear! Music and SFX are loaded and played here.
#
#

import pygame
from path import *

class sound():
	
	def __init__(self):
		pygame.mixer.music.load(pathtoscript + "level1.ogg")

	def startmusic(self):
		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.play(-1)

	def stopmusic(self):
		self.currentsong.stop()
	
	def loadlevelmusic(self, number):
		if number == 1:
			pygame.mixer.music.load(pathtoscript + "level1.ogg")

