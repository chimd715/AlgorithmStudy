"""
    programmers algorithm
    last solved: 2021.11.24
    url: https://programmers.co.kr/learn/courses/30/lessons/77485
"""
from common import print_solved


def solution(rows, columns, queries):
    matrix = [list(range(columns * i + 1, columns * (i + 1) + 1)) for i in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        moved = []
        temp = matrix[x1][y1]
        for i in range(y1+1, y2+1):
            moved.append(temp)
            matrix[x1][i], temp = temp, matrix[x1][i]
        for i in range(x1+1, x2+1):
            moved.append(temp)
            matrix[i][y2], temp = temp, matrix[i][y2]
        for i in range(y1, y2)[::-1]:
            moved.append(temp)
            matrix[x2][i], temp = temp, matrix[x2][i]
        for i in range(x1, x2)[::-1]:
            moved.append(temp)
            matrix[i][y1], temp = temp, matrix[i][y1]
        answer.append(min(moved))
    return answer


if __name__ == "__main__":
    solutions = [
        solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]),
        solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]),
        solution(100, 97, [[1, 1, 100, 97]])
    ]

    answers = [
        [8, 10, 25],
        [1, 1, 5, 3],
        [1]
    ]

    print_solved(solutions, answers)
