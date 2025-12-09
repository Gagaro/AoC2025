import math
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
import sys

import networkx

from runner import Runner


@dataclass(eq=True, frozen=True)
class JunctionBox:
    x: int
    y: int
    z: int

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)


class DayRunner(Runner):
    def run1(self):
        junction_boxes = [JunctionBox(*map(int, line.split(','))) for line in self.lines]
        graph = networkx.Graph()
        graph.add_nodes_from(junction_boxes)

        edges = sorted((
            (junction_box, second_junction_box, junction_box.distance(second_junction_box))
            for i, junction_box in enumerate(junction_boxes)
            for second_junction_box in junction_boxes[i + 1:]
        ), key=lambda x: x[2])
        graph.add_weighted_edges_from(edges[:1000 if not self.test else 10])
        graphes_lengths = sorted(
            (len(g) for g in networkx.connected_components(graph)),
            reverse=True,
        )
        return reduce(lambda x, y: x * y, graphes_lengths[:3])

    def run2(self):
        junction_boxes = [JunctionBox(*map(int, line.split(','))) for line in self.lines]
        graph = networkx.Graph()
        graph.add_nodes_from(junction_boxes)

        edges = sorted((
            (junction_box, second_junction_box, junction_box.distance(second_junction_box))
            for i, junction_box in enumerate(junction_boxes)
            for second_junction_box in junction_boxes[i + 1:]
        ), key=lambda x: x[2])
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
            if networkx.is_connected(graph):
                return edge[0].x * edge[1].x



if __name__ == '__main__':
    is_test = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if is_test:
        input_path = Path(__file__).parent / 'input_test.txt'
    else:
        input_path = Path(__file__).parent / 'input.txt'

    print(DayRunner(input_path, test=is_test).run1())
    print(DayRunner(input_path, test=is_test).run2())
