"""
    programmers algorithm
    last solved: 2021.12.12
    url: https://programmers.co.kr/learn/courses/30/lessons/17677
"""
from common import print_solved


def solution(str1, str2):
    import re
    j_str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not ''.join(re.findall(r'[^a-z]*', str1[i:i+2]))]
    j_str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not ''.join(re.findall(r'[^a-z]*', str2[i:i+2]))]

    j_i_list = []
    for item in j_str1:
        if item in j_str2 and j_i_list.count(item) < min(j_str1.count(item), j_str2.count(item)):
            j_i_list.append(item)

    j_i = len(j_i_list)
    j_u = len(j_str1) + len(j_str2) - j_i

    j = 1 if j_u == 0 else j_i / j_u
    return int(j * 65536)


def solution_2(str1, str2):
    from collections import Counter
    j_str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    j_str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    j_counter1 = Counter(j_str1)
    j_counter2 = Counter(j_str2)

    j_i = sum((j_counter1 & j_counter2).values())
    j_u = sum((j_counter1 | j_counter2).values())

    j = 1 if j_u == 0 else j_i / j_u
    return int(j * 65536)


if __name__ == "__main__":
    solutions = [
        solution("FRANCE", "french"),
        solution("handshake", "shake hands"),
        solution("aa1+aa2", "AAAA12"),
        solution("E=M*C^2", "e=m*c^2"),
        solution("", "")
    ]

    answers = [
        16384,
        65536,
        43690,
        65536,
        65536
    ]

    print_solved(solutions, answers)
