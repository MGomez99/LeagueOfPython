import pygame
import player1
import player2
import sys

class Controller:
	def __init__(self, width=800 , height=600 ,player1_spec , player2_spec)
	pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.background =pygame.Surface(self.screen.get_size())
		self.player1 = player1_spec
		self.player2 = player2_spec		
		self.sprites = pygame.sprite.Group((self.player1,) + (self.player2,))

	def mainLoop(self):
		pygame.key.set_repeat(1,60)
		while True:
			for event in pygame.event.get():
				if even.type == pygame.Quit:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_UP):
                        			self.player1.move_up()
                   			if(event.key == pygame.K_DOWN):
                        			self.player1.move_down()
                    			if(event.key == pygame.K_LEFT):
                        			self.player1.move_left()
                   			if(event.key == pygame.K_RIGHT):
                        			self.player1.move_right()
					if(event.key == pygame.K_KP1):
						self.player1.attack1()
					if(event.key == pygame.K_KP2):
						self.player1.attack2()
					if(event.key == pygame.K_KP3):
						self.player1.attack3()
					if(event.key == pygame.K_w):
						self.player2.move_up()
					if(event.key == pygame.K_s):
						self.player2.move_down()
					if(event.key == pygame.K_a):
						self.player2.move_left()
					if(event.key == pygame.K_d):
						self.player2.move_right()
					if(event.key == pygame.K_y):
						self.player2.attack1()
					if(event.key == pygame.K_u):
						self.player2.attack2()
					if(event.key == pygame.K_i):
							self.player2.attack3()
			if(pygame.sprite.collide_rect(self.player2.attack, self.player1):
				self.player1.health -= self.player2.attack.damage()
			#copy and paste this for all the attacks or maybe we can for loop it
			if(self.player1.health == 0):
				self.player1.kill()
			if(self.player2.health == 0):
				self.player2.kill()
			self.screen.blit(self.background, (0,0))
			self.sprites.draw(self.screen)
			pygame.display.flip()

def main():
	spec_choice_1 = input("Choose a spec for player 1 (name of specs here): ")
	name1 = input("what is your name? ")
	if spec_choice_1 == "name of spec 1"
		spec_choice_1 = spec.Spec1
		player1_spec = player1_spec.Player1(spec_choice_1, spawn, name1)
	"""same for the other specs"""
	spec_choice_2 = input("Choose a spec for player 2 (name of specs here): ")
	name2 = input("what is your name? ")
	if spec_choice_2 == "name of spec 1"
		spec_choice_2 = spec.Spec1
		player2_spec = player1_spec.Player1(spec_choice_1, spawn, human, name1)
	gameon = Controller(player1_spec, player2_spec)
	gameon.mainLoop()
