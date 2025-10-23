from collections import defaultdict

def solve_771_v1(n, k, m, arr):
    rem_groups = defaultdict(list)
    for x in arr:
        rem_groups[x % m].append(x)

    for group in rem_groups.values():
        if len(group) >= k:
            print("Yes")
            print(*group[:k])
            return
    print("No")



from collections import Counter

def solve_771_v2(n, k, m, arr):
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




def solve_771_v3(n, k, m, arr):
    remainders = [[] for _ in range(m)]
    for x in arr:
        remainders[x % m].append(x)

    for group in remainders:
        if len(group) >= k:
            print("Yes")
            print(*group[:k])
            return
    print("No")


