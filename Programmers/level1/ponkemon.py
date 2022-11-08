"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/1845
"""
from common import print_solved


def solution(nums):
    pokemon_dict = {}
    for num in nums:
        if num not in pokemon_dict:
            pokemon_dict[num] = 0
        pokemon_dict[num] += 1

    return len(nums) // 2 if len(pokemon_dict) >= len(nums) // 2 else len(pokemon_dict)


if __name__ == "__main__":
    solutions = [
        solution([3, 1, 2, 3]),
        solution([3, 3, 3, 2, 2, 4]),
        solution([3, 3, 3, 2, 2, 2]),
    ]

    answers = [2, 3, 2]

    print_solved(solutions, answers)
