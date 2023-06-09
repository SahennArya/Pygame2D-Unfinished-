import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # self.image = pygame.image.load("player_assets/2 Punk/Punk_hurt.png")
        self.image = pygame.Surface ((25,25))
        # self.image = self.animations["idle"][self.frame_index]
        self.image.fill("yellow")
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 1
        self.jump_speed = -10

    def import_character_assets(self):
        character_path = "guy.png"
        self.animations = {"idle":[], "run":[], "jump":[], "fall":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def apply_gravity(self):
        self.direction.y += self.gravity* 0.7
        self.rect.y += self.direction.y* 0.7
    
    def jump(self):
        self.direction.y = self.jump_speed
        
    def update(self):
        self.get_input()
        # self.rect.x += self.direction.x * self.speed*0.5
        # self.apply_gravity()