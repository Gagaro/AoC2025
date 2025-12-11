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
        total_counts = 0
        for line in self.lines:
            # print(line)

            line = line.split(' ')
            buttons = list(map(lambda x: map(int, x[1:-1].split(',')), line[1:-1]))
            jolt_from_btn = {}
            for button_id, jolts in enumerate(buttons):
                for jolt in jolts:
                    jolt_from_btn.setdefault(jolt, []).append(button_id)

            joltages = list(map(int, line[-1][1:-1].split(',')))

            o = Optimize()

            count = Int('count')

            B = [Int(f'b{i}') for i in range(len(buttons))]
            for b in B:
                o.add(b >= 0)

            o.add(count == sum(B))

            for joltage, joltage_buttons in jolt_from_btn.items():
                o.add(joltages[joltage] == sum(B[button] for button in joltage_buttons))

            # (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
            # {3: [0, 1, 3], 1: [1, 5], 2: [2, 3, 4], 0: [4, 5]}

            # print(o)

            # [b0 >= 0,
            #  b1 >= 0,
            #  b2 >= 0,
            #  b3 >= 0,
            #  b4 >= 0,
            #  b5 >= 0,
            #  count == b0 + b1 + b2 + b3 + b4 + b5,
            #  0 + b0 + b1 + b3 == 7,
            #  0 + b1 + b5 == 5,
            #  0 + b2 + b3 + b4 == 4,
            #  0 + b4 + b5 == 3]

            o.minimize(count)
            o.check()
            total_counts += o.model()[count].as_long()

        return total_counts


if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    # print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
