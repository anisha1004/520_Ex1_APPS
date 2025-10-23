from collections import defaultdict, deque
import heapq
import json

def solve_1079(inp: str) -> str:
    s = inp.strip()
    n = int(s, 2)
    cnt = 0
    while n:
        if n & 1:
            u = 1 if (n & 3) == 1 or n == 1 else -1
            cnt += 1
            n -= u
        else:
            n >>= 1
    return f"{cnt}\n"

def solve_771(inp: str) -> str:
    lines = inp.strip().splitlines()
    n, k, m = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    buckets = defaultdict(list)
    for x in arr:
        buckets[x % m].append(x)
    for vals in buckets.values():
        if len(vals) >= k:
            chosen = vals[:k]
            return "Yes\n" + " ".join(map(str, chosen)) + " \n"
    return "No\n"

def _suffix_array(s: str):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            a, b = sa[i - 1], sa[i]
            tmp[b] = tmp[a] + ((rank[a], rank[a + k] if a + k < n else -1) < (rank[b], rank[b + k] if b + k < n else -1))
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
    return lcp

def solve_3040(inp: str) -> str:
    s = inp.strip()
    sa = _suffix_array(s)
    lcp = _kasai(s, sa)
    maxL = max(lcp)
    best = None
    for i in range(1, len(s)):
        if lcp[i] == maxL:
            for start in (sa[i], sa[i - 1]):
                cand = s[start:start + maxL]
                if best is None or cand < best:
                    best = cand
    return f"{best}\n"

def solve_4655(inp: str) -> str:
    it = iter(inp.strip().splitlines())
    q = int(next(it))
    out = []
    for _ in range(q):
        a, b, c = map(int, next(it).split())
        s = a + b + c
        out.append(str(min(s // 2, s - min(a, b, c))))
    return "\n".join(out) + "\n"

def solve_4245(inp: str) -> str:
    A, B = map(int, inp.strip().split())
    if B <= 1:
        return "0\n"
    need = (B - 1 + (A - 2)) // (A - 1)
    return f"{need}\n"

def _simulate_candies(candies, x, start_type):
    by_type = {
        0: sorted([(h, m) for t, h, m in candies if t == 0]),
        1: sorted([(h, m) for t, h, m in candies if t == 1]),
    }
    idx = {0: 0, 1: 0}
    pq = {0: [], 1: []}  # max-heaps by -m
    jump = x
    cur = start_type
    eaten = 0
    while True:
        while idx[cur] < len(by_type[cur]) and by_type[cur][idx[cur]][0] <= jump:
            h, m = by_type[cur][idx[cur]]
            heapq.heappush(pq[cur], (-m, m))
            idx[cur] += 1
        if not pq[cur]:
            break
        m = heapq.heappop(pq[cur])[1]
        jump += m
        eaten += 1
        cur ^= 1
    return eaten

def solve_747(inp: str) -> str:
    it = iter(inp.strip().splitlines())
    n, x = map(int, next(it).split())
    candies = []
    for _ in range(n):
        t, h, m = map(int, next(it).split())
        candies.append((t, h, m))
    ans = max(_simulate_candies(candies, x, 0), _simulate_candies(candies, x, 1))
    return f"{ans}\n"

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
    return ('D\n' if qD else 'R\n')

def solve_3177(inp: str) -> str:
    it = iter(inp.strip().splitlines())
    N, M = map(int, next(it).split())
    perm = tuple(map(int, next(it).split()))
    swaps = [tuple(map(int, next(it).split())) for _ in range(M)]
    swaps = [(a - 1, b - 1) for a, b in swaps]
    target = tuple(range(1, N + 1))
    if perm == target:
        return "0\n"
    dq = deque([(perm, 0)])
    seen = {perm}
    while dq:
        state, d = dq.popleft()
        arr = list(state)
        for a, b in swaps:
            arr[a], arr[b] = arr[b], arr[a]
            newt = tuple(arr)
            if newt not in seen:
                if newt == target:
                    return f"{d + 1}\n"
                seen.add(newt)
                dq.append((newt, d + 1))
            arr[a], arr[b] = arr[b], arr[a]
    # Problem guarantees a solution exists
    return "0\n"

def solve_4559(inp: str) -> str:
    it = iter(inp.strip().splitlines())
    n = int(next(it))
    A = list(map(int, next(it).split()))
    LIMIT = 10**18
    if 0 in A:
        return "0\n"
    prod = 1
    for a in A:
        if prod > LIMIT // max(a, 1):
            return "-1\n"
        prod *= a
        if prod > LIMIT:
            return "-1\n"
    return f"{prod}\n"


