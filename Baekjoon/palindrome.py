def is_palindrome(s):
    front_string = s[:len(s)//2]
    rear_string = s[:len(s)//2-1:-1] if len(s) % 2 == 0 else s[:len(s)//2:-1]
    return front_string == rear_string


def solution(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            new_s = s[i:j]
            if is_palindrome(new_s):
                max_length = max(max_length, len(new_s))
    return max_length


print(solution("abcdcba"))
print(solution("abacde"))
# 7 3
