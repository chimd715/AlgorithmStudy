"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12906
"""
from common import print_solved


def solution(arr):
    answer = []
    current_num = -1
    for num in arr:
        if num != current_num:
            answer.append(num)
            current_num = num

    return answer


def short_solution(arr):
    return [num for i, num in enumerate(arr) if num != arr[i - 1] or i == 0]


if __name__ == "__main__":
    solutions = [solution([1, 1, 3, 3, 0, 1, 1]), solution([4, 4, 4, 3, 3])]

    answers = [[1, 3, 0, 1], [4, 3]]

    print_solved(solutions, answers)
