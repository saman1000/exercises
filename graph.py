from typing import List
from collections import deque

def shortest_distance(roads, start, destination):
    # TODO: implement
    if start == destination:
        return 0
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        city, distance = queue.popleft()
        if city == destination:
            return distance
        if city not in visited:
            visited.add(city)
            if roads[city]:
                for neighbor in roads[city]:
                    queue.extend([(neighbor, distance + 1)])

    return None

def find_vertices_within_distance(graph, start, distance):
    # TODO: Implement the breadth-first search algorithm to find all vertices within a given distance.
    visited = set()
    queue = deque([(start, 0)])
    vertices_within_distance = []
    while queue:
        vertice, vertice_distance = queue.popleft()
        if 0 < vertice_distance <= distance:
            vertices_within_distance.append(vertice)
        if vertice not in visited:
            visited.add(vertice)
            if graph.get(vertice):
                for adjacent in graph[vertice]:
                    queue.extend([(adjacent, vertice_distance + 1)])
    return vertices_within_distance

def shortest_route_greedy(distance: int, stride_length: int, obstacles: List[int]) -> int:
    # TODO: implement the function
    goal = distance - 1
    if goal in obstacles:
        return -1
    index = 0
    steps = 0
    while index != goal:
        next_target = index + stride_length
        while next_target in obstacles or next_target > goal:
            next_target -= 1
            if next_target == index:
                return -1
        index = next_target
        steps += 1
    return steps

def shortest_route(distance: int, stride_length: int, obstacles: List[int]) -> int:
    # TODO: implement the function
    goal = distance - 1
    if goal in obstacles:
        return -1
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        start, steps = queue.popleft()
        for stride in range(1, stride_length + 1):
            next_goal = start + stride
            if next_goal == goal:
                return steps + 1
            if next_goal not in obstacles and next_goal not in visited:
                queue.append((next_goal, steps + 1))
                visited.add(next_goal)
    return -1

def bfs_matrix(mat, start, end):
    # TODO: implement
    num_columns = len(mat[0])
    num_rows = len(mat)
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        point, steps = queue.popleft()
        if point == end:
            return steps
        if point not in visited and mat[point[0]][point[1]] == 1:
            visited.add(point)
            for one_point in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
                if 0 <= one_point[0] < num_rows and 0 <= one_point[1] < num_columns:
                    if one_point not in visited and mat[point[0]][point[1]] == 1:
                        queue.append((one_point, steps + 1))
    return 0


def knight_moves(board, start, end):
    """
    Your task is to write a function that calculates the minimum number of moves
    it would take for a knight to get from `start` to `end` on a chessboard.

    :param board: 2D array representing the chess board
    :param start: a tuple (x,y) representing the starting cell on the board
    :param end: a tuple (x,y) representing the end cell on the board

    :return: minimum number of steps required for a knight to reach from start to end
    """

    # TODO: implement the function
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        cell, moves = queue.popleft()
        if cell == end:
            return moves
        if cell not in visited:
            visited.add(cell)
            queue.extend((one_cell, moves + 1) for one_cell in get_possible_knight_moves(cell) if is_on_chess_board(board, one_cell) and one_cell not in visited)
    return -1

def get_possible_knight_moves(cell):
    row = cell[0]
    col = cell[1]
    return [
        (row + 2, col + 1),
        (row + 2, col - 1),
        (row - 2, col + 1),
        (row - 2, col - 1),
        (row + 1, col + 2),
        (row + 1, col - 2),
        (row - 1, col + 2),
        (row - 1, col - 2),
    ]

def is_on_chess_board(board, cell):
    return 0 <= cell[0] < len(board) and 0 <= cell[1] < len(board[0])


if __name__ == "__main__":
    print(knight_moves([[0]*8 for _ in range(8)], (4, 4), (6, 6))) # 4
