"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/76501
"""
from common import print_solved


def solution(absolutes, signs):
    answer = 0
    for i, num in enumerate(absolutes):
        answer += num if signs[i] else -1 * num
    return answer


if __name__ == "__main__":
    solutions = [
        solution([4, 7, 12], [True, False, True]),
        solution([1, 2, 3], [False, False, True])
    ]

    answers = [
        9,
        0
    ]

    print_solved(solutions, answers)
