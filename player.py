import pygame

Yellow = (255,255,0)
class player(pygame.sprite.Sprite):
  def __init__(self, mainscreen):
    super().__init__()
    self.rect = pygame.Rect(-10,10,-10,10)
    self.x = 100
    self.y = 100
    self.radius = 15
    self.velocity = 2
    self.origin = (self.x, self.y)
  
  def draw(self, mainscreen):
    pygame.draw.circle(mainscreen, Yellow, (self.x, self.y), self.radius)
  
  
  def update(self):
    self.movement()
    self.rect.center=(self.x,self.y)
    self.origin = (self.x, self.y)
    
  def movement(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and self.velocity > 0 and self.x < 625:
        self.x += self.velocity
    if keys[pygame.K_a] and self.velocity > 0 and self.x > 15:
      self.x -= self.velocity
    if keys[pygame.K_w] and self.velocity > 0 and self.y > 15:
      self.y -= self.velocity
    if keys[pygame.K_s] and self.velocity > 0 and self.y < 465:
      self.y += self.velocity