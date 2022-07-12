import pygame,sys

def logic(surface,offset):

	ledge_rotate_mask=pygame.mask.from_surface(ledge_rotate)
	global bird_move
	bird_rect.centery+=bird_move
	if bird_rect.bottom>=576 or bird_rect.top<=0:
		bird_move*=-1
	result=ledge_rotate_mask.overlap(bird_mask,offset)
	if result:
		bird_move*=-1

def rotate(surface,angle):
	rotated_surface=pygame.transform.rotate(surface,-angle)
	rotated_rect=rotated_surface.get_rect(center=(512,288))
	return rotated_surface,rotated_rect
pygame.init()

screen=pygame.display.set_mode((1024,576))
clock=pygame.time.Clock()

ledge=pygame.image.load(r'C:\users\chand\ballbalancer\wood.png').convert_alpha()
ledge_mask=pygame.mask.from_surface(ledge)
ledge_rect=ledge.get_rect(center=(512,288))

bird=pygame.image.load(r'C:\Users\chand\ballbalancer\bird.png').convert_alpha()
bird_mask=pygame.mask.from_surface(bird)
bird_rect=bird.get_rect(center=(512,20))

bird_move=1
angle=0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	angle+=1
	ledge_rotate,ledge_rect_rotate=rotate(ledge,angle)

	mx=bird_rect.centerx-bird.get_width()//2
	my=bird_rect.centery-bird.get_height()//2
	lx=512-ledge_rotate.get_width()//2
	ly=288-ledge_rotate.get_height()//2
	lx=512-ledge.get_width()//2
	ly=288-ledge.get_height()//2

	offset=(mx-lx,my-ly)
	
	screen.fill((0,0,250))
	logic(ledge,offset)
	
	screen.blit(ledge_rotate,ledge_rect_rotate)
	screen.blit(bird,(mx,my))
	pygame.display.update()
	clock.tick(60)