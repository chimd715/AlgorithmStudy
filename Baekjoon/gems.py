def solution(gems):
    answer = [0, 0]

    distinct_gem_count = len(set(gems))
    # print(f"distince gem count: {distinct_gem_count}")

    gem_bag = {}
    gem_bag[gems[0]] = 1

    start_pos = 0
    end_pos = 0
    distance = 99999
    while start_pos <= end_pos < len(gems):
        if len(gem_bag) < distinct_gem_count:
            # print("take more gem")
            end_pos = end_pos + 1
            if end_pos >= len(gems):
                break

            gem = gems[end_pos]
            # print(f"gem: {gem}")
            if gem in gem_bag:
                gem_bag[gem] += 1
            else:
                gem_bag[gem] = 1
        else:
            # print("pop gem")
            if distance > end_pos - start_pos:
                distance = end_pos - start_pos
                answer = [start_pos + 1, end_pos + 1]
                # print(f"update distance: {distance}")

            gem = gems[start_pos]
            # print(f"gem: {gem}")
            gem_bag[gem] -= 1
            if gem_bag[gem] == 0:
                del gem_bag[gem]

            start_pos = start_pos + 1
        # print(f"gem bag status: {gem_bag}")

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

"""
3, 7
1, 3
1, 1
1, 5
"""
