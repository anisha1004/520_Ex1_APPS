from collections import defaultdict

def solution1(n, k, m, arr):
    rem_groups = defaultdict(list)
    for x in arr:
        rem_groups[x % m].append(x)

    for group in rem_groups.values():
        if len(group) >= k:
            print("Yes")
            print(*group[:k])
            return
    print("No")

# Example test
solution1(3, 2, 3, [1, 8, 4])  # Output: Yes 1 4
solution1(3, 3, 3, [1, 8, 4])  # Output: No


from collections import Counter

def solution2(n, k, m, arr):
    cnt = Counter(arr)
    rem_groups = defaultdict(list)
    for num in cnt:
        rem_groups[num % m].extend([num]*cnt[num])

    for group in rem_groups.values():
        if len(group) >= k:
            print("Yes")
            print(*group[:k])
            return
    print("No")

# Test
solution2(4, 3, 5, [2, 7, 7, 7])  # Output: Yes 2 7 7
solution2(3, 3, 3, [1, 8, 4])      # Output: No


def solution3(n, k, m, arr):
    remainders = [[] for _ in range(m)]
    for x in arr:
        remainders[x % m].append(x)

    for group in remainders:
        if len(group) >= k:
            print("Yes")
            print(*group[:k])
            return
    print("No")

# Test
solution3(3, 2, 3, [1, 8, 4])  # Yes 1 4
solution3(3, 3, 3, [1, 8, 4])  # No
solution3(4, 3, 5, [2, 7, 7, 7])  # Yes 2 7 7
