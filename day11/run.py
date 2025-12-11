from collections import defaultdict

import networkx as nx
from pathlib import Path
import sys

from runner import Runner


class DayRunner(Runner):
    def run1(self):
        graph = nx.DiGraph()

        for line in self.lines:
            node = line[:3]
            for other_node in line[5:].split(' '):
                graph.add_edge(node, other_node)

        return len(list(nx.all_simple_paths(graph, 'you', 'out')))

    def run2(self):
        graph = nx.DiGraph()

        for line in self.lines:
            node = line[:3]
            for other_node in line[5:].split(' '):
                graph.add_edge(node, other_node)

        def count(start, end):
            ordered_nodes = nx.topological_sort(graph)
            counts = defaultdict(int)
            counts[start] = 1
            for node in ordered_nodes:
                for child in graph.successors(node):
                    counts[child] += counts[node]
            return counts[end]

        first_part = count('svr', 'fft')
        seconde_part = count('fft', 'dac')
        third_part = count('dac', 'out')

        return first_part * seconde_part * third_part


if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    # print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
