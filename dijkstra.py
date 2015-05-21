__author__ = 'Stephen'

import collections


Point = collections.namedtuple('Point', ['x', 'y'])
Data = collections.namedtuple('Data', ['graph', 'end_point', 'current_point', 'shortest_distance', 'path'])

# graph_tuple is (2D array, start point, end point)
def find_shortest_path(graph_tuple):
    temp_graph = graph_tuple[0]
    row = len(temp_graph)
    col = len(temp_graph[0])

    graph = [[0 for x in range(row)] for x in range(col)]
    for i in range(row):
        for j in range(col):
            if temp_graph[i][j] == -1:
                graph[i][j] = -1

    data = Data(graph, graph_tuple[2], graph_tuple[1], -1, [graph_tuple[1]])
    return calculate_distance(data)

def calculate_distance(data):
    # unpack data tuple
    graph = data.graph
    current_point = data.current_point
    end_point = data.end_point
    shortest_distance = data.shortest_distance
    path = data.path
    distance = graph[current_point.x][current_point.y]

    if current_point == end_point:
        shortest_distance = __shortest_distance(distance, shortest_distance)
        return graph, shortest_distance

    new_points = [Point(current_point.x+1, current_point.y), Point(current_point.x-1, current_point.y),
                  Point(current_point.x, current_point.y+1), Point(current_point.x, current_point.y-1)]
    for point in new_points:
        if __valid_point(point, graph, path):
            value = graph[point.x][point.y]
            if (value > distance+1) or (value == 0):
                graph[point.x][point.y] = distance+1
                new_path = path.copy()
                new_path.append(point)
                new_data = Data(graph, end_point, point, shortest_distance, new_path)
                graph, shortest_distance = calculate_distance(new_data)
    return graph, shortest_distance

def __valid_point(point, graph, path):
    if (point.x >= 0) and (point.x < len(graph)):
        if (point.y >= 0) and (point.y < len(graph[0])):
            not_repeat_point = not (path.__contains__(point))
            valid_position = (graph[point.x][point.y] != -1)
            return not_repeat_point and valid_position
    return False

def __shortest_distance(distance, shortest_distance):
    if shortest_distance == -1 or distance < shortest_distance:
        return distance
    return shortest_distance
