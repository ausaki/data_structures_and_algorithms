import math

class Tile:
    def __init__(self, top, bottom, left, right, tile_id) -> None:
        self.top, self.bottom, self.left, self.right = top, bottom, left, right
        self.tile_id = tile_id

    @classmethod
    def from_matrix(cls, tile_id, tile):
        top = tile[0]
        bottom = tile[-1]
        left = ''.join(t[0] for t in tile)
        right = ''.join(t[-1] for t in tile)
        return cls(top, bottom, left, right, tile_id)

    def rotate(self):
        self.top, self.bottom, self.left, self.right = self.left[::-1], self.right[::-1], self.bottom, self.top
    
    def flipv(self):
        self.top, self.bottom, self.left, self.right = self.bottom, self.top, self.left[::-1], self.right[::-1]

    def fliph(self):
        self.top, self.bottom, self.left, self.right = self.top[::-1], self.bottom[::-1], self.right, self.left

    def copy(self):
        return Tile(self.top, self.bottom, self.left, self.right, self.tile_id)

    def __str__(self) -> str:
        return f'{self.tile_id}: {self.top} , {self.bottom} , {self.left} , {self.right}'

def solution(img, tiles):
    m = 12
    n = len(img)
    if n == len(tiles):
        return img[0].tile_id * img[m - 1].tile_id * img[-1].tile_id * img[-m].tile_id
    i, j = divmod(n, m)
    left = img[-1].right if j > 0 else None
    top = img[n - m].bottom if i > 0 else None
    for i, tile in enumerate(tiles):
        if tile is None:
            continue
        t = tile.copy()
        img.append(t)
        tiles[i] = None
        for _ in range(4):
            if (left is None or t.left == left) and (top is None or t.top == top):
                res = solution(img, tiles)
                if res:
                    return res
            t.rotate()
        t.fliph()
        for _ in range(4):
            if (left is None or t.left == left) and (top is None or t.top == top):
                res = solution(img, tiles)
                if res:
                    return res
            t.rotate()
        img.pop()
        tiles[i] = tile
    return 0


def solution2()

def main():
    tiles = []
    tile = None
    while True:
        line = input().strip()
        if line == 'end':
            break
        if not line:
            continue
        if line.startswith('Tile'):
            tile_id = int(line[5:-1])
            tile = []
            tiles.append([tile_id, tile])
            continue
        tile.append(line)
    tiles = [Tile.from_matrix(*tile) for tile in tiles]
    img = []
    print(solution(img, tiles))

main()