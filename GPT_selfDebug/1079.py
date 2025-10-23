def solve_1079_v1(s):
    s = list(map(int, s[::-1]))  # reverse for LSB -> MSB
    s.append(0)  # extra space for carry
    n = len(s)
    count = 0

    for i in range(n):
        if s[i] > 1:
            s[i+1] += s[i] // 2
            s[i] %= 2
        if s[i] == 1:
            count += 1
    return count



from functools import lru_cache

def solve_1079_v2(s):
    n = int(s, 2)

    @lru_cache(None)
    def solve(x):
        if x == 0:
            return 0
        # nearest power of 2
        p = 1
        while p <= x:
            p *= 2
        p //= 2
        # try subtracting or adding powers of 2
        return 1 + min(solve(x - p), solve(p - x))
    
    return solve(n)

print(min_beautiful_numbers_2(s))  # Output: 4


def solve_1079_v3(s):
    s = list(map(int, s[::-1]))
    s.append(0)  # for potential carry
    count = 0
    i = 0
    while i < len(s):
        if s[i] > 1:
            s[i+1] += s[i] // 2
            s[i] %= 2
        if s[i] == 1:
            count += 1
        i += 1
    return count

