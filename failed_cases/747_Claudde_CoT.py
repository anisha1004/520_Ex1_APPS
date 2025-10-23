def solve_747_v1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    n, x = map(int, lines[0].split())
    candies = []
    for i in range(1, n + 1):
        t, h, m = map(int, lines[i].split())
        candies.append((h, m, t))
    
    from functools import lru_cache
    
    def get_jump(mask):
        jump = x
        for i in range(n):
            if mask & (1 << i):
                jump += candies[i][1]
        return jump
    
    @lru_cache(maxsize=None)
    def dfs(mask, last_type):
        jump = get_jump(mask)
        max_candies = 0
        for i in range(n):
            if mask & (1 << i):
                continue
            h, m, t = candies[i]
            if jump >= h and last_type != t:
                new_mask = mask | (1 << i)
                candies_eaten = 1 + dfs(new_mask, t)
                max_candies = max(max_candies, candies_eaten)
        return max_candies
    
    result = dfs(0, -1)
    return f"{result}\n"
