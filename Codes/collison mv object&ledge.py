import pygame,sys,os
pygame.init()
screen=pygame.display.set_mode((1024,576))
clock=pygame.time.Clock()
bg=pygame.image.load(r'C:\Users\chand\ballbalancer\background.jpg').convert()
bird=pygame.image.load(r'C:\Users\chand\ballbalancer\bird.png').convert()
bird_rect=bird.get_rect(center=(262,144))
ledge=pygame.image.load(r'C:\Users\chand\ballbalancer\wood.png').convert_alpha()
ledge_rect=ledge.get_rect(center=(512,288))
ledge_rect=ledge.get_rect(topleft=(262,255))
gravity=0.01
bird_move=0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(bg,(0,0))
	bird_move+=gravity
	bird_rect.centery+=bird_move
	if bird_rect.colliderect(ledge_rect):
		print("collision")
	#	bird_rect.centery=ledge_rect.toplefty-12
	screen.blit(bird,bird_rect)
	screen.blit(ledge,ledge_rect)
	pygame.display.update()
	clock.tick(120)