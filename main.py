import pygame
import player
import background
import level
import hud

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)

levels = [
    level.level("assets/level1.png",100,100, 1),
    level.level("assets/lake.png", 350,280,  2),
]

currentLevel = 0

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

hud = hud.hud(p)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    #p.update()
        
    #check for collisions
    for level in levels:
        if level is not None:
            collision = pygame.sprite.collide_rect(level, game_player)
            if collision and level.levelNum != currentLevel:
                currentLevel = level.levelNum
                hud.level = currentLevel
            
    if currentLevel==0:
        game_background.draw()
        for level in levels:
            if level is not None:
                level.draw(screen)
        game_player.update()
        game_player.draw(screen)
    
    if currentLevel>0:
        if(hud.draw(screen)):
            print("win")
            #game_player.origin = (game_player.x, game_player.y)
            levels[currentLevel-1].kill()
            levels[currentLevel-1] = None
            currentLevel = 0
            hud.level = currentLevel

    p.move()
    p.draw(screen)
    pygame.display.flip()
    #pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
