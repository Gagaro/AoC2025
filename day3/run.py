import sys
from pathlib import Path

from runner import Runner


class Day3Runner(Runner):
    def run1(self):
        def get_voltages():
            for bank in self.lines:
                first_digit = max(bank[:-1])
                bank = bank[bank.find(first_digit) + 1:]
                second_digit = max(bank)
                max_number = int(f'{first_digit}{second_digit}')
                yield max_number
        return sum(voltage for voltage in get_voltages())

    def run2(self):
        def get_voltages():
            for bank in self.lines:
                max_number = ''
                current_index = 0
                for i in range(11, -1, -1):
                    current_bank = bank[current_index:-i if i > 0 else None]
                    digit = max(current_bank)
                    current_index = current_index + current_bank.find(digit) + 1
                    max_number += digit
                yield int(max_number)

        return sum(voltage for voltage in get_voltages())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day3Runner(input_path).run1())
    print(Day3Runner(input_path).run2())
