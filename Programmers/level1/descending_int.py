"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12933
"""
from common import print_solved


def solution(n):
    return int(
        "".join(sorted([num for num in str(n)], key=lambda x: int(x), reverse=True))
    )


if __name__ == "__main__":
    solutions = [solution(118372)]

    answers = [873211]

    print_solved(solutions, answers)
