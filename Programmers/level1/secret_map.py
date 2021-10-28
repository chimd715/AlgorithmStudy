"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/17681
"""
from common import print_solved


def solution(n, map1, map2):
    _map = [[0] * n for i in range(n)]
    for i in range(n):
        _map1 = bin(map1[i])[2:].zfill(n)
        _map2 = bin(map2[i])[2:].zfill(n)
        for j in range(n):
            _map[i][j] = int(_map1[j:j+1]) or int(_map2[j:j+1])

    return ["".join([_char and "#" or " " for _char in _line]) for _line in _map]


if __name__ == "__main__":
    solutions = [
        solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]),
        solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
    ]

    answers = [
        ["#####", "# # #", "### #", "#  ##", "#####"],
        ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
    ]

    print_solved(solutions, answers)
