"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/77884
"""
from common import print_solved


def find_all_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisors = find_all_divisors(i)
        answer += i if len(divisors) % 2 == 0 else -1 * i
    return answer


if __name__ == "__main__":
    solutions = [solution(13, 17), solution(24, 27)]

    answers = [43, 52]

    print_solved(solutions, answers)
