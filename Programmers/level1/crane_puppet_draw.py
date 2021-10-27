"""
    programmers algorithm
    last solved: 2021.10.27
    url: https://programmers.co.kr/learn/courses/30/lessons/64061
"""
from common import print_solved


def pop_item(board, x, y):
    item = board[y][x]
    board[y][x] = 0
    return board, item


def solution(board, moves):
    board = board[::-1]
    answer = 0

    pop_container = []
    for move in moves:
        x = move - 1
        for y in range(len(board))[::-1]:
            board, popped_item = pop_item(board, x, y)
            if not popped_item:
                continue

            last_popped_item = pop_container[-1] if pop_container else 0
            if popped_item == last_popped_item:
                pop_container = pop_container[:-1]
                answer += 1
            else:
                pop_container.append(popped_item)
            break

    return answer * 2


if __name__ == "__main__":
    solutions = [
        solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
    ]

    answers = [
        4
    ]

    print_solved(solutions, answers)
