import pygame
#0=grass
#1=water
#2=road
tiles=[
    [0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,0,0],
    [0,0,0,0,0,2,0,0],
    [0,0,0,0,0,2,0,0],
    [0,2,2,2,2,2,0,0],
    [0,2,0,0,0,0,0,0],
    [0,2,0,0,0,0,0,0],
    [0,2,2,2,2,2,2,2]
]
sprites = [[None] * 8 for x in range(8)]
images = [
    "assets/grass.png",
    "assets/water.png",
    "assets/road.png"
]

class Background():
    def __init__(self, screen):
        self.screen = screen
        for r in range(0,8):
            for c in range(0,8):
                s = pygame.sprite.Sprite()
                s.image = pygame.image.load(images[tiles[r][c]])
                s.rect = s.image.get_rect()
                s.rect.topleft = (c*64, r*64)
                sprites[r][c]=s

    def draw(self):
        for r in range(0,8):
            for c in range(0,8):
                self.screen.blit(sprites[r][c].image, sprites[r][c].rect)