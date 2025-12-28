import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption("Dino Runner")
clock=pygame.time.Clock()

#load the image of the dinosaur
dino_img=pygame.image.load("assets/dino.png")
dino_img = pygame.transform.scale(dino_img, (60, 60))  
cactus_img=pygame.image.load("assets/cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (50, 60))  

#cactus starting position
cactus_x = 600

#dino_physics
dino_y=200
dino_vel_y=0
gravity=1.8
jump_power=-18
is_jumping = False

score =0
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_vel_y = jump_power
                is_jumping = True
                

    screen.fill((255,255,255))


    #cactus movement
    cactus_x=  cactus_x-10
    if(cactus_x<-50):
        cactus_x=800

    # Apply gravity
    dino_y += dino_vel_y
    dino_vel_y += gravity

    # Stay on ground
    if dino_y >= 200:
        dino_y = 200
        is_jumping = False

    # Collision detection
    dino_rect = pygame.Rect(50, dino_y, dino_img.get_width(), dino_img.get_height())
    cactus_rect = pygame.Rect(cactus_x, 200, cactus_img.get_width(), cactus_img.get_height())

    if dino_rect.colliderect(cactus_rect):
    # Show Game Over text
        font = pygame.font.Font(None, 72)  # large text
        text = font.render("GAME OVER", True, (255, 0, 0))  # red color
        screen.blit(text, (330, 200))

        font_small = pygame.font.Font(None, 48)
        score_text = font_small.render(f"Score: {int(score)}", True, (0, 0, 0))
        screen.blit(score_text, (380, 250))
          
        pygame.display.update()
        pygame.time.delay(1500)

        pygame.quit()
        sys.exit()

    # Update score
    score += 0.5

    # Draw Dino and cactus
    screen.blit(dino_img, (50, dino_y))
    screen.blit(cactus_img, (cactus_x, 200))

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(int(score)), True, (0, 0, 0))
    screen.blit(score_text, (700, 20))



    pygame.display.update()
    clock.tick(30)