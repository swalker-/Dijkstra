__author__ = 'Stephen'

import collections


Point = collections.namedtuple('Point', ['x', 'y'])

def find_shortest_path(graph_tuple):
    temp_graph = graph_tuple[0]
    row = len(temp_graph)
    col = len(temp_graph[0])

    graph = [[0 for x in range(row)] for x in range(col)]
    for i in range(row):
        for j in range(col):
            if temp_graph[i][j] == -1:
                graph[i][j] = -1

    return calculate_distance(graph, graph_tuple[2], graph_tuple[1], -1, [graph_tuple[1]])

def __valid_point(point, graph, path):
    if (point.x >= 0) and (point.x < len(graph)):
        if (point.y >= 0) and (point.y < len(graph[0])):
            not_repeat_point = not (path.__contains__(point))
            valid_position = (graph[point.x][point.y] != -1)
            return not_repeat_point and valid_position
    return False

def calculate_distance(graph, end_point, current_point, shortest_distance, path):
    distance = graph[current_point.x][current_point.y]
    if current_point == end_point:
        if shortest_distance == -1:
            shortest_distance = distance
        elif distance<shortest_distance:
            shortest_distance = distance
        return (graph, shortest_distance)
    points = [Point(current_point.x+1, current_point.y), Point(current_point.x-1, current_point.y),
              Point(current_point.x, current_point.y+1), Point(current_point.x, current_point.y-1)]
    for new_point in points:
        if __valid_point(new_point, graph, path):
            value = graph[new_point.x][new_point.y]
            if (value > distance+1) or (value == 0):
                graph[new_point.x][new_point.y] = distance+1
                new_path = path.copy()
                new_path.append(new_point)
                (g, s) = calculate_distance(graph, end_point, new_point, shortest_distance, new_path)
                graph = g
                shortest_distance = s

    return (graph, shortest_distance)
