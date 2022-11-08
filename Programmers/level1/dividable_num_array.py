"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12910
"""
from common import print_solved


def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    return sorted(answer) if answer else [-1]


def short_solution(arr, divisor):
    return [num for num in sorted(arr) if num % divisor == 0] or [-1]


if __name__ == "__main__":
    solutions = [
        solution([5, 9, 7, 10], 5),
        solution([2, 36, 1, 3], 1),
        solution([3, 2, 6], 10),
    ]

    answers = [[5, 10], [1, 2, 3, 36], [-1]]

    print_solved(solutions, answers)
