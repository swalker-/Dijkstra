__author__ = 'Stephen'

import unittest
from dijkstra import *

class TestDijkstra(unittest.TestCase):

    def test_cases(self):
        graph0 = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        graph1 = [[0, 0, 0, 0, 0],
                  [0, 0, 0,-1, 0],
                  [0, 0, 0,-1, 0],
                  [0,-1,-1,-1, 0],
                  [0, 0, 0, 0, 0]]

        graph2 = [[0,-1, 0, 0, 0],
                  [0,-1, 0,-1, 0],
                  [0,-1, 0,-1, 0],
                  [0,-1, 0,-1, 0],
                  [0, 0, 0,-1, 0]]

        graph3 = [[0, 0, 0, 0, 0],
                  [0,-1,-1,-1, 0],
                  [0,-1, 0,-1, 0],
                  [0,-1,-1,-1, 0],
                  [0, 0, 0, 0, 0]]

        graph4 = [[0, 0, 0, 0, 0],
                  [0,-1,-1,-1, 0],
                  [0,-1, 0,-1, 0],
                  [0,-1, 0,-1, 0],
                  [0, 0, 0,-1, 0],
                  [0,-1,-1,-1, 0],
                  [0, 0, 0, 0, 0]]

        graph5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0]]

        start = Point(0,0)
        start2 = Point(2,2)
        end = Point(4,4)
        end2 = Point(4,6)
        end3 = Point(24, 20)

        graph_info_list = [(graph0, start, end), (graph1, start, end), (graph2, start, end),
                           (graph0, start2, end), (graph1, start2, end), (graph2, start2, end),
                           (graph3, start2, end), (graph4, start2, end2), (graph5, start, end3)]

        shortest_distances = [8, 8, 16, 4, 8, 8, float("inf"), 10, 44]
        num_paths = [5, 2, 1, 5, 2, 1, 0, 1, 5]

        for counter in range(len(graph_info_list)):
            result = find_shortest_path(graph_info_list[counter], 5)
            actual_distance = result[1]
            expected_distance = shortest_distances[counter]

            shortest_paths = result[2]
            actual_paths = len(shortest_paths)
            expected_paths = num_paths[counter]

            self.assertEquals(actual_distance, expected_distance)
            self.assertEquals(actual_paths, expected_paths)

if __name__ == '__main__':
    unittest.main()