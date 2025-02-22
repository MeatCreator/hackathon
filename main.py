import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True

class Pointer(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/pointer.png")
        self.rect = self.image.get_rect()
        self.rect.center=(40,40) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)

p = Pointer()
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
    p.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()
    #pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
