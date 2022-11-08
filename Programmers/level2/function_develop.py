"""
    programmers algorithm
    last solved: 2021.11.17
    url: https://programmers.co.kr/learn/courses/30/lessons/42586
"""
from common import print_solved


def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        count = 0
        for progress in progresses:
            if progress < 100:
                break
            count += 1

        for i in range(count):
            progresses.pop(0)
            speeds.pop(0)

        if count:
            answer.append(count)

    return answer


def solution_2(progresses, speeds):
    answer = []
    pos = 0
    while pos < len(progresses):
        count = 0
        is_continue = True
        for i in range(pos, len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] < 100:
                is_continue = False
            elif is_continue:
                count += 1

        if count:
            answer.append(count)
            pos += count

    return answer


if __name__ == "__main__":
    solutions = [
        solution([93, 30, 55], [1, 30, 5]),
        solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]),
        solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]),
        solution([96, 99, 98, 97], [1, 1, 1, 1]),
        solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]),
        solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]),
    ]

    answers = [[2, 1], [1, 3, 2], [3, 3], [4], [1, 2, 3], [2, 4]]

    print_solved(solutions, answers)
