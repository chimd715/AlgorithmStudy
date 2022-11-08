"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/77484
"""
from common import print_solved


def lotto_rank(num):
    return 7 - num if num > 1 else 6


def solution(lottos, win_nums):
    match_count = 0
    wild_card_count = 0
    for lotto_num in lottos:
        if lotto_num in win_nums:
            match_count += 1
        if lotto_num == 0:
            wild_card_count += 1

    return [lotto_rank(match_count + wild_card_count), lotto_rank(match_count)]


if __name__ == "__main__":
    solutions = [
        solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]),
        solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]),
        solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]),
    ]

    answers = [[3, 5], [1, 6], [1, 1]]

    print_solved(solutions, answers)
