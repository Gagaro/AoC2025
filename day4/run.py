import sys
from pathlib import Path

from runner import Runner


class Day4Runner(Runner):
    def run1(self):
        map = self.lines
        max_y = len(map)
        max_x = len(map[0])
        count = 0

        for y in range(max_y):
            for x in range(max_x):
                if map[y][x] != '@':
                    continue
                surrounding = (
                        (map[y - 1][max(0, x - 1): x + 2] if y - 1 >= 0 else '')
                        + map[y][max(0, x - 1): x + 2]
                        + (map[y + 1][max(0, x - 1): x + 2] if y + 1 < max_y else '')
                )
                if surrounding.count('@') < 5:
                    # print(map[y - 1][max(0, x - 1): x + 2] if y - 1 >= 0 else '')
                    # print(map[y][max(0, x - 1): x + 2])
                    # print(map[y + 1][max(0, x - 1): x + 2] if y + 1 < max_y else '')
                    # print(f'{x=} {y=} {surrounding=}')
                    count += 1
        return count

    def run2(self):
        map = self.lines
        max_y = len(map)
        max_x = len(map[0])
        count = 0
        new_map = None

        while new_map != map:
            if new_map is None:
                new_map = map.copy()
            else:
                map = new_map.copy()
            for y in range(max_y):
                for x in range(max_x):
                    if map[y][x] != '@':
                        continue
                    surrounding = (
                            (map[y - 1][max(0, x - 1): x + 2] if y - 1 >= 0 else '')
                            + map[y][max(0, x - 1): x + 2]
                            + (map[y + 1][max(0, x - 1): x + 2] if y + 1 < max_y else '')
                    )
                    if surrounding.count('@') < 5:
                        # print(map[y - 1][max(0, x - 1): x + 2] if y - 1 >= 0 else '')
                        # print(map[y][max(0, x - 1): x + 2])
                        # print(map[y + 1][max(0, x - 1): x + 2] if y + 1 < max_y else '')
                        # print(f'{x=} {y=} {surrounding=}')
                        new_map[y] = list(new_map[y])
                        new_map[y][x] = '.'
                        new_map[y] = ''.join(new_map[y])
                        count += 1
        return count


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day4Runner(input_path).run1())
    print(Day4Runner(input_path).run2())
