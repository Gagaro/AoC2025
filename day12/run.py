from pathlib import Path
import sys

from runner import Runner


class DayRunner(Runner):
    def run1(self):
        presents_areas = [5, 7, 7, 7, 6, 7]
        count = 0
        for line in self.lines[30:]:
            area = int(line[:2]) * int(line[3:5])
            needed_area = sum(a * b for a, b in zip(presents_areas, map(int, line[7:].split())))
            if area >= needed_area:
                count += 1
        return count

    def run2(self):
        return


if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
