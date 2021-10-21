"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/67256
"""
from common import print_solved
from collections import deque


def measure_distance(origin_position, target_position):
    def get_int_node(node):
        if node == '*':
            return 10
        elif node == '#':
            return 11
        return int(node)

    nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '#']
    edges = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8', '*'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8', '#'],
        '0': ['*', '#', '8'],
        '*': ['7', '0'],
        '#': ['0', '9']
    }

    to_visit_nodes = deque()
    to_visit_nodes.append(origin_position)

    visited_nodes = []
    distances = [0] * 12
    while to_visit_nodes:
        current_node = to_visit_nodes.popleft()
        visited_nodes.append(current_node)
        for edge in edges[current_node]:
            if edge in visited_nodes:
                continue

            edge_pos = get_int_node(edge)
            current_node_pos = get_int_node(current_node)
            if distances[edge_pos] == 0:
                distances[edge_pos] = distances[current_node_pos] + 1
            else:
                distances[edge_pos] = min(distances[edge_pos], distances[current_node_pos] + 1)

            to_visit_nodes.append(edge)
    return distances[get_int_node(target_position)]


def solution(numbers, hand):
    left_push = ['1', '4', '7']
    right_push = ['3', '6', '9']

    answer = ''
    left_position = '*'
    right_position = '#'
    for number in numbers:
        number = str(number)
        if number in left_push:
            left_position = number
            answer += 'L'
        elif number in right_push:
            right_position = number
            answer += 'R'
        else:
            left_distance = measure_distance(left_position, number)
            right_distance = measure_distance(right_position, number)

            if right_distance > left_distance:
                left_position = number
                answer += 'L'
            elif right_distance < left_distance:
                right_position = number
                answer += 'R'
            elif left_distance == right_distance and hand == "right":
                right_position = number
                answer += 'R'
            elif left_distance == right_distance and hand == "left":
                left_position = number
                answer += 'L'

    return answer


if __name__ == "__main__":
    solutions = [
        solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"),
        solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"),
        solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"),
    ]

    answers = [
        "LRLLLRLLRRL",
        "LRLLRRLLLRR",
        "LLRLLRLLRL"
    ]

    print_solved(solutions, answers)
