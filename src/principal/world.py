from ..settings import ALTURA_TELA, CORES, LARGURA_TELA

class World:
  def __init__(self, screen) :
    self.screen = screen
    self.tile_size = 32  # Tamanho de cada tile
    self.num_tiles_x = LARGURA_TELA // self.tile_size
    self.num_tiles_y = ALTURA_TELA // self.tile_size

    self.map_grid = [
      [10, 1, 2, 0, 0, 0],
      [3, 4, 4, 5, 3, 2],
      [0, 1, 3, 3, 0, 2],
      [0, 1, 1, 1, 1, 2],
    ]

  def DrawMap(self):
    #executa antes dos metodos
    self.screen.fill(CORES['branco'])  # Limpa a tela

  # def DrawMonsterInMap(self, screen): 
  #   screen
