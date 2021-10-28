"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/86491
"""
from common import print_solved


def solution(sizes):
    max_w = max([max(w, h) for w, h in sizes])
    max_h = max([min(w, h) for w, h in sizes])
    return max_w * max_h


if __name__ == "__main__":
    solutions = [
        solution([[60, 50], [30, 70], [60, 30], [80, 40]]),
        solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]),
        solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
    ]

    answers = [
        4000,
        120,
        133
    ]

    print_solved(solutions, answers)
