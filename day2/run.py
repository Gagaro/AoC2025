import sys
from pathlib import Path

from runner import Runner


class Day2Runner(Runner):
    def run1(self):
        numbers_ranges = self.lines[0]

        def get_numbers():
            for numbers_range in numbers_ranges.split(','):
                start, end = numbers_range.split('-')
                for number in map(str, range(int(start), int(end) + 1)):
                    number_length = len(number)
                    if number_length % 2 == 0 and number[:int(number_length / 2)] == number[int(number_length / 2):]:
                        yield int(number)

        return sum(number for number in get_numbers())

    def run2(self):
        numbers_ranges = self.lines[0]

        def get_numbers():
            for numbers_range in numbers_ranges.split(','):
                start, end = numbers_range.split('-')
                for number in map(str, range(int(start), int(end) + 1)):
                    number_length = len(number)
                    for pattern_length in range(1, int(number_length / 2) + 1):
                        if number_length % pattern_length != 0:
                            continue
                        if len(set(
                            number[x * pattern_length:(x + 1) * pattern_length]
                            for x in range(0, int(number_length / pattern_length))
                        )) == 1:
                            yield int(number)
                            break

        return sum(number for number in get_numbers())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    # print(Day2Runner(input_path).run1())
    print(Day2Runner(input_path).run2())
