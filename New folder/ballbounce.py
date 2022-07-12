import pygame,sys



def rotatedxy(surface,angle):
   global ball_y
   circle_rect.y+=ball_y
   rotated_surface=pygame.transform.rotozoom(surface,-angle,1)
   rotated_rect=rotated_surface.get_rect(center=(250,400)) 

 
   mx,my=circle_rect.centerx-circle.get_width()//2,circle_rect.centery-circle.get_height()//2


  
   offset=(mx-(250 - rotated_surface.get_width()//2),my-(400 - rotated_surface.get_height()//2))
   rotated_surface_mask = pygame.mask.from_surface(rotated_surface)


     #collision with boundry
   if circle_rect.top<=0 or circle_rect.bottom>=800:
        ball_y+=1
  
   result = rotated_surface_mask.overlap(circle_mask,offset)
   #result2 = rotated_surface_mask.overlap(circle2_mask,offset)

   if result:
        ball_y*=-1
 
    
    
   screen.blit(circle,(mx,my))

   screen.blit(rotated_surface,rotated_rect)
  
   




pygame.init()
screen=pygame.display.set_mode((500,800))
clock=pygame.time.Clock()

bg_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/background1.png').convert()
#bg_surface=pygame.transform.scale2x(bg_surface)
ledge_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/base.png').convert_alpha()
ledge_rect=ledge_surface.get_rect(center=(100,400))
ledge_mask=pygame.mask.from_surface(ledge_surface)
angle=0
p=0
#ox=wedge_rect.centerx
#oy=wedge_rect.centery

circle=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/ball.png').convert_alpha()
circle_mask = pygame.mask.from_surface(circle)
circle_rect=circle.get_rect(center=(250,50))
#pos=circle_mask.mask.set_at((250,5))
circle2 = pygame.image.load('C:/Users/DRAVI/Pictures/ci2.png').convert_alpha()
circle2_mask = pygame.mask.from_surface(circle)

#circle_rect = circle.get_rect()
#circle_mask = pygame.mask.from_surface(circle)

colour = circle

#ball_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/ball.png').convert_alpha()
#ball_rect=ball_surface.get_rect(center=(250,200))
ball_y=1
ball_x=20
TRY=pygame.USEREVENT
pygame.time.set_timer(TRY,1300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                  pygame.quit()
                  sys.exit()
              
    angle+=1
    screen.fill((0, 0, 128))
    #screen.blit(wedge_surface,(ox,oy))
    rotatedxy(ledge_surface, angle)
    # ball_bounce()
    
    

    pygame.display.update() 
    clock.tick(120)