from collections import defaultdict, deque
import heapq
import math

# 1079 — Beautiful number decomposition (three solutions)

def solve_1079_v1(input_str: str) -> str:
    s = input_str.strip()

    def is_zero(x): return x == "0"
    def is_one(x): return x == "1"
    def is_odd(x): return x[-1] == '1'
    def mod4(x):
        if len(x) == 1:
            return int(x, 2)
        return int(x[-2:], 2)
    def strip(x):
        x = x.lstrip('0')
        return x if x else "0"
    def add1(x):
        x = list(x)
        i = len(x) - 1
        carry = 1
        while i >= 0 and carry:
            if x[i] == '0':
                x[i] = '1'
                carry = 0
            else:
                x[i] = '0'
                carry = 1
            i -= 1
        if carry:
            x.insert(0, '1')
        return ''.join(x)
    def sub1(x):
        x = list(x)
        i = len(x) - 1
        borrow = 1
        while i >= 0 and borrow:
            if x[i] == '1':
                x[i] = '0'
                borrow = 0
            else:
                x[i] = '1'
                borrow = 1
            i -= 1
        return strip(''.join(x))
    def div2(x):
        if len(x) == 1: return "0"
        return x[:-1]

    s = strip(s)
    cnt = 0
    while not is_zero(s):
        if is_odd(s):
            if is_one(s):
                cnt += 1
                s = "0"
            else:
                if mod4(s) == 1:
                    s = sub1(s)
                else:
                    s = add1(s)
                cnt += 1
        else:
            s = div2(s)
    return str(cnt) + "\n"

def solve_1079_v2(input_str: str) -> str:
    s = input_str.strip()[::-1]
    n = len(s)
    INF = 10**18
    dp0, dp1 = 0, INF  # dp for carry 0 and carry 1
    for i in range(n):
        b = int(s[i])
        ndp0, ndp1 = INF, INF
        for carry, dp in ((0, dp0), (1, dp1)):
            if dp >= INF: 
                continue
            v = b + carry  # 0..2
            # choose digit x in {-1,0,1} to minimize cost; next carry = (v - x)//2 when (v-x) even and in {0,2}
            # enumerate possible x
            for x in (-1, 0, 1):
                u = v - x
                if u % 2 != 0: 
                    continue
                nc = u // 2
                if nc not in (0,1): 
                    continue
                cost = dp + (1 if x != 0 else 0)
                if nc == 0:
                    if cost < ndp0: ndp0 = cost
                else:
                    if cost < ndp1: ndp1 = cost
        dp0, dp1 = ndp0, ndp1
    # after last bit, we may have remaining carry; we can resolve by writing it in NAF: carry could be 0 or 1
    ans = min(dp0, dp1 + 1)  # if carry 1 remains, it's represented as +1 at new bit
    return str(ans) + "\n"

def solve_1079_v3(input_str: str) -> str:
    s = input_str.strip()[::-1]
    carry = 0
    ans = 0
    for i, ch in enumerate(s):
        v = (ord(ch) & 1) + carry
        if v == 0:
            carry = 0
        elif v == 1:
            # lookahead to decide +1 or -1: if next bit with carry would also be 1, choose +1 (i.e., set digit -1)
            nxt = ( (ord(s[i+1]) & 1) if i+1 < len(s) else 0 ) + 0
            if nxt + carry >= 2:  # emulate run of ones
                ans += 1
                carry = 1  # choose x = -1 -> (1 - (-1)) / 2 = 1
            else:
                ans += 1
                carry = 0  # choose x = +1 -> (1 - 1)/2 = 0
        else:  # v == 2
            carry = 1
    if carry:
        ans += 1
    return str(ans) + "\n"


# 771 — Divisible differences selection (three solutions)

def solve_771_v1(input_str: str) -> str:
    it = iter(input_str.strip().split())
    n, k, m = map(int, (next(it), next(it), next(it)))
    arr = list(map(int, (next(it) for _ in range(n))))
    groups = defaultdict(list)
    for a in arr:
        groups[a % m].append(a)
    for r, lst in groups.items():
        if len(lst) >= k:
            return "Yes\n" + " ".join(map(str, lst[:k])) + " \n"
    return "No\n"

def solve_771_v2(input_str: str) -> str:
    parts = list(map(int, input_str.strip().split()))
    n, k, m = parts[:3]
    arr = parts[3:]
    buckets = [0]*m
    for a in arr:
        buckets[a % m] += 1
    target = -1
    for r, c in enumerate(buckets):
        if c >= k:
            target = r
            break
    if target == -1:
        return "No\n"
    res = []
    for a in arr:
        if a % m == target:
            res.append(a)
            if len(res) == k: break
    return "Yes\n" + " ".join(map(str, res)) + " \n"

def solve_771_v3(input_str: str) -> str:
    n, k, m = map(int, input_str.splitlines()[0].split())
    arr = list(map(int, input_str.splitlines()[1].split()))
    mod_map = defaultdict(list)
    for a in arr:
        mod_map[a % m].append(a)
    best_r = max(mod_map, key=lambda r: len(mod_map[r]))
    if len(mod_map[best_r]) < k:
        return "No\n"
    return "Yes\n" + " ".join(map(str, mod_map[best_r][:k])) + " \n"


# 3040 — Longest repeated substring (three solutions)

def solve_3040_v1(input_str: str) -> str:
    s = input_str.strip()
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0]*n
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i+k] if i+k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]; cur = sa[i]
            tmp[cur] = tmp[prev] + ((rank[prev], rank[prev+k] if prev+k < n else -1) < (rank[cur], rank[cur+k] if cur+k < n else -1))
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n-1: break
        k <<= 1
    # Kasai LCP
    lcp = [0]*n
    inv = [0]*n
    for i, p in enumerate(sa): inv[p] = i
    h = 0
    best = (0, "")  # (length, substring)
    for i in range(n):
        r = inv[i]
        if r == n-1:
            h = 0
            continue
        j = sa[r+1]
        while i+h < n and j+h < n and s[i+h] == s[j+h]:
            h += 1
        if h > 0:
            sub = s[i:i+h]
            if h > best[0] or (h == best[0] and sub < best[1]):
                best = (h, sub)
        if h: h -= 1
    return (best[1] if best[0] else s[0]) + "\n"

def solve_3040_v2(input_str: str) -> str:
    s = input_str.strip()
    n = len(s)
    MOD1, MOD2 = (10**9+7, 10**9+9)
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
        x1 = (h1[j] - h1[i]*pow1[j-i]) % MOD1
        x2 = (h2[j] - h2[i]*pow2[j-i]) % MOD2
        return (x1,x2)
    def ok(L):
        seen = {}
        best = None
        for i in range(n-L+1):
            key = get(i,i+L)
            if key in seen:
                cand = s[i:i+L]
                if best is None or cand < best:
                    best = cand
            else:
                seen[key] = i
        return best
    lo, hi = 1, n-1
    ans = ""
    while lo <= hi:
        mid = (lo+hi)//2
        t = ok(mid)
        if t is not None:
            ans = t
            lo = mid+1
        else:
            hi = mid-1
    return (ans if ans else s[0]) + "\n"

def solve_3040_v3(input_str: str) -> str:
    s = input_str.strip()
    # Suffix Automaton
    class SAM:
        def __init__(self):
            self.link = [-1]
            self.next = [dict()]
            self.len = [0]
            self.occur = [0]
            self.last = 0
        def extend(self, c):
            cur = len(self.len)
            self.len.append(self.len[self.last]+1)
            self.next.append({})
            self.link.append(0)
            self.occur.append(1)
            p = self.last
            while p >= 0 and c not in self.next[p]:
                self.next[p][c] = cur
                p = self.link[p]
            if p == -1:
                self.link[cur] = 0
            else:
                q = self.next[p][c]
                if self.len[p]+1 == self.len[q]:
                    self.link[cur] = q
                else:
                    clone = len(self.len)
                    self.len.append(self.len[p]+1)
                    self.next.append(self.next[q].copy())
                    self.link.append(self.link[q])
                    self.occur.append(0)
                    while p >= 0 and self.next[p].get(c, -1) == q:
                        self.next[p][c] = clone
                        p = self.link[p]
                    self.link[q] = self.link[cur] = clone
            self.last = cur
    sam = SAM()
    for ch in s:
        sam.extend(ch)
    # count occurrences using topo by len
    order = sorted(range(len(sam.len)), key=lambda i: sam.len[i], reverse=True)
    for v in order:
        if sam.link[v] != -1:
            sam.occur[sam.link[v]] += sam.occur[v]
    # find max length with occur>=2 and lexicographically smallest
    best_len = 0
    # DFS lexicographically to retrieve smallest for best_len
    # First compute best_len
    for v in range(len(sam.len)):
        if sam.occur[v] >= 2:
            best_len = max(best_len, sam.len[v])
    if best_len == 0:
        return s[0] + "\n"
    res = []
    def dfs(u, depth):
        nonlocal res
        if depth == best_len:
            return True
        for ch in map(chr, range(97,123)):
            if ch in sam.next[u]:
                v = sam.next[u][ch]
                # we need that there's a path to some state with occur>=2 and length >= best_len
                # quick pruning: find the maximum length reachable in this subtree with occur>=2
                # Use a stack to climb following greedily; if occur[v] >=2 and len[v] >= depth+1 it's ok,
                # but we may need longer; however sam.len gives max length for the state.
                if sam.occur[v] >= 2:
                    # there exists a substring ending here occurring >=2 with length >= sam.len[v]
                    if sam.len[v] >= depth+1:
                        res.append(ch)
                        if dfs(v, depth+1):
                            return True
                        res.pop()
        return False
    dfs(0,0)
    return "".join(res) + "\n"


# 4655 — Candies (three solutions)

def solve_4655_v1(input_str: str) -> str:
    it = iter(map(int, input_str.strip().split()))
    q = next(it)
    out = []
    for _ in range(q):
        a = next(it); b = next(it); c = next(it)
        out.append(str((a+b+c)//2))
    return "\n".join(out) + "\n"

def solve_4655_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    q = int(lines[0])
    out = []
    for i in range(1, q+1):
        a,b,c = map(int, lines[i].split())
        out.append(str((a+b+c)//2))
    return "\n".join(out) + "\n"

def solve_4655_v3(input_str: str) -> str:
    nums = list(map(int, input_str.strip().split()))
    q = nums[0]
    res = []
    for i in range(q):
        a,b,c = nums[1+3*i:1+3*(i+1)]
        res.append((a+b+c)//2)
    return "\n".join(map(str,res)) + "\n"


# 4245 — Power Strips (three solutions)

def solve_4245_v1(input_str: str) -> str:
    A, B = map(int, input_str.strip().split())
    if B == 1: return "0\n"
    need = (B - 1 + (A - 2)) // (A - 1)
    return str(need) + "\n"

def solve_4245_v2(input_str: str) -> str:
    A, B = map(int, input_str.strip().split())
    sockets = 1
    cnt = 0
    while sockets < B:
        sockets += (A - 1)
        cnt += 1
    return str(cnt) + "\n"

def solve_4245_v3(input_str: str) -> str:
    A, B = map(int, input_str.strip().split())
    return ( "0\n" if B == 1 else f"{(B-2)//(A-1)+1}\n" )


# 747 — Om Nom (three solutions)

def solve_747_v1(input_str: str) -> str:
    it = iter(map(int, input_str.strip().split()))
    n = next(it); x0 = next(it)
    candies = [tuple((next(it), next(it), next(it))) for _ in range(n)]  # (t,h,m)
    def run(start_type):
        x = x0
        cnt = 0
        ts = [[],[]]
        for t,h,m in candies:
            ts[t].append((h,m))
        ts[0].sort(); ts[1].sort()
        idx = [0,0]
        heaps = [[],[]]  # max-heaps via negative
        cur = start_type
        while True:
            while idx[cur] < len(ts[cur]) and ts[cur][idx[cur]][0] <= x:
                h,m = ts[cur][idx[cur]]
                heapq.heappush(heaps[cur], (-m,m))
                idx[cur]+=1
            if heaps[cur]:
                m = heapq.heappop(heaps[cur])[1]
                x += m
                cnt += 1
                cur ^= 1
            else:
                break
        return cnt
    return str(max(run(0), run(1))) + "\n"

def solve_747_v2(input_str: str) -> str:
    data = list(map(int, input_str.strip().split()))
    n, x0 = data[:2]
    arr = [tuple(data[2+3*i:2+3*i+3]) for i in range(n)]
    def simulate(start):
        used = [False]*n
        x = x0
        cur = start
        cnt = 0
        while True:
            best = -1
            best_m = -1
            for i,(t,h,m) in enumerate(arr):
                if not used[i] and t == cur and h <= x and m > best_m:
                    best_m = m
                    best = i
            if best == -1:
                break
            used[best] = True
            x += arr[best][2]
            cnt += 1
            cur ^= 1
        return cnt
    return str(max(simulate(0), simulate(1))) + "\n"

def solve_747_v3(input_str: str) -> str:
    it = iter(map(int, input_str.strip().split()))
    n = next(it); x0 = next(it)
    t0, t1 = [], []
    for _ in range(n):
        t,h,m = next(it), next(it), next(it)
        (t0 if t==0 else t1).append((h,m))
    def run(start):
        x = x0
        cnt = 0
        lists = [sorted(t0), sorted(t1)]
        ptr = [0,0]
        pools = [[],[]]
        turn = start
        while True:
            while ptr[turn] < len(lists[turn]) and lists[turn][ptr[turn]][0] <= x:
                heapq.heappush(pools[turn], -lists[turn][ptr[turn]][1])
                ptr[turn]+=1
            if pools[turn]:
                x += -heapq.heappop(pools[turn])
                cnt += 1
                turn ^= 1
            else:
                break
        return cnt
    return str(max(run(0), run(1))) + "\n"


# 1303 — Little X and Little Z (three solutions)

def solve_1303_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p,q,l,r = map(int, lines[0].split())
    A = [tuple(map(int, lines[i+1].split())) for i in range(p)]
    C = [tuple(map(int, lines[1+p+i].split())) for i in range(q)]
    MAXT = 2000+1000+1000
    z = [0]*(MAXT+1)
    for a,b in A:
        z[a:b+1] = [1]*(b-a+1)
    ans = 0
    for t in range(l, r+1):
        ok = False
        for c,d in C:
            cs, de = c+t, d+t
            if cs > MAXT: break
            if de > MAXT: de = MAXT
            # any overlap?
            if any(z[cs:de+1]):
                ok = True
                break
        if ok: ans += 1
    return str(ans) + "\n"

def solve_1303_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p,q,l,r = map(int, lines[0].split())
    A = [tuple(map(int, lines[i+1].split())) for i in range(p)]
    C = [tuple(map(int, lines[1+p+i].split())) for i in range(q)]
    def overlaps(t):
        i=j=0
        AA=sorted(A); CC=sorted((c+t,d+t) for c,d in C)
        while i < len(AA) and j < len(CC):
            a,b = AA[i]
            c,d = CC[j]
            if b < c: i += 1
            elif d < a: j += 1
            else: 
                return True
        return False
    ans = sum(1 for t in range(l,r+1) if overlaps(t))
    return str(ans) + "\n"

def solve_1303_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    p,q,l,r = map(int, lines[0].split())
    A = [tuple(map(int, lines[i+1].split())) for i in range(p)]
    C = [tuple(map(int, lines[1+p+i].split())) for i in range(q)]
    MAXT = 2005
    maskA = 0
    for a,b in A:
        for t in range(a,b+1):
            maskA |= (1<<t)
    ans = 0
    for t in range(l, r+1):
        maskC = 0
        for c,d in C:
            for u in range(c+t, d+t+1):
                if u >= 0:
                    maskC |= (1<<u)
        if maskA & maskC:
            ans += 1
    return str(ans) + "\n"


# 203 — ACM vote outcome (three solutions)

def solve_203_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0]); s = lines[1].strip()
    dqD = deque(i for i,ch in enumerate(s) if ch=='D')
    dqR = deque(i for i,ch in enumerate(s) if ch=='R')
    while dqD and dqR:
        d = dqD.popleft()
        r = dqR.popleft()
        if d < r:
            dqD.append(d + n)
        else:
            dqR.append(r + n)
    return ("D" if dqD else "R") + "\n"

def solve_203_v2(input_str: str) -> str:
    n, s = int(input_str.splitlines()[0]), input_str.splitlines()[1].strip()
    banD = banR = 0
    alive = list(s)
    while True:
        next_round = []
        nd = nr = 0
        for ch in alive:
            if ch == 'D':
                if banD:
                    banD -= 1
                else:
                    next_round.append('D'); nr += 1; banR += 1
            else:
                if banR:
                    banR -= 1
                else:
                    next_round.append('R'); nd += 1; banD += 1
        if nd == 0: return "R\n"
        if nr == 0: return "D\n"
        alive = next_round

def solve_203_v3(input_str: str) -> str:
    n = int(input_str.splitlines()[0]); s = input_str.splitlines()[1].strip()
    diff = 0
    alive = [1]*n
    while True:
        d_alive = r_alive = 0
        for i,ch in enumerate(s):
            if not alive[i]: continue
            if ch == 'D':
                if diff < 0:
                    alive[i] = 0
                else:
                    diff += 1
            else:  # 'R'
                if diff > 0:
                    alive[i] = 0
                else:
                    diff -= 1
        for i in range(n):
            if alive[i]:
                if s[i]=='D': d_alive += 1
                else: r_alive += 1
        if d_alive == 0: return "R\n"
        if r_alive == 0: return "D\n"


# 3177 — Arrange (minimum swaps with allowed swaps) (three solutions)

def solve_3177_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    N, M = map(int, lines[0].split())
    start = tuple(map(int, lines[1].split()))
    swaps = [tuple(map(int, ln.split())) for ln in lines[2:2+M]]
    swaps = [(a-1,b-1) for a,b in swaps]
    target = tuple(range(1, N+1))
    if start == target: return "0\n"
    from collections import deque
    q = deque([start])
    dist = {start: 0}
    while q:
        cur = q.popleft()
        d = dist[cur]
        for a,b in swaps:
            nxt = list(cur)
            nxt[a], nxt[b] = nxt[b], nxt[a]
            nxt = tuple(nxt)
            if nxt not in dist:
                if nxt == target:
                    return str(d+1) + "\n"
                dist[nxt] = d+1
                q.append(nxt)
    return "0\n"

def solve_3177_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    N, M = map(int, lines[0].split())
    start = tuple(map(int, lines[1].split()))
    swaps = [tuple(map(int, ln.split())) for ln in lines[2:2+M]]
    swaps = [(a-1,b-1) for a,b in swaps]
    target = tuple(range(1, N+1))
    if start == target: return "0\n"
    from collections import deque
    front = {start:0}
    back = {target:0}
    fq = deque([start]); bq = deque([target])
    while fq and bq:
        if len(fq) <= len(bq):
            cur = fq.popleft()
            d = front[cur]
            for a,b in swaps:
                nxt = list(cur); nxt[a], nxt[b] = nxt[b], nxt[a]; nxt = tuple(nxt)
                if nxt in front: continue
                if nxt in back: return str(d + 1 + back[nxt]) + "\n"
                front[nxt] = d+1; fq.append(nxt)
        else:
            cur = bq.popleft()
            d = back[cur]
            for a,b in swaps:
                nxt = list(cur); nxt[a], nxt[b] = nxt[b], nxt[a]; nxt = tuple(nxt)
                if nxt in back: continue
                if nxt in front: return str(d + 1 + front[nxt]) + "\n"
                back[nxt] = d+1; bq.append(nxt)
    return "0\n"

def solve_3177_v3(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    N, M = map(int, lines[0].split())
    start = tuple(map(int, lines[1].split()))
    swaps = [tuple(map(int, ln.split())) for ln in lines[2:2+M]]
    swaps = [(a-1,b-1) for a,b in swaps]
    target = tuple(range(1, N+1))
    if start == target: return "0\n"
    # A* with heuristic: number of misplaced positions cannot be swapped arbitrarily, but we use admissible h=ceil(cycles distance)
    def heuristic(p):
        # number of cycles in permutation mapping p -> target
        visited = [False]*N
        cnt = 0
        pos = [0]*(N+1)
        for i,v in enumerate(p):
            pos[v] = i
        # This heuristic will be zero; for simplicity, use zero to keep correctness.
        return 0
    import heapq
    pq = [(heuristic(start), 0, start)]
    dist = {start: 0}
    while pq:
        f, g, cur = heapq.heappop(pq)
        if cur == target: return str(g) + "\n"
        if g != dist[cur]: continue
        for a,b in swaps:
            nxt = list(cur); nxt[a], nxt[b] = nxt[b], nxt[a]; nxt = tuple(nxt)
            ng = g + 1
            if nxt not in dist or ng < dist[nxt]:
                dist[nxt] = ng
                heapq.heappush(pq, (ng + heuristic(nxt), ng, nxt))
    return "0\n"


# 4559 — Product with overflow cap (three solutions)

def solve_4559_v1(input_str: str) -> str:
    it = iter(map(int, input_str.strip().split()))
    n = next(it)
    A = [next(it) for _ in range(n)]
    LIMIT = 10**18
    if any(a == 0 for a in A): return "0\n"
    prod = 1
    for a in A:
        if a > LIMIT // prod:
            return "-1\n"
        prod *= a
    return str(prod) + "\n"

def solve_4559_v2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n = int(lines[0]); arr = list(map(int, lines[1].split()))
    LIMIT = 10**18
    if 0 in arr: return "0\n"
    prod = 1
    for a in arr:
        if prod > LIMIT // a:
            return "-1\n"
        prod *= a
    return f"{prod}\n"

def solve_4559_v3(input_str: str) -> str:
    parts = input_str.strip().split()
    n = int(parts[0])
    LIMIT = 10**18
    prod = 1
    for i in range(1, n+1):
        a = int(parts[i])
        if a == 0:
            return "0\n"
        if prod > LIMIT // a:
            return "-1\n"
        prod *= a
    return str(prod) + "\n"

