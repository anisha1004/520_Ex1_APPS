from collections import defaultdict, deque
import heapq

# ---------- Problem 1079 ----------
def solve_1079(inp: str) -> str:
    s = inp.strip()
    n = len(s)
    cnt = 0
    carry = 0
    i = 0
    # Process binary string using +/-1 and /2 (via carry), counting ops
    while i < n or carry:
        b = int(s[n - 1 - i]) if i < n else 0
        x = b + carry
        if x % 2 == 0:
            carry = x // 2
        else:
            # choose +/-1 to make next even; prefer -1 unless x==1 or x%4==1
            r = x & 3
            cnt += 1
            carry = (x - 1) // 2 if (r == 1 or x == 1) else (x + 1) // 2
        i += 1
    return f"{cnt}\n"

# ---------- Problem 771 ----------
def solve_771(inp: str) -> str:
    parts = inp.strip().split()
    it = iter(parts)
    n = int(next(it)); k = int(next(it)); m = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    groups = defaultdict(list)
    for a in nums:
        groups[a % m].append(a)
    for arr in groups.values():
        if len(arr) >= k:
            return "Yes\n" + " ".join(map(str, arr[:k])) + " \n"
    return "No\n"

# ---------- Problem 3040 ----------
def _suffix_array(s: str):
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            a, b = sa[i - 1], sa[i]
            tmp[b] = tmp[a] + (
                (rank[a], rank[a + k] if a + k < n else -1)
                < (rank[b], rank[b + k] if b + k < n else -1)
            )
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

def _kasai(s: str, sa):
    n = len(s)
    rank = [0] * n
    for i, p in enumerate(sa):
        rank[p] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        r = rank[i]
        if r == 0:
            k = 0
            continue
        j = sa[r - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[r] = k
        if k:
            k -= 1
    return lcp  # lcp[i] is LCP of sa[i] and sa[i-1]

def solve_3040(inp: str) -> str:
    s = inp.strip()
    if not s:
        return "\n"
    sa = _suffix_array(s)
    lcp = _kasai(s, sa)
    maxL = max(lcp)
    best = None
    # pick lexicographically smallest substring among those with length maxL
    for i in range(1, len(s)):
        if lcp[i] == maxL:
            for start in (sa[i], sa[i - 1]):
                cand = s[start:start + maxL]
                if best is None or cand < best:
                    best = cand
    return f"{best}\n"

# ---------- Problem 4655 ----------
def solve_4655(inp: str) -> str:
    it = iter(inp.strip().split())
    q = int(next(it))
    out = []
    for _ in range(q):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        total = a + b + c
        m1 = total // 2
        m2 = total - min(a, b, c)
        out.append(str(min(m1, m2)))
    return "\n".join(out) + "\n"

# ---------- Problem 4245 ----------
def solve_4245(inp: str) -> str:
    A, B = map(int, inp.strip().split())
    if B <= 1:
        return "0\n"
    return f"{(B - 1 + (A - 2)) // (A - 1)}\n"

# ---------- Problem 747 ----------
def _simulate_omnom(candies, x0, start_type):
    # Greedy: at each step, eat the reachable candy of the required type with max mass.
    used = [False] * len(candies)
    x = x0
    t = start_type
    eaten = 0
    while True:
        best_idx = -1
        best_m = -1
        for i, (tt, h, m) in enumerate(candies):
            if not used[i] and tt == t and h <= x and m > best_m:
                best_m = m
                best_idx = i
        if best_idx == -1:
            break
        used[best_idx] = True
        x += candies[best_idx][2]
        eaten += 1
        t ^= 1
    return eaten

def solve_747(inp: str) -> str:
    lines = inp.strip().splitlines()
    n, x = map(int, lines[0].split())
    candies = [tuple(map(int, ln.split())) for ln in lines[1:1 + n]]
    ans = max(_simulate_omnom(candies, x, 0), _simulate_omnom(candies, x, 1))
    return f"{ans}\n"

# ---------- Problem 1303 ----------
def solve_1303(inp: str) -> str:
    it = iter(inp.strip().splitlines())
    p, q, l, r = map(int, next(it).split())
    A = [tuple(map(int, next(it).split())) for _ in range(p)]
    C = [tuple(map(int, next(it).split())) for _ in range(q)]
    ans = 0
    for t in range(l, r + 1):
        ok = False
        for a, b in A:
            if ok:
                break
            for c, d in C:
                if max(a, c + t) <= min(b, d + t):
                    ok = True
                    break
        if ok:
            ans += 1
    return f"{ans}\n"

# ---------- Problem 203 ----------
def solve_203(inp: str) -> str:
    lines = inp.strip().splitlines()
    n = int(lines[0])
    s = lines[1].strip()
    qD = deque(i for i, ch in enumerate(s) if ch == 'D')
    qR = deque(i for i, ch in enumerate(s) if ch == 'R')
    while qD and qR:
        d = qD.popleft()
        r = qR.popleft()
        if d < r:
            qD.append(d + n)
        else:
            qR.append(r + n)
    return "D\n" if qD else "R\n"

# ---------- Problem 3177 ----------
def solve_3177(inp: str) -> str:
    parts = inp.strip().split()
    it = iter(parts)
    N = int(next(it)); M = int(next(it))
    perm = tuple(int(next(it)) for _ in range(N))
    swaps = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(M)]
    target = tuple(range(1, N + 1))
    if perm == target:
        return "0\n"

    def neighbors(state):
        lst = list(state)
        for a, b in swaps:
            lst[a], lst[b] = lst[b], lst[a]
            yield tuple(lst)
            lst[a], lst[b] = lst[b], lst[a]

    front = {perm: 0}
    back = {target: 0}
    qf = deque([perm])
    qb = deque([target])

    while qf and qb:
        # expand smaller frontier
        if len(qf) <= len(qb):
            cur_q, cur_map, other_map = qf, front, back
        else:
            cur_q, cur_map, other_map = qb, back, front

        for _ in range(len(cur_q)):
            state = cur_q.popleft()
            d = cur_map[state]
            for nxt in neighbors(state):
                if nxt in cur_map:
                    continue
                if nxt in other_map:
                    return f"{d + 1 + other_map[nxt]}\n"
                cur_map[nxt] = d + 1
                cur_q.append(nxt)
    # Problem guarantees solvable
    return "-1\n"

# ---------- Problem 4559 ----------
def solve_4559(inp: str) -> str:
    it = iter(inp.strip().split())
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    LIMIT = 10**18
    if 0 in arr:
        return "0\n"
    prod = 1
    for a in arr:
        if a > LIMIT // prod:
            return "-1\n"
        prod *= a
        if prod > LIMIT:
            return "-1\n"
    return f"{prod}\n"


