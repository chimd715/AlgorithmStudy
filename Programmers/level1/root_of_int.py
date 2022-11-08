"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12934
"""
from common import print_solved
from math import sqrt


def solution(n):
    float_sqrt = int(sqrt(n))
    if float_sqrt * float_sqrt == n:
        return (float_sqrt + 1) * (float_sqrt + 1)
    return -1


if __name__ == "__main__":
    solutions = [solution(121), solution(3)]

    answers = [144, -1]

    print_solved(solutions, answers)
