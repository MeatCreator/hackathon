import pygame

class level(pygame.sprite.Sprite):
    def __init__(self, image, posx, posy, levelNum):
        super().__init__() 
        self.levelNum = levelNum
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center=(posx,posy)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
  
  
 