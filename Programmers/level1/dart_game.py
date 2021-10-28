"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/17682
"""
from common import print_solved


def solution(dartResult):
    scores = []
    temp = ''
    for char in dartResult:
        if char == 'S':
            scores.append(int(temp))
            temp = ""
            scores[-1] = scores[-1]
        elif char == 'D':
            scores.append(int(temp))
            temp = ""
            scores[-1] = scores[-1] * scores[-1]
        elif char == 'T':
            scores.append(int(temp))
            temp = ""
            scores[-1] = scores[-1] * scores[-1] * scores[-1]
        elif char == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif char == '#':
            scores[-1] *= -1
        else:
            temp += char

    return sum(scores)


def solution_2(dartResult):
    from re import findall
    scores = []
    for num, score, option in findall(r'([0-9]*)([SDT])([*#]?)', dartResult):
        new_score = int(num)
        if score == 'D':
            new_score = pow(new_score, 2)
        elif score == 'T':
            new_score = pow(new_score, 3)

        if option == '*':
            if scores:
                scores[-1] *= 2
            new_score *= 2
        elif option == '#':
            new_score *= -1

        scores.append(new_score)
    return sum(scores)


if __name__ == "__main__":
    solutions = [
        solution('1S2D*3T'),
        solution('1D2S#10S'),
        solution('1D2S0T'),
        solution('1S*2T*3S'),
        solution('1D#2S*3S'),
        solution('1T2D3D#'),
        solution('1D2S3T*')
    ]

    answers = [
        37,
        9,
        3,
        23,
        5,
        -4,
        59
    ]

    print_solved(solutions, answers)
