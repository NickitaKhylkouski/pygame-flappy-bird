import pygame
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.points = 0
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"{self.points}", True, (255, 255, 255))
        self.rect = self.image.get_rect()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"{self.points}", True, (255, 255, 255))