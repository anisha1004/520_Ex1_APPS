from collections import defaultdict, deque
import heapq
import math
import sys

def solve_1079_v1(s: str) -> str:
    s = s.strip()
    n = len(s)
    ans = 0
    carry = 0
    for j in range(n - 1, -1, -1):
        b = 1 if s[j] == '1' else 0
        x = b + carry
        if (x & 1) == 0:
            carry = x >> 1
        else:
            next_bit = 1 if j - 1 >= 0 and s[j - 1] == '1' else 0
            if next_bit == 1:
                ans += 1
                carry = 1
            else:
                ans += 1
                carry = 0
    if carry:
        ans += 1
    return f"{ans}\n"

def solve_1079_v2(s: str) -> str:
    s = s.strip()
    INF = 10**18
    dp0, dp1 = 0, INF
    for j in range(len(s) - 1, -1, -1):
        b = 1 if s[j] == '1' else 0
        ndp0, ndp1 = INF, INF
        x = b
        if (x & 1) == 0:
            if x == 0:
                ndp0 = min(ndp0, dp0)
            else:
                ndp1 = min(ndp1, dp0)
        else:
            ndp0 = min(ndp0, dp0 + 1)
            ndp1 = min(ndp1, dp0 + 1)
        if dp1 < INF:
            x = b + 1
            if (x & 1) == 0:
                if x == 2:
                    ndp1 = min(ndp1, dp1)
            else:
                ndp0 = min(ndp0, dp1 + 1)
                ndp1 = min(ndp1, dp1 + 1)
        dp0, dp1 = ndp0, ndp1
    ans = min(dp0, dp1 + 1 if dp1 < INF else INF)
    return f"{ans}\n"

def solve_1079_v3(s: str) -> str:
    s = s.strip()
    n = len(s)
    ans = 0
    carry = 0
    j = n - 1
    while j >= 0:
        b = 1 if s[j] == '1' else 0
        x = b + carry
        if (x & 1) == 0:
            carry = x >> 1
            j -= 1
        else:
            next_is_one = j - 1 >= 0 and s[j - 1] == '1'
            if next_is_one:
                ans += 1
                carry = 1
                j -= 1
                while j >= 0 and s[j] == '1':
                    j -= 1
            else:
                ans += 1
                carry = 0
                j -= 1
    if carry:
        ans += 1
    return f"{ans}\n"

def solve_771_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n, k, m = next(it), next(it), next(it)
    a = [next(it) for _ in range(n)]
    buckets = defaultdict(list)
    for v in a:
        buckets[v % m].append(v)
    for r, vals in buckets.items():
        if len(vals) >= k:
            return "Yes\n" + " ".join(map(str, vals[:k])) + " "
    return "No"

def solve_771_v2(data: str) -> str:
    parts = list(map(int, data.strip().split()))
    n, k, m = parts[0], parts[1], parts[2]
    a = parts[3:]
    cnt = [0]*m
    for v in a:
        cnt[v % m] += 1
    for r in range(m):
        if cnt[r] >= k:
            res = []
            for v in a:
                if v % m == r:
                    res.append(v)
                    if len(res) == k: break
            return "Yes\n" + " ".join(map(str, res)) + " "
    return "No"

def solve_771_v3(data: str) -> str:
    import itertools
    it = iter(map(int, data.strip().split()))
    n, k, m = next(it), next(it), next(it)
    a = [next(it) for _ in range(n)]
    a_sorted = sorted(a, key=lambda x: x % m)
    for r, group in itertools.groupby(a_sorted, key=lambda x: x % m):
        group = list(group)
        if len(group) >= k:
            return "Yes\n" + " ".join(map(str, group[:k])) + " "
    return "No"

def solve_3040_v1(s: str) -> str:
    s = s.strip()
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0]*n
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i+k] if i+k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev, cur = sa[i-1], sa[i]
            tmp[cur] = tmp[prev] + ((rank[prev], rank[prev+k] if prev+k < n else -1) < (rank[cur], rank[cur+k] if cur+k < n else -1))
        rank = tmp[:]
        if rank[sa[-1]] == n-1: break
        k <<= 1
    lcp = [0]*n
    h = 0
    pos = [0]*n
    for i, p in enumerate(sa): pos[p] = i
    for i in range(n):
        if pos[i] == n-1:
            h = 0
            continue
        j = sa[pos[i]+1]
        while i+h < n and j+h < n and s[i+h] == s[j+h]: h += 1
        lcp[pos[i]] = h
        if h: h -= 1
    best_len = max(lcp)
    if best_len == 0: return s[0] + "\n"
    cands = []
    for i in range(n-1):
        if lcp[i] == best_len:
            cands.append(s[sa[i]:sa[i]+best_len])
    return min(cands) + "\n"

def solve_3040_v2(s: str) -> str:
    s = s.strip()
    n = len(s)
    mod1, mod2 = 10**9+7, 10**9+9
    base = 911382323
    p1 = [1]*(n+1)
    p2 = [1]*(n+1)
    for i in range(n):
        p1[i+1] = (p1[i]*base) % mod1
        p2[i+1] = (p2[i]*base) % mod2
    h1 = [0]*(n+1)
    h2 = [0]*(n+1)
    for i,ch in enumerate(s):
        v = ord(ch)
        h1[i+1] = (h1[i]*base + v) % mod1
        h2[i+1] = (h2[i]*base + v) % mod2
    def get(i,j):
        x1 = (h1[j]-h1[i]*p1[j-i])%mod1
        x2 = (h2[j]-h2[i]*p2[j-i])%mod2
        return (x1,x2)
    def exists(L):
        seen = {}
        best = None
        for i in range(n-L+1):
            key = get(i,i+L)
            if key in seen:
                cand = s[i:i+L]
                if best is None or cand < best:
                    best = cand
            else:
                seen[key]=i
        return best
    lo, hi = 1, n-1
    ans = ""
    while lo <= hi:
        mid = (lo+hi)//2
        t = exists(mid)
        if t:
            ans = t
            lo = mid+1
        else:
            hi = mid-1
    return ans + "\n"

def solve_3040_v3(s: str) -> str:
    s = s.strip()
    class SAM:
        def __init__(self):
            self.next = [{}]
            self.link = [-1]
            self.len = [0]
            self.occ = [0]
        def extend(self, c):
            cur = len(self.next)
            self.next.append({})
            self.len.append(self.len[-1]+1)
            self.link.append(0)
            self.occ.append(1)
            p = self.last
            while p!=-1 and c not in self.next[p]:
                self.next[p][c]=cur
                p = self.link[p]
            if p==-1:
                self.link[cur]=0
            else:
                q = self.next[p][c]
                if self.len[p]+1==self.len[q]:
                    self.link[cur]=q
                else:
                    clone = len(self.next)
                    self.next.append(self.next[q].copy())
                    self.len.append(self.len[p]+1)
                    self.link.append(self.link[q])
                    self.occ.append(0)
                    while p!=-1 and self.next[p].get(c, -1)==q:
                        self.next[p][c]=clone
                        p = self.link[p]
                    self.link[q]=self.link[cur]=clone
            self.last = cur
        def build(self, s):
            self.last = 0
            for ch in s:
                self.extend(ch)
    sam = SAM()
    sam.build(s)
    order = sorted(range(len(sam.len)), key=lambda i: sam.len[i])
    for v in reversed(order):
        if sam.link[v]!=-1:
            sam.occ[sam.link[v]] += sam.occ[v]
    target = 0
    for i in range(len(sam.len)):
        if sam.occ[i] >= 2 and sam.len[i] > target:
            target = sam.len[i]
    if target == 0:
        return s[0] + "\n"
    res = []
    state = 0
    need = target
    while need:
        for ch in map(chr, range(97,123)):
            if ch in sam.next[state]:
                v = sam.next[state][ch]
                if sam.occ[v] >= 2:
                    res.append(ch)
                    state = v
                    need -= 1
                    break
        else:
            break
    return "".join(res) + "\n"

def solve_4655_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    q = next(it)
    out = []
    for _ in range(q):
        a,b,c = next(it), next(it), next(it)
        s = a+b+c
        out.append(str(min(s//2, s - max(a,b,c))))
    return "\n".join(out) + "\n"

def solve_4655_v2(data: str) -> str:
    lines = list(map(int, data.strip().split()))
    q = lines[0]
    out = []
    idx = 1
    for _ in range(q):
        x = sorted(lines[idx:idx+3])
        idx += 3
        out.append(str(min((x[0]+x[1]+x[2])//2, x[0]+x[1])))
    return "\n".join(out) + "\n"

def solve_4655_v3(data: str) -> str:
    nums = list(map(int, data.strip().split()))
    q = nums[0]
    res = []
    i = 1
    for _ in range(q):
        a,b,c = nums[i], nums[i+1], nums[i+2]
        i += 3
        m = max(a,b,c)
        res.append(str((a+b+c - m) if m >= (a+b+c-m) else (a+b+c)//2))
    return "\n".join(res) + "\n"

def solve_4245_v1(s: str) -> str:
    A,B = map(int, s.strip().split())
    if B <= 1: return "0\n"
    need = B-1
    return f"{(need + (A-2))//(A-1)}\n"

def solve_4245_v2(s: str) -> str:
    A,B = map(int, s.strip().split())
    x = 0
    sockets = 1
    while sockets < B:
        x += 1
        sockets += A-1
    return f"{x}\n"

def solve_4245_v3(s: str) -> str:
    A,B = map(int, s.strip().split())
    return ("0\n" if B<=1 else f"{math.ceil((B-1)/(A-1))}\n")

def solve_747_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n, x = next(it), next(it)
    C, F = [], []
    for _ in range(n):
        t,h,m = next(it), next(it), next(it)
        (F if t==1 else C).append((h,m))
    C.sort(); F.sort()
    def run(start):
        i=j=0
        hc,hf=[],[]
        cur=x
        t=start
        eaten=0
        while True:
            if t==0:
                while i<len(C) and C[i][0]<=cur:
                    heapq.heappush(hc, -C[i][1]); i+=1
                if not hc: break
                cur += -heapq.heappop(hc); eaten+=1; t=1
            else:
                while j<len(F) and F[j][0]<=cur:
                    heapq.heappush(hf, -F[j][1]); j+=1
                if not hf: break
                cur += -heapq.heappop(hf); eaten+=1; t=0
        return eaten
    return f"{max(run(0), run(1))}\n"

def solve_747_v2(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n, x = next(it), next(it)
    arr = [[],[]]
    for _ in range(n):
        t,h,m = next(it), next(it), next(it)
        arr[t].append((h,m))
    for t in (0,1): arr[t].sort()
    def simulate(start):
        idx=[0,0]
        heaps=[[],[]]
        cur=x
        t=start
        ans=0
        while True:
            while idx[t] < len(arr[t]) and arr[t][idx[t]][0] <= cur:
                heapq.heappush(heaps[t], -arr[t][idx[t]][1]); idx[t]+=1
            if not heaps[t]: break
            cur += -heapq.heappop(heaps[t]); ans+=1; t^=1
        return ans
    return f"{max(simulate(0), simulate(1))}\n"

def solve_747_v3(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n, x = next(it), next(it)
    A = [[] for _ in range(2)]
    for _ in range(n):
        t,h,m = next(it), next(it), next(it)
        A[t].append((h,m))
    A[0].sort(); A[1].sort()
    def go(start):
        cur=x; i=[0,0]; heap=[[],[]]; ans=0; t=start
        while True:
            added=False
            while i[t]<len(A[t]) and A[t][i[t]][0]<=cur:
                heapq.heappush(heap[t], -A[t][i[t]][1]); i[t]+=1; added=True
            if heap[t]:
                cur += -heapq.heappop(heap[t]); ans+=1; t^=1
            else:
                if not added: break
                t^=1
        return ans
    return f"{max(go(0), go(1))}\n"

def solve_1303_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    p,q,l,r = next(it), next(it), next(it), next(it)
    Z = [tuple((next(it), next(it))) for _ in range(p)]
    X = [tuple((next(it), next(it))) for _ in range(q)]
    maxT = 2001
    z = 0
    for a,b in Z:
        z |= ((1 << (b-a+1)) - 1) << a
    x = 0
    for c,d in X:
        x |= ((1 << (d-c+1)) - 1) << c
    ans=0
    for t in range(l, r+1):
        if z & (x<<t): ans+=1
    return f"{ans}\n"

def solve_1303_v2(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    p,q,l,r = next(it), next(it), next(it), next(it)
    Z = [tuple((next(it), next(it))) for _ in range(p)]
    X = [tuple((next(it), next(it))) for _ in range(q)]
    maxv = 2005
    cover = [0]*(maxv+1)
    for a,b in Z:
        cover[a]+=1
        cover[b+1]-=1
    for i in range(1,len(cover)):
        cover[i]+=cover[i-1]
    mark = [0]*(maxv+1)
    for c,d in X:
        mark[c]+=1
        mark[d+1]-=1
    for i in range(1,len(mark)):
        mark[i]+=mark[i-1]
    xs = [1 if mark[i]>0 else 0 for i in range(len(mark))]
    zs = [1 if cover[i]>0 else 0 for i in range(len(cover))]
    ans=0
    for t in range(l,r+1):
        ok=False
        i=0
        while i<len(xs) and not ok:
            if xs[i] and i+t<len(zs) and zs[i+t]:
                ok=True
            i+=1
        if ok: ans+=1
    return f"{ans}\n"

def solve_1303_v3(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    p,q,l,r = next(it), next(it), next(it), next(it)
    Z = [tuple((next(it), next(it))) for _ in range(p)]
    X = [tuple((next(it), next(it))) for _ in range(q)]
    ans=0
    for t in range(l,r+1):
        ok=False
        for a,b in Z:
            if ok: break
            for c,d in X:
                if not (b < c+t or d+t < a):
                    ok=True
                    break
        if ok: ans+=1
    return f"{ans}\n"

def solve_203_v1(data: str) -> str:
    it = iter(data.strip().split())
    n = int(next(it))
    s = next(it).strip()
    qD, qR = deque(), deque()
    for i,ch in enumerate(s):
        (qD if ch=='D' else qR).append(i)
    while qD and qR:
        d = qD.popleft()
        r = qR.popleft()
        if d < r:
            qD.append(d+n)
        else:
            qR.append(r+n)
    return ("D\n" if qD else "R\n")

def solve_203_v2(data: str) -> str:
    n = int(data.strip().split()[0])
    s = data.strip().split()[1]
    banD = banR = 0
    aliveD = s.count('D')
    aliveR = n - aliveD
    q = deque(s)
    while aliveD and aliveR:
        ch = q.popleft()
        if ch=='D':
            if banD: banD-=1
            else:
                banR+=1
                q.append('D')
                aliveR-=1
        else:
            if banR: banR-=1
            else:
                banD+=1
                q.append('R')
                aliveD-=1
    return ("D\n" if aliveD else "R\n")

def solve_203_v3(data: str) -> str:
    n = int(data.strip().split()[0])
    s = data.strip().split()[1]
    idx = deque(range(n))
    arr = list(s)
    banD = banR = 0
    aliveD = arr.count('D')
    aliveR = n - aliveD
    while aliveD and aliveR:
        i = idx.popleft()
        if arr[i]=='D':
            if banD: banD-=1
            else:
                banR+=1
                idx.append(i+n)
                aliveR-=1
        else:
            if banR: banR-=1
            else:
                banD+=1
                idx.append(i+n)
                aliveD-=1
    return ("D\n" if aliveD else "R\n")

def solve_3177_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    N, M = next(it), next(it)
    perm = tuple(next(it) for _ in range(N))
    swaps = [tuple((next(it)-1, next(it)-1)) for _ in range(M)]
    goal = tuple(range(1, N+1))
    if perm == goal: return "0\n"
    q = deque([perm])
    dist = {perm:0}
    while q:
        cur = q.popleft()
        d = dist[cur]
        for a,b in swaps:
            lst = list(cur)
            lst[a], lst[b] = lst[b], lst[a]
            nxt = tuple(lst)
            if nxt not in dist:
                if nxt == goal: return f"{d+1}\n"
                dist[nxt]=d+1
                q.append(nxt)
    return "0\n"

def solve_3177_v2(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    N, M = next(it), next(it)
    start = tuple(next(it) for _ in range(N))
    swaps = [tuple((next(it)-1, next(it)-1)) for _ in range(M)]
    goal = tuple(range(1,N+1))
    if start == goal: return "0\n"
    front = {start:0}
    back = {goal:0}
    qf = deque([start])
    qb = deque([goal])
    while qf and qb:
        if len(qf) <= len(qb):
            for _ in range(len(qf)):
                cur = qf.popleft()
                d = front[cur]
                for a,b in swaps:
                    lst = list(cur)
                    lst[a], lst[b] = lst[b], lst[a]
                    nxt = tuple(lst)
                    if nxt in front: continue
                    if nxt in back: return f"{d+1+back[nxt]}\n"
                    front[nxt]=d+1
                    qf.append(nxt)
        else:
            for _ in range(len(qb)):
                cur = qb.popleft()
                d = back[cur]
                for a,b in swaps:
                    lst = list(cur)
                    lst[a], lst[b] = lst[b], lst[a]
                    nxt = tuple(lst)
                    if nxt in back: continue
                    if nxt in front: return f"{d+1+front[nxt]}\n"
                    back[nxt]=d+1
                    qb.append(nxt)
    return "0\n"

def solve_3177_v3(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    N, M = next(it), next(it)
    start = tuple(next(it) for _ in range(N))
    swaps = [tuple((next(it)-1, next(it)-1)) for _ in range(M)]
    goal = tuple(range(1,N+1))
    if start == goal: return "0\n"
    import heapq
    def h(state):
        return sum(1 for i,v in enumerate(state,1) if i!=v)
    pq = [(h(start), 0, start)]
    seen = {start:0}
    while pq:
        _, g, cur = heapq.heappop(pq)
        if cur == goal: return f"{g}\n"
        if seen[cur] != g: continue
        for a,b in swaps:
            lst = list(cur)
            lst[a], lst[b] = lst[b], lst[a]
            nxt = tuple(lst)
            ng = g+1
            if nxt not in seen or ng < seen[nxt]:
                seen[nxt]=ng
                heapq.heappush(pq, (ng + h(nxt), ng, nxt))
    return "0\n"

def solve_4559_v1(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    if 0 in a: return "0\n"
    LIM = 10**18
    prod = 1
    for v in a:
        if v > LIM // prod: return "-1\n"
        prod *= v
    return f"{prod}\n"

def solve_4559_v2(data: str) -> str:
    nums = list(map(int, data.strip().split()))
    n = nums[0]
    arr = nums[1:]
    LIM = 10**18
    if any(v==0 for v in arr): return "0\n"
    s = sum(math.log10(v) for v in arr)
    if s > math.log10(LIM) + 1e-12: return "-1\n"
    prod = 1
    for v in arr:
        if v > LIM // prod: return "-1\n"
        prod *= v
    return f"{prod}\n"

def solve_4559_v3(data: str) -> str:
    it = iter(map(int, data.strip().split()))
    n = next(it)
    LIM = 10**18
    prod = 1
    zero = False
    for _ in range(n):
        v = next(it)
        if v == 0: zero = True
        if not zero:
            if v > LIM // max(prod,1): return "-1\n"
            prod *= v
    return ("0\n" if zero else f"{prod}\n")


