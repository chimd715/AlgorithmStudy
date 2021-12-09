"""
    programmers algorithm
    last solved: 2021.12.9
    url: https://programmers.co.kr/learn/courses/30/lessons/42746
"""
from common import print_solved


def solution(numbers):
    str_nums = list(map(str, numbers))
    max_char_len = max([len(num) for num in str_nums])
    str_nums.sort(key=lambda x: (x * max_char_len), reverse=True)

    return ''.join(str_nums)


if __name__ == "__main__":
    solutions = [
        solution([6, 10, 2]),
        solution([3, 30, 34, 5, 9])
    ]

    answers = [
        "6210",
        "9534330"
    ]

    print_solved(solutions, answers)
