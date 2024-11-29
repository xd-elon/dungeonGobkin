import pygame
from .principal.world import World  # Certifique-se de que o caminho esteja correto
from .settings import LARGURA_TELA, ALTURA_TELA, FPS

pygame.init()
pygame.display.set_caption("Meu Jogo")
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.world = World(screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.world.DrawMap()  # Desenha o mundo

            pygame.display.flip()  # Atualiza a tela
            clock.tick(FPS)  # Limita a 60 FPS

        pygame.quit()