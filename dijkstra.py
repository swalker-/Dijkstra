__author__ = 'Stephen'

import collections

Point = collections.namedtuple('Point', ['x', 'y'])
Data = collections.namedtuple('Data', ['graph', 'end_point', 'current_point', 'shortest_distance', 'path', 'shortest_paths'])

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

    # prep information to be packed into data tuple
    end_point = graph_tuple[2]
    current_point = graph_tuple[1]
    shortest_distance = float("inf")
    path = [current_point]
    shortest_paths = []
    data = Data(graph, end_point, current_point, shortest_distance, path, shortest_paths)
    return __calculate_distance(data)

def __calculate_distance(data):
    # unpack data tuple
    graph = data.graph
    current_point = data.current_point
    end_point = data.end_point
    shortest_distance = data.shortest_distance
    path = data.path
    shortest_paths = data.shortest_paths
    distance = graph[current_point.x][current_point.y]

    if current_point == end_point:
        if distance == shortest_distance:
            shortest_paths.append(path)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_paths = [path]
        return graph, shortest_distance, shortest_paths

    # If it is impossible for the current path to be shorter than
    # the current shortest path, stop searching
    if __not_shortest_path(distance, shortest_distance, current_point, end_point):
        return graph, shortest_distance, shortest_paths

    # Potential points to visit
    new_points = [Point(current_point.x+1, current_point.y), Point(current_point.x-1, current_point.y),
                  Point(current_point.x, current_point.y+1), Point(current_point.x, current_point.y-1)]

    # Depth first search
    for point in new_points:
        if __valid_point(point, graph, path):
            value = graph[point.x][point.y]
            if (value >= distance+1) or (value == 0):
                graph[point.x][point.y] = distance+1
                new_path = path.copy()
                new_path.append(point)
                new_data = Data(graph, end_point, point, shortest_distance, new_path, shortest_paths)
                graph, shortest_distance, shortest_paths = __calculate_distance(new_data)

    return graph, shortest_distance, shortest_paths

def __not_shortest_path(distance, shortest_distance, current_point, end_point):
    has_shortest_distance = not (shortest_distance == float("inf"))
    is_longer = (__best_distance(distance, current_point, end_point) > shortest_distance)
    return has_shortest_distance and is_longer

def __best_distance(distance, current_point, end_point):
    min_movement_x = abs(current_point.x - end_point.x)
    min_movement_y = abs(current_point.y - end_point.y)
    return distance+min_movement_x+min_movement_y

def __valid_point(point, graph, path):
    if (point.x >= 0) and (point.x < len(graph)):
        if (point.y >= 0) and (point.y < len(graph[0])):
            not_repeat_point = not (path.__contains__(point))
            valid_position = (graph[point.x][point.y] != -1)
            return not_repeat_point and valid_position
    return False

