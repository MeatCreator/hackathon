import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("assets/grass.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)