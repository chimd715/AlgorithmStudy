"""
    programmers algorithm
    last solved: 2021.10.27
    url: https://programmers.co.kr/learn/courses/30/lessons/42862
"""
from common import print_solved


def solution(n, lost, reserve):
    people = [0] * (n+2)
    for index in lost:
        people[index] -= 1

    for index in reserve:
        people[index] += 1

    for i, person in enumerate(people):
        if person < 0:
            if people[i-1] > 0:
                people[i-1] -= 1
                people[i] += 1
            elif people[i+1] > 0:
                people[i+1] -= 1
                people[i] += 1

    people[0] = 0
    people[-1] = 0
    answer = 0
    for person in people:
        if person >= 0:
            answer += 1
    return answer - 2


def solution_2(n, lost, reserve):
    _lost = [_l for _l in sorted(lost) if _l not in reserve]
    _reserve = [_r for _r in reserve if _r not in lost]

    answer = n - len(_lost)
    for _l in _lost:
        if _l-1 in _reserve:
            _reserve.remove(_l-1)
            answer += 1
        elif _l+1 in _reserve:
            _reserve.remove(_l+1)
            answer += 1

    return answer


if __name__ == "__main__":
    solutions = [
        solution(5, [2, 4], [1, 3, 5]),
        solution(5, [2, 4], [3]),
        solution(5, [2, 4, 5], [3, 5]),
        solution(3, [3], [1])
    ]

    answers = [
        5,
        4,
        4,
        2
    ]

    print_solved(solutions, answers)
