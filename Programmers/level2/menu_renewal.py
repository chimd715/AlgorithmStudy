"""
    programmers algorithm
    last solved: 2021.11.27
    url: https://programmers.co.kr/learn/courses/30/lessons/72411
"""
from common import print_solved


def solution(orders, course_menu_counts):
    from itertools import combinations

    answer = []
    for course_menu_count in course_menu_counts:
        ordered_courses = []
        for order in orders:
            ordered_courses.extend(list(map(lambda x: ''.join(sorted(x)), combinations(order, course_menu_count))))

        courses = {}
        for ordered_course in ordered_courses:
            courses[ordered_course] = courses[ordered_course] + 1 if ordered_course in courses else 1

        if not courses:
            continue

        max_course_order_count = max(list(courses.values()))
        if max_course_order_count > 1:
            answer.extend([course for course in courses if courses[course] == max_course_order_count])

    return sorted(answer)


def solution_with_counter(orders, course):
    from collections import Counter
    from itertools import combinations

    answer = []
    for menu_size in course:
        possible_courses = []
        for order in orders:
            possible_courses.extend(list(map(lambda x: ''.join(sorted(x)), combinations(order, menu_size))))

        if not possible_courses:
            continue

        courses_counter = Counter(possible_courses).most_common()
        most_ordered_count = courses_counter[0][1] if courses_counter[0][1] > 1 else 30
        for course_name, order_count in courses_counter:
            if order_count < most_ordered_count:
                break
            answer.append(course_name)

    return sorted(answer)


if __name__ == "__main__":
    solutions = [
        solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]),
        solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]),
        solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
    ]

    answers = [
        ["AC", "ACDE", "BCFG", "CDE"],
        ["ACD", "AD", "ADE", "CD", "XYZ"],
        ["WX", "XY"]
    ]

    print_solved(solutions, answers)
