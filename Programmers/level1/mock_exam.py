"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/81301
"""
from common import print_solved


def check_answer(answer_sheet, real_answer, problem_num):
    return real_answer == answer_sheet[problem_num % len(answer_sheet)]


def solution(answers):
    correct_problem_list = [[], [], []]
    for i, answer in enumerate(answers):
        if check_answer([1, 2, 3, 4, 5], answer, i):
            correct_problem_list[0].append(i)
        if check_answer([2, 1, 2, 3, 2, 4, 2, 5], answer, i):
            correct_problem_list[1].append(i)
        if check_answer([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answer, i):
            correct_problem_list[2].append(i)

    max_score = max([len(_list) for _list in correct_problem_list])
    return [i+1 for i, _list in enumerate(correct_problem_list) if len(_list) == max_score]


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 4, 5]),
        solution([1, 3, 2, 4, 2])
    ]

    answers = [
        [1],
        [1, 2, 3]
    ]

    print_solved(solutions, answers)
