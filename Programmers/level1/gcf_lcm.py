"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12940
"""
from common import print_solved


def find_gcf(n, m, lcm):
    gcf = lcm
    while gcf < n * m and (gcf % n != 0 or gcf % m != 0):
        gcf += lcm
    return gcf


def find_lcm(n, m):
    divisors = [i for i in range(1, min(n, m) + 1) if n % i == 0 and m % i == 0]
    return max(divisors)


def solution(n, m):
    lcm = find_lcm(n, m)
    gcf = find_gcf(n, m, lcm)
    return [lcm, gcf]


if __name__ == "__main__":
    solutions = [
        solution(3, 12),
        solution(2, 5)
    ]

    answers = [
        [3, 12],
        [1, 10]
    ]

    print_solved(solutions, answers)
