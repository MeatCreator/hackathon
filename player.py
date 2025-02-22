import pygame
import background

Yellow = (255,255,0)
class player(pygame.sprite.Sprite):
  def __init__(self, mainscreen):
    super().__init__()
    self.rect = pygame.Rect(-10,10,-10,10)
    self.x = 20
    self.y = 100
    self.radius = 15
    self.velocity = 2
    self.origin = (self.x, self.y)
  
  def draw(self, mainscreen):
    pygame.draw.circle(mainscreen, Yellow, (self.x, self.y), self.radius)
  
  
  def update(self):
    #this will scale REALLY badly
    #but it works for now
    # for r in range(0,8):
    #     for c in range(0,8):    
    #       if(background.tiles[r][c] >= 1 and (self.x >= c*64 and self.x <= (c+1)*64)):
    #           print(r,c)
    #           if(self.origin[0] > self.x):
    #             self.x = self.x+15
    #           else:
    #             self.x = self.x-15
    #       elif(background.tiles[r][c] >= 1 and (self.y >= r*64 and self.y <= (r+1)*64)):
    #           print(r,c)
    #           if(self.origin[1] > self.y):
    #             self.y = self.y+15
    #           else:
    #             self.y = self.y-15
              
    self.movement()
    self.rect.center=(self.x,self.y)
    self.origin = (self.x, self.y)
    self.movement()

    
  def movement(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and self.velocity > 0 and self.x < 498:
      self.x += self.velocity
    if keys[pygame.K_a] and self.velocity > 0 and self.x > 15:
      self.x -= self.velocity
    if keys[pygame.K_w] and self.velocity > 0 and self.y > 15:
      self.y -= self.velocity
    if keys[pygame.K_s] and self.velocity > 0 and self.y < 498:
      self.y += self.velocity