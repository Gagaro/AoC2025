from collections import defaultdict
from pathlib import Path
import sys

from runner import Runner


class Day6Runner(Runner):
    def run1(self):
        lazers = set()
        first_line = self.lines.pop(0)

        lazers.add(first_line.find('S'))
        count = 0
        for line in self.lines:
            for mirror in (i for i, letter in enumerate(line) if letter == '^'):
                if mirror in lazers:
                    lazers.remove(mirror)
                    lazers.add(mirror + 1)
                    lazers.add(mirror - 1)
                    count += 1
        return count

    def run2(self):
        lazers = defaultdict(int)
        first_line = self.lines.pop(0)

        lazers[first_line.find('S')] = 1
        for line in self.lines:
            for mirror in (i for i, letter in enumerate(line) if letter == '^'):
                if mirror in lazers:
                    count = lazers[mirror]
                    del lazers[mirror]
                    lazers[mirror - 1] += count
                    lazers[mirror + 1] += count
        return sum(count for count in lazers.values())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day6Runner(input_path).run1())
    print(Day6Runner(input_path).run2())
