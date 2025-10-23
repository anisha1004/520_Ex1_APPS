from collections import defaultdict, deque

def solve_1079(input_str):
    s = input_str.strip()
    dp_balanced = 0
    dp_owe = 1
    s = '0' + s
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
        if length == 0: return ""
        if length > n: return None
        P1, M1 = 31, 10**9 + 7
        P2, M2 = 37, 10**9 + 9
        p1_pow = pow(P1, length - 1, M1)
        p2_pow = pow(P2, length - 1, M2)
        hashes = defaultdict(list)
        h1, h2 = 0, 0
        for i in range(length):
            h1 = (h1 * P1 + ord(s[i])) % M1
            h2 = (h2 * P2 + ord(s[i])) % M2
        hashes[(h1, h2)].append(0)
        best_found_sub = None
        for i in range(1, n - length + 1):
            h1 = ((h1 - ord(s[i-1]) * p1_pow) * P1 + ord(s[i + length - 1])) % M1
            h2 = ((h2 - ord(s[i-1]) * p2_pow) * P2 + ord(s[i + length - 1])) % M2
            h = (h1, h2)
            if h in hashes:
                current_sub = s[i : i+length]
                for start_index in hashes[h]:
                    if s[start_index : start_index + length] == current_sub:
                        if best_found_sub is None or current_sub < best_found_sub:
                            best_found_sub = current_sub
                        break
            hashes[h].append(i)
        return best_found_sub
    low, high = 0, n
    ans_str = ""
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
        result = check(mid)
        if result is not None:
            ans_str = result
            low = mid + 1
        else:
            high = mid - 1
    return ans_str

def solve_4655(input_str):
    lines = input_str.strip().split('\n')
    q = int(lines[0])
    outputs = []
    for i in range(1, q + 1):
        a, b, c = map(int, lines[i].split())
        outputs.append((a + b + c) // 2)
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
            best_candy_idx = -1
            max_mass = -1
            for i, (h, m) in enumerate(available[current_type]):
                if h <= jump and m > max_mass:
                    max_mass = m
                    best_candy_idx = i
            if best_candy_idx == -1:
                break
            eaten_count += 1
            jump += max_mass
            available[current_type].pop(best_candy_idx)
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
        current_perm_tuple, dist = q.popleft()
        current_perm_list = list(current_perm_tuple)
        for i, j in swaps:
            next_perm_list = current_perm_list[:]
            next_perm_list[i], next_perm_list[j] = next_perm_list[j], next_perm_list[i]
            next_perm_tuple = tuple(next_perm_list)
            if next_perm_tuple == target_perm:
                return dist + 1
            if next_perm_tuple not in visited:
                visited.add(next_perm_tuple)
                q.append((next_perm_tuple, dist + 1))
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
