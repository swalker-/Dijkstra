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

graph3 = [[0, 0, 0, 0, 0],
          [0,-1,-1,-1, 0],
          [0,-1, 0,-1, 0],
          [0,-1,-1,-1, 0],
          [0, 0, 0, 0, 0]]

start = Point(0,0)
end = Point(4,4)
start2 = Point(2,2)
start3 = Point(0,3)

graph_info_list = [(graph0, start, end), (graph1, start, end), (graph2, start, end),
                   (graph0, start2, end), (graph1, start2, end), (graph2, start2, end),
                   (graph2, start3, end), (graph3, start2, end)]
for graph_info in graph_info_list:
    result = dijkstra.find_shortest_path(graph_info)

    new_graph = result[0]
    shortest_distance = result[1]
    shortest_paths = result[2]

    print("Start point: ", graph_info[1])
    print("End point: ", graph_info[2])
    print()

    for graph in graph_info[0]:
        for i in graph:
            print(repr(i).rjust(2), end=' ')
        print()
    print()
    for graph in new_graph:
        for i in graph:
            print(repr(i).rjust(2), end=' ')
        print()
    print()
    print("shortest distance: ", shortest_distance)
    print()
    print("# of paths: ", len(shortest_paths))
    if len(shortest_paths) > 10:
        print("(not displayed)")
    else:
        for p in shortest_paths:
            print(p)
            print()
    print("--------------------")
    print()
