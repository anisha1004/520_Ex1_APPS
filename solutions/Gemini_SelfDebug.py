from collections import defaultdict, deque

def solve_1079(input_str):
    s = '0' + input_str.strip()
    dp_balanced = 0
    dp_owe = 1
    for char in reversed(s):
        if char == '0':
            new_dp_balanced = dp_balanced
            new_dp_owe = 1 + min(dp_balanced, dp_owe)
        else:
            new_dp_balanced = 1 + min(dp_balanced, dp_owe)
            new_dp_owe = dp_owe
        dp_balanced = new_dp_balanced
        dp_owe = new_dp_owe
    return dp_balanced

def solve_771(input_str):
    lines = input_str.strip().split('\n')
    n, k, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    groups = defaultdict(list)
    for x in a:
        groups[x % m].append(x)
    for remainder in groups:
        if len(groups[remainder]) >= k:
            return ("Yes", groups[remainder][:k])
    return ("No", [])

def solve_3040(input_str):
    s = input_str.strip()
    n = len(s)
    def check(length):
        if length == 0 or length > n:
            return False
        seen = set()
        for i in range(n - length + 1):
            sub = s[i:i+length]
            if sub in seen:
                return True
            seen.add(sub)
        return False
    max_len = 0
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
        if check(mid):
            max_len = mid
            low = mid + 1
        else:
            high = mid - 1
    if max_len == 0:
        return ""
    subs = [s[i:i+max_len] for i in range(n - max_len + 1)]
    subs.sort()
    for i in range(len(subs) - 1):
        if subs[i] == subs[i+1]:
            return subs[i]
    return ""

def solve_4655(input_str):
    lines = input_str.strip().split('\n')
    q = int(lines[0])
    outputs = []
    for i in range(1, q + 1):
        a, b, c = map(int, lines[i].split())
        total_candies = a + b + c
        outputs.append(total_candies // 2)
    return outputs

def solve_4245(input_str):
    a, b = map(int, input_str.strip().split())
    if b == 1:
        return 0
    needed = b - 1
    gain_per_strip = a - 1
    strips = (needed + gain_per_strip - 1) // gain_per_strip
    return strips

def solve_747(input_str):
    lines = input_str.strip().split('\n')
    n, x = map(int, lines[0].split())
    candies = [[] for _ in range(2)]
    for i in range(1, n+1):
        t, h, m = map(int, lines[i].split())
        candies[t].append((h, m))
    def calculate_eaten(start_type, initial_jump, candies_lists):
        jump = initial_jump
        available = [list(candies_lists[0]), list(candies_lists[1])]
        eaten_count = 0
        current_type = start_type
        while True:
            best_idx = -1
            max_mass = -1
            for i, (h, m) in enumerate(available[current_type]):
                if h <= jump and m > max_mass:
                    max_mass = m
                    best_idx = i
            if best_idx == -1:
                break
            eaten_count += 1
            jump += max_mass
            available[current_type].pop(best_idx)
            current_type = 1 - current_type
        return eaten_count
    return max(calculate_eaten(0, x, candies), calculate_eaten(1, x, candies))

def solve_1303(input_str):
    lines = input_str.strip().split('\n')
    p, q, l, r = map(int, lines[0].split())
    z_intervals = [tuple(map(int, lines[i+1].split())) for i in range(p)]
    x_intervals = [tuple(map(int, lines[i+1+p].split())) for i in range(q)]
    count = 0
    for t in range(l, r+1):
        is_suitable = False
        for za, zb in z_intervals:
            for xc, xd in x_intervals:
                if max(za, xc + t) <= min(zb, xd + t):
                    is_suitable = True
                    break
            if is_suitable:
                break
        if is_suitable:
            count += 1
    return count

def solve_203(input_str):
    s = input_str.strip()
    n = len(s)
    d_queue = deque()
    r_queue = deque()
    for i, char in enumerate(s):
        if char == 'D':
            d_queue.append(i)
        else:
            r_queue.append(i)
    while d_queue and r_queue:
        d_idx = d_queue.popleft()
        r_idx = r_queue.popleft()
        if d_idx < r_idx:
            d_queue.append(d_idx + n)
        else:
            r_queue.append(r_idx + n)
    return 'D' if d_queue else 'R'

def solve_3177(input_str):
    lines = input_str.strip().split('\n')
    n, m = map(int, lines[0].split())
    initial_perm = tuple(map(int, lines[1].split()))
    swaps = [tuple(map(lambda x: int(x)-1, lines[i+2].split())) for i in range(m)]
    target_perm = tuple(range(1, n+1))
    if initial_perm == target_perm:
        return 0
    q = deque([(initial_perm, 0)])
    visited = {initial_perm}
    while q:
        current, dist = q.popleft()
        current_list = list(current)
        for i, j in swaps:
            next_list = current_list[:]
            next_list[i], next_list[j] = next_list[j], next_list[i]
            next_tuple = tuple(next_list)
            if next_tuple == target_perm:
                return dist + 1
            if next_tuple not in visited:
                visited.add(next_tuple)
                q.append((next_tuple, dist + 1))
    return -1

def solve_4559(input_str):
    a = list(map(int, input_str.strip().split()))
    if 0 in a:
        return 0
    LIMIT = 10**18
    product = 1
    for x in a:
        if x > LIMIT // product:
            return -1
        product *= x
    return product
