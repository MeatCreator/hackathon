import pygame

button_images = ["assets/rock.png", "assets/paper.png", "assets/scissors.png"]
pressed_button_images = ["assets/rock_pressed.png", "assets/paper_pressed.png", "assets/scissors_pressed.png"]
button_sprites = [None,None,None]
pressed_button_sprites = [None,None,None]
class hud:
    def __init__(self, pointer):
        self.pointer = pointer
        self.pressed = 4
        for i in range(3):
            s = pygame.sprite.Sprite()
            s.image = pygame.image.load(button_images[i])
            s.rect = s.image.get_rect()
            s.rect.center=(100+i*156,460)
            button_sprites[i]=s
            s2 = pygame.sprite.Sprite()
            s2.image = pygame.image.load(pressed_button_images[i])
            s2.rect = s.image.get_rect()
            s2.rect.center=(100+i*156,460)
            pressed_button_sprites[i]=s2


    def draw(self, surface):       
        if pygame.mouse.get_pressed()[0]:
            collided = False
            for i in range(3):
                if pygame.sprite.collide_rect(button_sprites[i], self.pointer):
                    collided = True
                    self.pressed = i
                    break
        for i in range(3):
            if self.pressed == i:
                surface.blit(pressed_button_sprites[i].image, pressed_button_sprites[i].rect)
            else:
                surface.blit(button_sprites[i].image, button_sprites[i].rect)
        