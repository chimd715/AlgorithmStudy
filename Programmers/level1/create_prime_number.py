"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/12977
"""
from common import print_solved


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in range(len(nums)):
        first_num = nums[i]
        for j in range(i+1, len(nums)):
            second_num = nums[j]
            for k in range(j+1, len(nums)):
                third_num = nums[k]

                answer += 1 if is_prime(first_num + second_num + third_num) else 0

    return answer


def solution_2(nums):
    from itertools import combinations

    answer = 0
    for three_nums in combinations(nums, 3):
        answer += 1 if is_prime(sum(three_nums)) else 0

    return answer


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 4]),
        solution([1, 2, 7, 6, 4])
    ]

    answers = [
        1,
        4
    ]

    print_solved(solutions, answers)
