def solve_4655(inp: str) -> str:
    """
    For each query with piles a, b, c:
    The optimal equal share is min((a+b+c)//2, a+b+c - min(a,b,c)).
    """
    it = iter(inp.strip().split())
    q = int(next(it))
    out = []
    for _ in range(q):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        total = a + b + c
        ans = min(total // 2, total - min(a, b, c))
        out.append(str(ans))
    return "\n".join(out) + "\n"
