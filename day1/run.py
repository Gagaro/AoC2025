import sys
from pathlib import Path

from runner import Runner


class Day1Runner(Runner):
    def run1(self):
        OPERATORS = {
            'L': -1,
            'R': 1,
        }

        count = 0
        dial = 50
        for line in self.lines:
            dial = (dial + OPERATORS[line[0]] * int(line[1:])) % 100
            if dial == 0:
                count += 1
        return count

    def run2(self):
        OPERATORS = {
            'L': -1,
            'R': 1,
        }

        count = 0
        dial = 50
        for line in self.lines:
            new_dial = dial + OPERATORS[line[0]] * int(line[1:])

            print(f'{dial=} {line} {new_dial=}')
            old_count = count

            if new_dial == 0:
                count += 1
            count += abs(new_dial // 100)
            if dial == 0 and new_dial < 0:
                count -= 1
            dial = new_dial % 100
            if dial == 0 and new_dial < 0:
                count += 1

            print(f'count += {count - old_count}')
            print(f'{dial=} {count=}\n')

        return count


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day1Runner(input_path).run1())
    print(Day1Runner(input_path).run2())
