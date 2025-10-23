# Problem 1079
def solve_1079_v1(input_str: str) -> str:
    s = input_str.strip()
    s = '0' + s
    count = 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == '1':
            j = i
            while j >= 0 and s[j] == '1':
                j -= 1
            if j >= 0:
                s = s[:j] + '1' + '0' * (i - j + 1) + s[i+1:]
                count += 1
                i = j
            else:
                count += 1
                break
        else:
            i -= 1
    return f"{count}\n"

def solve_1079_v2(input_str: str) -> str:
    s = input_str.strip()
    digits = list(s)
    digits.insert(0, '0')
    count = 0
    i = len(digits) - 1
    while i > 0:
        if digits[i] == '1':
            start = i
            while i > 0 and digits[i] == '1':
                i -= 1
            if digits[i] == '0':
                digits[i] = '1'
                for k in range(i + 1, start + 2):
                    if k < len(digits):
                        digits[k] = '0'
                count += 1
            else:
                i -= 1
        else:
            i -= 1
    return f"{count}\n"

def solve_1079_v3(input_str: str) -> str:
    s = input_str.strip()
    result = 0
    consecutive = 0
    for ch in s:
        if ch == '1':
            consecutive += 1
        else:
            if consecutive > 0:
                result += 1
                consecutive = 0
    if consecutive > 0:
        result += 1
    return f"{result}\n"

# Problem 771
def solve_771_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, k, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    groups = {}
    for num in a:
        r = num % m
        if r not in groups:
            groups[r] = []
        groups[r].append(num)
    for r in groups:
        if len(groups[r]) >= k:
            return "Yes\n" + ' '.join(map(str, groups[r][:k])) + " "
    return "No"

def solve_771_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, k, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    remainders = [[] for _ in range(m)]
    for num in a:
        remainders[num % m].append(num)
    for bucket in remainders:
        if len(bucket) >= k:
            return "Yes\n" + ' '.join(map(str, bucket[:k])) + " "
    return "No"

def solve_771_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, k, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    from collections import defaultdict
    mod_groups = defaultdict(list)
    for num in a:
        mod_groups[num % m].append(num)
    for key in mod_groups:
        if len(mod_groups[key]) >= k:
            return "Yes\n" + ' '.join(map(str, mod_groups[key][:k])) + " "
    return "No"

# Problem 3040
def solve_3040_v1(input_str: str) -> str:
    s = input_str.strip()
    n = len(s)
    max_len = 0
    result = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if s.count(substr) > 1:
                if len(substr) > max_len or (len(substr) == max_len and substr < result):
                    max_len = len(substr)
                    result = substr
    return result + "\n"

def solve_3040_v2(input_str: str) -> str:
    s = input_str.strip()
    n = len(s)
    best = ""
    for length in range(n, 0, -1):
        candidates = []
        for i in range(n - length + 1):
            substr = s[i:i + length]
            if s.find(substr, i + 1) != -1:
                candidates.append(substr)
        if candidates:
            return min(candidates) + "\n"
    return "\n"

def solve_3040_v3(input_str: str) -> str:
    s = input_str.strip()
    n = len(s)
    suffixes = [s[i:] for i in range(n)]
    suffixes.sort()
    max_len = 0
    result = ""
    for i in range(n - 1):
        lcp_len = 0
        for j in range(min(len(suffixes[i]), len(suffixes[i + 1]))):
            if suffixes[i][j] == suffixes[i + 1][j]:
                lcp_len += 1
            else:
                break
        if lcp_len > max_len:
            max_len = lcp_len
            result = suffixes[i][:lcp_len]
    return result + "\n"

# Problem 4655
def solve_4655_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    q = int(lines[0])
    results = []
    for i in range(1, q + 1):
        a, b, c = map(int, lines[i].split())
        total = a + b + c
        results.append(str(min(total // 2, a + b, a + c, b + c)))
    return '\n'.join(results) + '\n'

def solve_4655_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    q = int(lines[0])
    results = []
    for i in range(1, q + 1):
        piles = list(map(int, lines[i].split()))
        piles.sort()
        results.append(str(min((piles[0] + piles[1] + piles[2]) // 2, piles[1] + piles[2])))
    return '\n'.join(results) + '\n'

def solve_4655_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    q = int(lines[0])
    results = []
    for i in range(1, q + 1):
        a, b, c = map(int, lines[i].split())
        results.append(str(min(a + b, a + c, b + c)))
    return '\n'.join(results) + '\n'

# Problem 4245
def solve_4245_v1(input_str: str) -> str:
    a, b = map(int, input_str.strip().split())
    if b <= 1:
        return "0\n"
    else:
        return f"{(b - 2 + a - 1) // (a - 1)}\n"

def solve_4245_v2(input_str: str) -> str:
    a, b = map(int, input_str.strip().split())
    sockets = 1
    strips = 0
    while sockets < b:
        sockets += a - 1
        strips += 1
    return f"{strips}\n"

def solve_4245_v3(input_str: str) -> str:
    a, b = map(int, input_str.strip().split())
    import math
    return f"{max(0, math.ceil((b - 1) / (a - 1)))}\n"

# Problem 747
def solve_747_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, x = map(int, lines[0].split())
    candies = []
    for i in range(1, n + 1):
        t, h, m = map(int, lines[i].split())
        candies.append((t, h, m))
    candies.sort(key=lambda c: c[1])
    dp = {}
    def solve(idx, jump, last_type):
        if idx == n:
            return 0
        state = (idx, jump, last_type)
        if state in dp:
            return dp[state]
        res = solve(idx + 1, jump, last_type)
        t, h, m = candies[idx]
        if jump >= h and t != last_type:
            res = max(res, 1 + solve(idx + 1, jump + m, t))
        dp[state] = res
        return res
    return f"{solve(0, x, -1)}\n"

def solve_747_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, x = map(int, lines[0].split())
    candies = []
    for i in range(1, n + 1):
        t, h, m = map(int, lines[i].split())
        candies.append((h, m, t))
    candies.sort()
    memo = {}
    def dfs(i, height, prev):
        if i == n:
            return 0
        if (i, height, prev) in memo:
            return memo[(i, height, prev)]
        result = dfs(i + 1, height, prev)
        h, m, t = candies[i]
        if height >= h and t != prev:
            result = max(result, 1 + dfs(i + 1, height + m, t))
        memo[(i, height, prev)] = result
        return result
    return f"{dfs(0, x, -1)}\n"

def solve_747_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, x = map(int, lines[0].split())
    candies = []
    for i in range(1, n + 1):
        t, h, m = map(int, lines[i].split())
        candies.append((h, m, t))
    candies.sort()
    INF = float('inf')
    dp = [[-INF, -INF] for _ in range(n + 1)]
    dp[0][0] = x
    dp[0][1] = x
    for i in range(n):
        h, m, t = candies[i]
        for j in range(i, -1, -1):
            if dp[j][1 - t] >= h:
                dp[j + 1][t] = max(dp[j + 1][t], dp[j][1 - t] + m)
            dp[j][t] = max(dp[j][t], dp[j][t])
    for i in range(n, -1, -1):
        if dp[i][0] > -INF or dp[i][1] > -INF:
            return f"{i}\n"
    return "0\n"

# Problem 1303
def solve_1303_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p, q, l, r = map(int, lines[0].split())
    z_schedule = []
    for i in range(1, p + 1):
        a, b = map(int, lines[i].split())
        z_schedule.append((a, b))
    x_schedule = []
    for i in range(p + 1, p + q + 1):
        c, d = map(int, lines[i].split())
        x_schedule.append((c, d))
    count = 0
    for t in range(l, r + 1):
        overlap = False
        for c, d in x_schedule:
            for a, b in z_schedule:
                if not (c + t > b or d + t < a):
                    overlap = True
                    break
            if overlap:
                break
        if overlap:
            count += 1
    return f"{count}\n"

def solve_1303_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p, q, l, r = map(int, lines[0].split())
    z = [tuple(map(int, lines[i].split())) for i in range(1, p + 1)]
    x = [tuple(map(int, lines[i].split())) for i in range(p + 1, p + q + 1)]
    result = 0
    for t in range(l, r + 1):
        for c, d in x:
            for a, b in z:
                if max(a, c + t) <= min(b, d + t):
                    result += 1
                    break
            else:
                continue
            break
    return f"{result}\n"

def solve_1303_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p, q, l, r = map(int, lines[0].split())
    z_intervals = [tuple(map(int, lines[i].split())) for i in range(1, p + 1)]
    x_intervals = [tuple(map(int, lines[i].split())) for i in range(p + 1, p + q + 1)]
    count = 0
    for shift in range(l, r + 1):
        found = False
        for x_start, x_end in x_intervals:
            for z_start, z_end in z_intervals:
                if x_start + shift <= z_end and x_end + shift >= z_start:
                    found = True
                    break
            if found:
                break
        if found:
            count += 1
    return f"{count}\n"

# Problem 203
def solve_203_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    s = lines[1].strip()
    from collections import deque
    senate = deque()
    for i, ch in enumerate(s):
        senate.append((ch, i))
    d_wait, r_wait = 0, 0
    while senate:
        party, idx = senate.popleft()
        if party == 'D':
            if r_wait > 0:
                r_wait -= 1
            else:
                d_wait += 1
                if all(p == 'D' for p, _ in senate) and d_wait >= len(senate) + 1:
                    return 'D\n'
                senate.append((party, idx))
        else:
            if d_wait > 0:
                d_wait -= 1
            else:
                r_wait += 1
                if all(p == 'R' for p, _ in senate) and r_wait >= len(senate) + 1:
                    return 'R\n'
                senate.append((party, idx))
    return 'D\n' if d_wait > 0 else 'R\n'

def solve_203_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    s = lines[1].strip()
    from collections import deque
    q = deque(range(n))
    d_ban, r_ban = 0, 0
    while q:
        if len(set(s[i] for i in q)) == 1:
            return s[q[0]] + '\n'
        i = q.popleft()
        if s[i] == 'D':
            if d_ban > 0:
                d_ban -= 1
            else:
                r_ban += 1
                q.append(i)
        else:
            if r_ban > 0:
                r_ban -= 1
            else:
                d_ban += 1
                q.append(i)
    return 'D\n'

def solve_203_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    senate = lines[1].strip()
    active = list(range(n))
    d_pending, r_pending = 0, 0
    while True:
        new_active = []
        for i in active:
            if senate[i] == 'D':
                if r_pending > 0:
                    r_pending -= 1
                else:
                    d_pending += 1
                    new_active.append(i)
            else:
                if d_pending > 0:
                    d_pending -= 1
                else:
                    r_pending += 1
                    new_active.append(i)
        active = new_active
        if len(active) == 0:
            return 'D\n' if d_pending > 0 else 'R\n'
        if all(senate[i] == senate[active[0]] for i in active):
            return senate[active[0]] + '\n'

# Problem 3177
def solve_3177_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    from collections import deque
    n, m = map(int, lines[0].split())
    perm = tuple(map(int, lines[1].split()))
    swaps = []
    for i in range(2, 2 + m):
        a, b = map(int, lines[i].split())
        swaps.append((a - 1, b - 1))
    target = tuple(range(1, n + 1))
    if perm == target:
        return "0\n"
    queue = deque([(perm, 0)])
    visited = {perm}
    while queue:
        current, dist = queue.popleft()
        for a, b in swaps:
            new_perm = list(current)
            new_perm[a], new_perm[b] = new_perm[b], new_perm[a]
            new_perm = tuple(new_perm)
            if new_perm == target:
                return f"{dist + 1}\n"
            if new_perm not in visited:
                visited.add(new_perm)
                queue.append((new_perm, dist + 1))
    return "-1\n"

def solve_3177_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, m = map(int, lines[0].split())
    initial = tuple(map(int, lines[1].split()))
    allowed = []
    for i in range(2, 2 + m):
        a, b = map(int, lines[i].split())
        allowed.append((a - 1, b - 1))
    goal = tuple(range(1, n + 1))
    from collections import deque
    q = deque([(initial, 0)])
    seen = {initial}
    while q:
        state, moves = q.popleft()
        if state == goal:
            return f"{moves}\n"
        for i, j in allowed:
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            new_state = tuple(new_state)
            if new_state not in seen:
                seen.add(new_state)
                q.append((new_state, moves + 1))
    return "-1\n"

def solve_3177_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, m = map(int, lines[0].split())
    perm = tuple(map(int, lines[1].split()))
    swaps = [tuple(map(lambda x: int(x) - 1, lines[i].split())) for i in range(2, 2 + m)]
    from collections import deque
    target = tuple(range(1, n + 1))
    q = deque([(perm, 0)])
    visited = {perm}
    while q:
        cur, depth = q.popleft()
        if cur == target:
            return f"{depth}\n"
        for i, j in swaps:
            nxt = list(cur)
            nxt[i], nxt[j] = nxt[j], nxt[i]
            nxt = tuple(nxt)
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, depth + 1))
    return "-1\n"

# Problem 4559
def solve_4559_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    if 0 in a:
        return "0\n"
    limit = 10 ** 18
    result = 1
    for num in a:
        if result > limit // num:
            return "-1\n"
        result *= num
    return f"{result}\n"

def solve_4559_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    MAX = 10 ** 18
    product = 1
    for x in nums:
        if x == 0:
            return "0\n"
        if product > MAX // x:
            return "-1\n"
        product *= x
    return f"{product}\n"

def solve_4559_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    threshold = 10 ** 18
    prod = 1
    for val in a:
        if val == 0:
            return "0\n"
        if prod > threshold // val:
            return "-1\n"
        prod *= val
    return f"{prod}\n"

