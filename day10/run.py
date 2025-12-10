from collections import deque
from pathlib import Path
import sys
from z3 import *

from runner import Runner


class DayRunner(Runner):
    def run1(self):
        counts = []
        for line in self.lines:
            # print(line)

            line = line.split(' ')
            lights_goal = {i for i, c in enumerate(line[0][1:-1]) if c == '#'}
            buttons = list(map(lambda x: set(map(int, x[1:-1].split(','))), line[1:-1]))

            queue = deque([[set()]])
            while queue:
                states = queue.popleft()
                state = states[-1]
                for button in buttons:
                    new_state = state ^ button
                    if new_state == lights_goal:
                        counts.append(len(states))
                        break
                    queue.append(states + [new_state])
                else:
                    continue
                break
        return sum(counts)

    def run2(self):
        for line in self.lines:
            print(line)

            line = line.split(' ')
            buttons = list(map(lambda x: set(map(int, x[1:-1].split(','))), line[1:-1]))
            joltages = line[-1][1:-1].split(',')



        return


if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    # print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
