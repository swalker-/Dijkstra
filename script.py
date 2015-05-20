__author__ = 'Stephen'

import dijkstra
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

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

graph_info_list = [(graph0, start, end), (graph1, start, end), (graph2, start, end)]
for graph_info in graph_info_list:
    result = dijkstra.find_shortest_path(graph_info)

    new_graph = result[0]
    shortest_path = result[1]

    for list in graph_info[0]:
        for i in list:
            print(repr(i).rjust(2), end=' ')
        print()
    print()
    for list in new_graph:
        for i in list:
            print(repr(i).rjust(2), end=' ')
        print()
    print()
    print("shortest path: ", shortest_path)
    print()
    print("--------------------")
    print()
