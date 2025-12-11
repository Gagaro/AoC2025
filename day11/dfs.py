from functools import lru_cache
from math import prod

FILENAME = "C:\\Users\\Gagaro\\PycharmProjects\\AoC2025\\day11\\input.txt"


def parse_input(filename):
    with open(filename, "r") as input_file:
        return {
            line[:3]: line[5:].split(" ") for line in input_file.read().splitlines()
        }


def count_paths(graph, start, end):
    @lru_cache(None)
    def dfs(node):
        if end == node:
            return 1
        return sum(dfs(neighbor) for neighbor in graph[node])
    return dfs(start)


def part_two(graph, paths):
    return max(
        prod(count_paths(graph, start, end) for start, end in zip(path, path[1:]))
        for path in paths
    )


def main():
    data = parse_input(FILENAME)
    data["out"] = []
    print(count_paths(data, "you", "out"))
    print(part_two(data, [["svr", "fft", "dac", "out"], ["svr", "dac", "fft", "out"]]))


if __name__ == "__main__":
    main()
