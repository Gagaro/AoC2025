import sys
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

from runner import Runner

@dataclass
class FreshIngredientRange:
    start_range: int
    end_range: int

    def is_fresh(self, ingredient_id):
        return self.start_range <= ingredient_id <= self.end_range


class Day5Runner(Runner):
    def run1(self):
        fresh_ingredient_ranges = []

        while self.lines:
            ranges = self.lines.pop(0)
            if not ranges:
                break
            fresh_ingredient_ranges.append(FreshIngredientRange(*map(int, ranges.split('-'))))

        count = 0
        for line in self.lines:
            ingredient = int(line)
            for fresh_ingredient_range in fresh_ingredient_ranges:
                if fresh_ingredient_range.is_fresh(ingredient):
                    count += 1
                    break
        return count

    def run2(self):
        fresh_ingredient_ranges = []

        while self.lines:
            ranges = self.lines.pop(0)
            if not ranges:
                break
            fresh_ingredient_ranges.append(FreshIngredientRange(*map(int, ranges.split('-'))))

        fresh_ingredient_ranges = sorted(fresh_ingredient_ranges, key=lambda range: range.start_range)
        current_index = 0
        while current_index < len(fresh_ingredient_ranges) - 1:
            first_ingredient_range = fresh_ingredient_ranges[current_index]
            second_ingredient_range = fresh_ingredient_ranges[current_index + 1]
            if first_ingredient_range.end_range >= second_ingredient_range.start_range:
                fresh_ingredient_ranges[current_index] = FreshIngredientRange(
                    first_ingredient_range.start_range,
                    max(first_ingredient_range.end_range, second_ingredient_range.end_range)
                )
                fresh_ingredient_ranges.pop(current_index + 1)
            else:
                current_index += 1
        return reduce(
            lambda count, ingredient_range: count + ingredient_range.end_range - ingredient_range.start_range + 1,
            fresh_ingredient_ranges,
            0
        )


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(Day5Runner(input_path).run1())
    print(Day5Runner(input_path).run2())
