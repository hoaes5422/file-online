import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

BLACK = (0,0,0)
running = True
while running:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.type == 1:	
				print("I love my wife")
		pygame.display.flip()

pygame.quit()		
