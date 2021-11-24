"""
    programmers algorithm
    last solved: 2021.11.24
    url: https://programmers.co.kr/learn/courses/30/lessons/43165
"""
from common import print_solved


def solution(numbers, target):
    from itertools import combinations

    answer = 0
    for i in range(len(numbers)):
        for c in combinations(numbers, i):
            nums = numbers.copy()
            for item in c:
                nums.remove(item)
                nums.append(-item)
            if sum(nums) == target:
                answer += 1
    return answer


if __name__ == "__main__":
    solutions = [
        solution([1, 1, 1, 1, 1], 3)
    ]

    answers = [
        5
    ]

    print_solved(solutions, answers)
