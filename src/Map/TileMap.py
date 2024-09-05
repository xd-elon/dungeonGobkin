class TileMap:
    def __init__(self, grid, tiles, tile_size):
        self.grid = grid
        self.tiles = tiles
        self.tile_size = tile_size

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, tile_id in enumerate(row):
                tile_image = self.tiles.get(tile_id)
                if tile_image:
                    screen.blit(tile_image, (x * self.tile_size, y * self.tile_size))


# Definir tiles e mapa
tiles = {
    0: pygame.image.load('grass.png'),
    1: pygame.image.load('wall.png'),
    2: pygame.image.load('water.png'),
    3: pygame.image.load('sand.png'),
}
map_grid = [
    [1, 1, 1, 2, 2, 2],
    [1, 0, 0, 2, 0, 2],
    [1, 0, 3, 3, 0, 2],
    [1, 1, 1, 1, 1, 2],
]
tile_map = TileMap(map_grid, tiles, 32)