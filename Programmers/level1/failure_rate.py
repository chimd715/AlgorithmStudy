"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/42889
"""
from common import print_solved
from collections import Counter


def solution(N, stages):
    failure_rate = {}
    users = Counter(stages)
    total_people = len(stages)
    for i in range(1, N + 1):
        failure_rate[i] = users[i] / total_people if total_people != 0 else 0
        total_people -= users[i]

    return sorted(
        list(failure_rate.keys()), key=lambda x: failure_rate[x], reverse=True
    )


if __name__ == "__main__":
    solutions = [solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), solution(4, [4, 4, 4, 4, 4])]

    answers = [[3, 4, 2, 1, 5], [4, 1, 2, 3]]

    print_solved(solutions, answers)
