import pygame
import player
import background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)

class Pointer(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/pointer.png")
        self.rect = self.image.get_rect()
        self.rect.center=(0,0) 
 
      def move(self):
        x,y = pygame.mouse.get_pos()
        self.rect.center = (x+32,y+32)
        

 
      def draw(self, surface):
        surface.blit(self.image, self.rect)

p = Pointer()
game_player = player.player(screen)
game_background = background.Background(screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    #p.update()
    # RENDER YOUR GAME HERE
    p.move()
    p.draw(screen)

    game_background.draw()

    game_player.update()
    game_player.draw(screen)
  
    # flip() the display to put your work on screen
    pygame.display.flip()
    #pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
