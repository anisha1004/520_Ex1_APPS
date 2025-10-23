from collections import defaultdict, deque
import heapq

def solve_1079(data: str) -> str:
    s = data.strip()
    def strip0(x: str) -> str:
        x = x.lstrip('0')
        return x if x else "0"
    def is_zero(x: str) -> bool:
        return x == "0"
    def is_one(x: str) -> bool:
        return x == "1"
    def is_odd(x: str) -> bool:
        return x[-1] == '1'
    def mod4(x: str) -> int:
        if len(x) == 1:
            return int(x, 2)
        return int(x[-2:], 2)
    def add1(x: str) -> str:
        a = list(x); i = len(a) - 1; c = 1
        while i >= 0 and c:
            if a[i] == '0': a[i] = '1'; c = 0
            else: a[i] = '0'; c = 1
            i -= 1
        if c: a.insert(0, '1')
        return ''.join(a)
    def sub1(x: str) -> str:
        a = list(x); i = len(a) - 1; b = 1
        while i >= 0 and b:
            if a[i] == '1': a[i] = '0'; b = 0
            else: a[i] = '1'; b = 1
            i -= 1
        return strip0(''.join(a))
    def div2(x: str) -> str:
        return "0" if len(x) == 1 else x[:-1]
    s = strip0(s)
    ans = 0
    while not is_zero(s):
        if is_odd(s):
            if is_one(s): ans += 1; s = "0"
            else:
                if mod4(s) == 1: s = sub1(s)
                else: s = add1(s)
                ans += 1
        else:
            s = div2(s)
    return str(ans) + "\n"

def solve_771(data: str) -> str:
    it = iter(data.strip().split())
    n = int(next(it)); k = int(next(it)); m = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    groups = defaultdict(list)
    for a in nums: groups[a % m].append(a)
    for lst in groups.values():
        if len(lst) >= k:
            return "Yes\n" + " ".join(map(str, lst[:k])) + " \n"
    return "No\n"

def solve_3040(data: str) -> str:
    s = data.strip()
    n = len(s)
    if n <= 1: return s + "\n"
    MOD1, MOD2 = 1_000_000_007, 1_000_000_009
    B = 911382323
    pow1 = [1]*(n+1); pow2 = [1]*(n+1)
    for i in range(n):
        pow1[i+1] = (pow1[i]*B) % MOD1
        pow2[i+1] = (pow2[i]*B) % MOD2
    h1 = [0]*(n+1); h2 = [0]*(n+1)
    for i,ch in enumerate(s,1):
        v = ord(ch)-96
        h1[i] = (h1[i-1]*B + v) % MOD1
        h2[i] = (h2[i-1]*B + v) % MOD2
    def get(i,j):
        return ((h1[j] - h1[i]*pow1[j-i]) % MOD1, (h2[j] - h2[i]*pow2[j-i]) % MOD2)
    def exists(L):
        seen = {}
        best = None
        for i in range(n-L+1):
            key = get(i,i+L)
            if key in seen:
                cand = s[i:i+L]
                if best is None or cand < best: best = cand
            else:
                seen[key] = i
        return best
    lo, hi = 1, n-1
    ans = ""
    while lo <= hi:
        mid = (lo+hi)//2
        t = exists(mid)
        if t is not None:
            ans = t
            lo = mid+1
        else:
            hi = mid-1
    return (ans if ans else s[0]) + "\n"

def solve_4655(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    q = next(it)
    out = []
    for _ in range(q):
        a = next(it); b = next(it); c = next(it)
        S = a + b + c
        M = max(a, b, c)
        out.append(str(min(S//2, S - M)))
    return "\n".join(out) + "\n"

def solve_4245(data: str) -> str:
    A, B = map(int, data.strip().split())
    if B == 1: return "0\n"
    return str((B - 1 + (A - 2)) // (A - 1)) + "\n"

def solve_747(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n = next(it); x0 = next(it)
    t0, t1 = [], []
    for _ in range(n):
        t, h, m = next(it), next(it), next(it)
        (t0 if t == 0 else t1).append((h, m))
    def run(start):
        lists = [sorted(t0), sorted(t1)]
        ptr = [0,0]
        heaps = [[],[]]
        x = x0
        cnt = 0
        turn = start
        while True:
            while ptr[turn] < len(lists[turn]) and lists[turn][ptr[turn]][0] <= x:
                heapq.heappush(heaps[turn], -lists[turn][ptr[turn]][1])
                ptr[turn] += 1
            if heaps[turn]:
                x += -heapq.heappop(heaps[turn])
                cnt += 1
                turn ^= 1
            else:
                break
        return cnt
    return str(max(run(0), run(1))) + "\n"

def solve_1303(data: str) -> str:
    lines = data.strip().splitlines()
    p, q, l, r = map(int, lines[0].split())
    A = [tuple(map(int, lines[i+1].split())) for i in range(p)]
    C = [tuple(map(int, lines[1+p+i].split())) for i in range(q)]
    maskA = 0
    for a,b in A:
        for t in range(a,b+1): maskA |= (1<<t)
    maskC0 = 0
    for c,d in C:
        for t in range(c,d+1): maskC0 |= (1<<t)
    ans = 0
    for t in range(l,r+1):
        if maskA & (maskC0 << t): ans += 1
    return str(ans) + "\n"

def solve_203(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0]); s = lines[1].strip()
    dqD = deque(i for i,ch in enumerate(s) if ch=='D')
    dqR = deque(i for i,ch in enumerate(s) if ch=='R')
    while dqD and dqR:
        d = dqD.popleft(); r = dqR.popleft()
        if d < r: dqD.append(d + n)
        else: dqR.append(r + n)
    return ("D" if dqD else "R") + "\n"

def solve_3177(data: str) -> str:
    lines = data.strip().splitlines()
    N, M = map(int, lines[0].split())
    start = tuple(map(int, lines[1].split()))
    swaps = [(int(a)-1, int(b)-1) for a,b in (ln.split() for ln in lines[2:2+M])]
    target = tuple(range(1, N+1))
    if start == target: return "0\n"
    front = {start:0}; back = {target:0}
    fq = deque([start]); bq = deque([target])
    while fq and bq:
        if len(fq) <= len(bq):
            cur = fq.popleft(); d = front[cur]
            for a,b in swaps:
                nxt = list(cur); nxt[a], nxt[b] = nxt[b], nxt[a]; nxt = tuple(nxt)
                if nxt in front: continue
                if nxt in back: return str(d + 1 + back[nxt]) + "\n"
                front[nxt] = d+1; fq.append(nxt)
        else:
            cur = bq.popleft(); d = back[cur]
            for a,b in swaps:
                nxt = list(cur); nxt[a], nxt[b] = nxt[b], nxt[a]; nxt = tuple(nxt)
                if nxt in back: continue
                if nxt in front: return str(d + 1 + front[nxt]) + "\n"
                back[nxt] = d+1; bq.append(nxt)
    return "0\n"

def solve_4559(data: str) -> str:
    parts = data.strip().split()
    n = int(parts[0]); arr = list(map(int, parts[1:1+n]))
    LIMIT = 10**18
    if 0 in arr: return "0\n"
    prod = 1
    for a in arr:
        if a > LIMIT // prod: return "-1\n"
        prod *= a
    return str(prod) + "\n"

