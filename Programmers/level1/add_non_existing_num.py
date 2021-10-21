"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/86051
"""
from common import print_solved


def solution(numbers):
    sum_all_num = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
    sum_nums = sum(numbers)
    return sum_all_num - sum_nums


def solution_2(numbers):
    answer = 0
    all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in all_nums:
        if number not in numbers:
            answer += number
    return answer


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 4, 6, 7, 8, 0]),
        solution([5, 8, 4, 0, 6, 7, 9])
    ]

    answers = [
        14,
        6
    ]

    print_solved(solutions, answers)
