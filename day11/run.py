from collections import defaultdict
from pathlib import Path
import sys

from runner import Runner


class DayRunner(Runner):
    def run1(self):
        return

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
