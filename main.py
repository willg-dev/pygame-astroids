# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import pygame.constants
from player import *

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
		
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, (0,0,0))
		player.draw(screen)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick() / 1000
if __name__ == "__main__":
	main()
