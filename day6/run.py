from functools import reduce

import numpy as np
from pathlib import Path
import sys

from runner import Runner


class Day6Runner(Runner):
    def run1(self):
        operations = self.lines.pop().split()
        numbers = np.array([line.split() for line in self.lines], np.int32)

        numbers_to_add = numbers[:, [operation == '+' for operation in operations]]
        numbers_to_multiply = numbers[:, [operation == '*' for operation in operations]]

        return np.add.reduce(numbers_to_add).sum() + np.multiply.reduce(numbers_to_multiply).sum()

    def run2(self):
        operations = self.lines.pop().split()

        numbers = list(map(lambda x: ''.join(x).strip(), list(zip(*self.lines))))

        count = 0
        while numbers:
            try:
                index = numbers.index('')
                number_list = numbers[:index]
                numbers = numbers[index + 1:]
            except ValueError:
                number_list = numbers
                numbers = []
            operator = operations.pop(0)
            if operator == '+':
                count += sum(map(int, number_list))
            else:
                count += reduce(lambda x, y: x * y, map(int, number_list))
        return count


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day6Runner(input_path).run1())
    print(Day6Runner(input_path).run2())
