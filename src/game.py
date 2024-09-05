import pygame

from src.settings import LARGURA_TELA, ALTURA_TELA

pygame.init()
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
clock = pygame.time.Clock()

# Loop principal do jogo
running = True

class Game():
    def Run():
      running = True
      while running:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  running = False

          
          screen.fill((0, 0, 0)) # background preto
          # tile_map.draw(screen)
          pygame.display.flip()
          clock.tick(60)

      pygame.quit()