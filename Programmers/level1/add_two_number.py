"""
    programmers algorithm
    last solved: 2021.10.24
    url: https://programmers.co.kr/learn/courses/30/lessons/68644
"""
from common import print_solved


def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.add(numbers[i] + numbers[j])
    return sorted(list(answer))


def short_solution(numbers):
    answer = [numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i != j]
    return sorted(list(set(answer)))


def solution_2(numbers):
    from itertools import combinations
    answer = [i + j for i, j in combinations(numbers, 2)]
    return sorted(list(set(answer)))


if __name__ == "__main__":
    solutions = [
        solution([2, 1, 3, 4, 1]),
        solution([5, 0, 2, 7])
    ]

    answers = [
        [2, 3, 4, 5, 6, 7],
        [2, 5, 7, 9, 12]
    ]

    print_solved(solutions, answers)
