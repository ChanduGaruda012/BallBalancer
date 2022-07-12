import pygame,sys
def rotate(surface,angle):
	rotated_surface=pygame.transform.rotate(surface,angle)
	rotated_rect=rotated_surface.get_rect(center=(250,250))
	return rotated_surface,rotated_rect
pygame.init()
screen=pygame.display.set_mode((1024,576))
clock=pygame.time.Clock()
bg=pygame.image.load(r'C:\Users\chand\ballbalancer\background.jpg').convert()
wood=pygame.image.load(r'C:\users\chand\ballbalancer\wood.png').convert_alpha()
angle = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	angle+=1
	wood_rotate,wood_rect_rotate=rotate(wood,angle)
	screen.blit(bg,(0,0))
	screen.blit(wood_rotate,wood_rect_rotate)
	pygame.display.update()
	clock.tick(120)