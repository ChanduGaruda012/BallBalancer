import pygame,sys
"""def rotate(surface,angle):
	rotated_surface=pygame.transform.rotate(surface,angle)
	rotated_rect=rotated_surface.get_rect(center=(100,100))
	return rotated_surface,rotated_rect"""
pygame.init()
screen=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
#bg=pygame.image.load(r'C:\Users\chand\ballbalancer\wt_background.png').convert()
#ball=pygame.image.load(r'C:\users\chand\ballbalancer\ball.jpg').convert_alpha()
ball=pygame.image.load(r'C:\users\chand\ballbalancer\Happybday.jpg').convert_alpha()
ball_rect = ball.get_rect(center =(400,400))
angle = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	#angle+=1
	#ball_rotate,ball_rect_rotate=rotate(ball,angle)
	#screen.blit(bg,(0,0))
	screen.blit(ball,ball_rect)
	pygame.display.update()
	clock.tick(120)