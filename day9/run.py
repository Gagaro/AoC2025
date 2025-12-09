from dataclasses import dataclass
from pathlib import Path
import sys

from shapely import Polygon

from runner import Runner


@dataclass(eq=True, frozen=True)
class Tile:
    x: int
    y: int

    def area(self, other_tile: 'Tile') -> int:
        return (abs(self.x - other_tile.x) + 1) * (abs(self.y - other_tile.y) + 1)


class DayRunner(Runner):
    def run1(self):
        tiles = [Tile(*map(int, line.split(','))) for line in self.lines]
        max_area = 0
        for index, tile in enumerate(tiles):
            for second_tile in tiles[index + 1:]:
                max_area = max(max_area, tile.area(second_tile))
        return max_area

    def run2(self):
        tiles = [Tile(*map(int, line.split(','))) for line in self.lines]
        polygon = Polygon([(tile.x, tile.y) for tile in tiles])
        max_area = 0
        for index, tile in enumerate(tiles):
            for second_tile in tiles[index + 1:]:
                square = Polygon(
                    ((tile.x, tile.y), (tile.x, second_tile.y),
                     (second_tile.x, second_tile.y), (second_tile.x, tile.y))
                )
                if polygon.covers(square):
                    max_area = max(max_area, tile.area(second_tile))
        return max_area


if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
