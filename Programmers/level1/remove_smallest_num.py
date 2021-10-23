"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12935
"""
from common import print_solved


def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


if __name__ == "__main__":
    solutions = [
        solution([4, 3, 2, 1]),
        solution([10])
    ]

    answers = [
        [4, 3, 2],
        [-1]
    ]

    print_solved(solutions, answers)
