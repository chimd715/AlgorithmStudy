def assert_s(s):
    opposite_parentheses = {"]": "[", "}": "{", ")": "("}

    stack = []
    for item in s:
        if item in ["]", ")", "}"]:
            if len(stack) == 0 or stack.pop() != opposite_parentheses[item]:
                return False
        elif item in ["[", "{", "("]:
            stack.append(item)
    return False if len(stack) > 0 else True


def shift(arr):
    return arr[1:] + arr[0]


def solution(s):
    count = 0

    shift_s = s
    for i in range(len(s)):
        if assert_s(shift_s):
            count += 1
        shift_s = shift(shift_s)

    return count


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
# 3 2 0 0
