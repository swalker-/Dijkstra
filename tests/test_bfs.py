__author__ = 'Stephen'

import unittest
from bfs import *

class TestBFS(unittest.TestCase):

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

        start = Point(0,0)
        end = Point(4,4)

        start2 = Point(2,2)

        graph_info_list = ((graph0, start, end), (graph1, start, end), (graph2, start, end),
                           (graph0, start2, end), (graph1, start2, end), (graph2, start2, end))

        shortest_distances = [8, 8, 16, 4, 8, 8]

        for counter in range(len(graph_info_list)):
            result = find_shortest_path(graph_info_list[counter])
            actual_distance = result[1]
            expected_distance = shortest_distances[counter]
            self.assertEquals(actual_distance, expected_distance)

if __name__ == '__main__':
    unittest.main()