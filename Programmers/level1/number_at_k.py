"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/42748
"""
from common import print_solved


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced_array = array[i-1:j]
        sorted_sliced_array = sorted(sliced_array)
        answer.append(sorted_sliced_array[k-1])

    return answer


def short_solution(array, commands):
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]


if __name__ == "__main__":
    solutions = [
        solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    ]

    answers = [
        [5, 6, 3]
    ]

    print_solved(solutions, answers)
