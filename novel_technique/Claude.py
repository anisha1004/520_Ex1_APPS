def solve_1079_v1(input_str: str) -> str:
   s = input_str.strip()
   s = '0' + s + '0'
   count = 0
   i = 1
   while i < len(s):
       if s[i] == '1':
           while i < len(s) and s[i] == '1':
               i += 1
           if i < len(s) and s[i] == '0':
               count += 1
           i += 1
       else:
           i += 1
   return f"{count}\n"


def solve_771_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, k, m = map(int, lines[0].split())
   a = list(map(int, lines[1].split()))
  
   mods = [[] for _ in range(m)]
   for num in a:
       mods[num % m].append(num)
  
   for lst in mods:
       if len(lst) >= k:
           return "Yes\n" + ' '.join(map(str, lst[:k])) + " \n"
   return "No\n"


def solve_3040_v1(input_str: str) -> str:
   s = input_str.strip()
   n = len(s)
  
   for length in range(n, 0, -1):
       seen = {}
       candidates = []
       for i in range(n - length + 1):
           substr = s[i:i+length]
           if substr in seen:
               candidates.append(substr)
           seen[substr] = True
       if candidates:
           return f"{min(candidates)}\n"
   return ""


def solve_4655_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   q = int(lines[0])
   results = []
   for i in range(1, q + 1):
       a, b, c = map(int, lines[i].split())
       total = a + b + c
       results.append(str(total // 2))
   return '\n'.join(results) + '\n'


def solve_4245_v1(input_str: str) -> str:
   a, b = map(int, input_str.strip().split())
   if b <= 1:
       return "0\n"
   return f"{(b - 2 + a - 1) // (a - 1)}\n"


def solve_747_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, x = map(int, lines[0].split())
   candies = []
   for i in range(1, n + 1):
       t, h, m = map(int, lines[i].split())
       candies.append((h, m, t))
  
   candies.sort()
  
   dp = {}
   dp[(0, -1, x)] = 0
  
   for idx in range(n):
       h, m, t = candies[idx]
       new_dp = dict(dp)
      
       for (eaten_mask, last_type, jump_height), count in list(dp.items()):
           if eaten_mask & (1 << idx):
               continue
          
           if jump_height >= h and last_type != t:
               new_mask = eaten_mask | (1 << idx)
               new_key = (new_mask, t, jump_height + m)
               new_dp[new_key] = max(new_dp.get(new_key, 0), count + 1)
      
       dp = new_dp
  
   return f"{max(dp.values()) if dp else 0}\n"


def solve_1303_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   p, q, l, r = map(int, lines[0].split())
   z_times = []
   for i in range(1, p + 1):
       a, b = map(int, lines[i].split())
       z_times.append((a, b))
  
   x_times = []
   for i in range(p + 1, p + q + 1):
       c, d = map(int, lines[i].split())
       x_times.append((c, d))
  
   count = 0
   for t in range(l, r + 1):
       found = False
       for c, d in x_times:
           for a, b in z_times:
               if max(a, c + t) <= min(b, d + t):
                   found = True
                   break
           if found:
               break
       if found:
           count += 1
  
   return f"{count}\n"


def solve_203_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n = int(lines[0])
   senate = lines[1]
  
   from collections import deque
   d_queue = deque()
   r_queue = deque()
  
   for i, party in enumerate(senate):
       if party == 'D':
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
  
   return "D\n" if d_queue else "R\n"


def solve_3177_v1(input_str: str) -> str:
   from collections import deque
  
   lines = input_str.strip().splitlines()
   n, m = map(int, lines[0].split())
   perm = tuple(map(int, lines[1].split()))
   swaps = []
   for i in range(2, m + 2):
       a, b = map(int, lines[i].split())
       swaps.append((a - 1, b - 1))
  
   target = tuple(range(1, n + 1))
  
   if perm == target:
       return "0\n"
  
   queue = deque([(perm, 0)])
   visited = {perm}
  
   while queue:
       current, moves = queue.popleft()
      
       for i, j in swaps:
           next_perm = list(current)
           next_perm[i], next_perm[j] = next_perm[j], next_perm[i]
           next_perm = tuple(next_perm)
          
           if next_perm == target:
               return f"{moves + 1}\n"
          
           if next_perm not in visited:
               visited.add(next_perm)
               queue.append((next_perm, moves + 1))
  
   return ""


def solve_4559_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n = int(lines[0])
   arr = list(map(int, lines[1].split()))
   LIMIT = 10**18
  
   if 0 in arr:
       return "0\n"
  
   prod = 1
   for a in arr:
       if prod > LIMIT // a:
           return "-1\n"
       prod *= a
  
   return f"{prod}\n"





