"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12943
"""
from common import print_solved


def collatz(num, count=0):
    if count >= 500:
        return -1
    if num == 1:
        return count

    return (
        collatz(num / 2, count + 1) if num % 2 == 0 else collatz(num * 3 + 1, count + 1)
    )


def solution(num):
    return collatz(num)


if __name__ == "__main__":
    solutions = [solution(6), solution(16), solution(626331)]

    answers = [8, 4, -1]

    print_solved(solutions, answers)
