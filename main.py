import pygame
import sys
from sprites.backround import City
from sprites.backround import Road
from sprites.bird import Bird
from sprites.pipes import Pipe
import time
from sprites.game import Score
pygame.init()

# Константы/Constants
WIDTH = 288
HEIGHT = 512
FPS = 60


# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


def main():
    # Спрайты/Sprites
    city = City()
    road = Road()
    player = Bird()
    pipes = pygame.sprite.Group()
    pipes.add(Pipe())
    score = Score()
    game_over = False
    checkpoint = False
    running = True
    time.sleep(5)
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for pipe in pipes:
            if (pipe.rect1.collidepoint(player.rect.midbottom) or pipe.rect2.collidepoint(player.rect.midtop)) and not game_over:
                game_over = True
        if (player.rect.bottom > road.rect.top or player.rect.top < city.rect.top) and not game_over:
            game_over = True
            sound_wing = pygame.mixer.Sound(r"assets/sounds/hit.wav")
            sound_wing.play()

        # Рендеринг/Rendering
        if pipes.sprites()[0].rect1.x < player.rect.x and not checkpoint:
            score.points +=1
            checkpoint = True
            sound_wing = pygame.mixer.Sound(r"assets/sounds/point.wav")
            sound_wing.play()
        city.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        road.draw(screen)
        player.draw(screen)
        score.draw(screen)
        # Обновление спрайтов/Updating sprites
        if not game_over:
            road.update(screen)
            player.update()
            pipes.update()
        if len(pipes) < 1:
            pipes.add(Pipe())
            checkpoint = False

        # Обновление экрана/Screen Refresh
        pygame.display.update()


if __name__ == "__main__":
    main()




