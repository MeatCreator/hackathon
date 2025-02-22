import pygame
import RockPaperScissorsGame

button_images = ["assets/rock.png", "assets/paper.png", "assets/scissors.png"]
pressed_button_images = ["assets/rock_pressed.png", "assets/paper_pressed.png", "assets/scissors_pressed.png"]
button_sprites = [None,None,None]
pressed_button_sprites = [None,None,None]
class hud:
    def __init__(self, pointer):
        self.pointer = pointer
        self.pressed = 4
        self.confirm_button = pygame.sprite.Sprite()
        self.confirm_button.image = pygame.image.load("assets/confirm_button.png")
        self.confirm_button.rect = self.confirm_button.image.get_rect()
        self.confirm_button.rect.center = (256, 350)
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
            if pygame.sprite.collide_rect(self.confirm_button, self.pointer) and self.pressed != 4:
                self.confirm()
        for i in range(3):
            if self.pressed == i:
                surface.blit(pressed_button_sprites[i].image, pressed_button_sprites[i].rect)
            else:
                surface.blit(button_sprites[i].image, button_sprites[i].rect)
        surface.blit(self.confirm_button.image, self.confirm_button.rect)

    def confirm(self):
        result = 2
        if self.pressed == 0:
            result = RockPaperScissorsGame.normal_logic("rock")
        elif self.pressed == 1:
            result =  RockPaperScissorsGame.normal_logic("paper")
        elif self.pressed == 2:
            result = RockPaperScissorsGame.normal_logic("scissors")

        print(result)
        self.pressed = 4
        #nothing is pressed
        if(result == 2):
            return        