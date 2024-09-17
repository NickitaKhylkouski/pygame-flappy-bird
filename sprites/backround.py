import pygame
class City(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/city.png")
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/road.png")
        self.image1 = pygame.image.load(r"assets/images/road.png")
        self.rect1 = self.image1.get_rect()
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.bottomleft = surface.get_rect().bottomleft
        self.rect.y += 25
        self.rect1.bottomleft = self.rect.bottomright
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)
    def update(self, surface):
        self.rect.x -= 5
        self.rect1.x -= 5
        if self.rect.right < 0:
            self.rect.midleft = self.rect1.midright
        if self.rect1.right < 0:
            self.rect1.midleft = self.rect.midright

