def solve_1079_v1(input_str: str) -> str:
   s = input_str.strip()
   n = len(s)
   s = '0' + s
   count = 0
   i = 1
   while i <= n:
       if s[i] == '1':
           j = i
           while j <= n and s[j] == '1':
               j += 1
           count += 1
           i = j + 1
       else:
           i += 1
   return f"{count}\n"


def solve_1079_v2(input_str: str) -> str:
   s = input_str.strip()
   s += '0'
   groups = 0
   i = 0
   while i < len(s):
       if s[i] == '1':
           groups += 1
           while i < len(s) and s[i] == '1':
               i += 1
           i += 1
       else:
           i += 1
   return f"{groups}\n"


def solve_1079_v3(input_str: str) -> str:
   s = input_str.strip()
   result = 0
   prev = '0'
   for c in s + '0':
       if prev == '1' and c == '0':
           result += 1
       prev = c
   return f"{result}\n"


def solve_771_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, k, m = map(int, lines[0].split())
   a = list(map(int, lines[1].split()))
  
   groups = {}
   for num in a:
       mod = num % m
       if mod not in groups:
           groups[mod] = []
       groups[mod].append(num)
  
   for mod in groups:
       if len(groups[mod]) >= k:
           return "Yes\n" + ' '.join(map(str, groups[mod][:k])) + " \n"
   return "No\n"


def solve_771_v2(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, k, m = map(int, lines[0].split())
   a = list(map(int, lines[1].split()))
  
   from collections import defaultdict
   d = defaultdict(list)
   for x in a:
       d[x % m].append(x)
  
   for key in d:
       if len(d[key]) >= k:
           return "Yes\n" + ' '.join(map(str, d[key][:k])) + " \n"
   return "No\n"


def solve_771_v3(input_str: str) -> str:
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
   best_len = 0
   best_str = ""
  
   for length in range(n, 0, -1):
       found = {}
       for i in range(n - length + 1):
           substr = s[i:i+length]
           if substr in found:
               if length > best_len or (length == best_len and substr < best_str):
                   best_len = length
                   best_str = substr
                   break
           found[substr] = i
       if best_len == length:
           break
  
   return f"{best_str}\n"


def solve_3040_v2(input_str: str) -> str:
   s = input_str.strip()
   n = len(s)
  
   for length in range(n, 0, -1):
       substrings = set()
       candidates = []
       for i in range(n - length + 1):
           substr = s[i:i+length]
           if substr in substrings:
               candidates.append(substr)
           substrings.add(substr)
       if candidates:
           return f"{min(candidates)}\n"
   return ""


def solve_3040_v3(input_str: str) -> str:
   s = input_str.strip()
   n = len(s)
   result = ""
  
   for l in range(n, 0, -1):
       seen = {}
       for i in range(n - l + 1):
           sub = s[i:i+l]
           if sub in seen:
               if not result or sub < result:
                   result = sub
           seen[sub] = True
       if result:
           return f"{result}\n"
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


def solve_4655_v2(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   q = int(lines[0])
   results = []
   for i in range(1, q + 1):
       nums = list(map(int, lines[i].split()))
       results.append(str(sum(nums) // 2))
   return '\n'.join(results) + '\n'


def solve_4655_v3(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   q = int(lines[0])
   output = []
   for i in range(1, q + 1):
       a, b, c = map(int, lines[i].split())
       output.append(str((a + b + c) // 2))
   return '\n'.join(output) + '\n'


def solve_4245_v1(input_str: str) -> str:
   a, b = map(int, input_str.strip().split())
   if b == 1:
       return "0\n"
   else:
       return f"{(b - 2 + a - 1) // (a - 1)}\n"


def solve_4245_v2(input_str: str) -> str:
   a, b = map(int, input_str.strip().split())
   import math
   return f"{max(0, math.ceil((b - 1) / (a - 1)))}\n"


def solve_4245_v3(input_str: str) -> str:
   a, b = map(int, input_str.strip().split())
   if b <= 1:
       return "0\n"
   else:
       need = b - 1
       gain = a - 1
       return f"{(need + gain - 1) // gain}\n"


def solve_747_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, x = map(int, lines[0].split())
   candies = []
   for i in range(1, n + 1):
       t, h, m = map(int, lines[i].split())
       candies.append((t, h, m))
  
   candies.sort(key=lambda c: c[1])
  
   dp = {}
   dp[(0, -1, x)] = 0
  
   for i in range(n):
       t, h, m = candies[i]
       new_dp = {}
       for (idx, last_type, jump), count in dp.items():
           if idx == i:
               if jump >= h and last_type != t:
                   key = (i + 1, t, jump + m)
                   new_dp[key] = max(new_dp.get(key, 0), count + 1)
               key = (i + 1, last_type, jump)
               new_dp[key] = max(new_dp.get(key, 0), count)
       dp = new_dp
  
   return f"{max(dp.values()) if dp else 0}\n"


def solve_747_v2(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, x = map(int, lines[0].split())
   candies = []
   for i in range(1, n + 1):
       t, h, m = map(int, lines[i].split())
       candies.append((h, m, t))
  
   candies.sort()
  
   dp = [[-1, -1] for _ in range(n + 1)]
   dp[0] = [x, x]
  
   for i in range(n):
       h, m, t = candies[i]
       for j in range(i + 1):
           for prev_t in range(2):
               if dp[j][prev_t] >= h and prev_t != t:
                   if dp[j + 1][t] < dp[j][prev_t] + m:
                       dp[j + 1][t] = dp[j][prev_t] + m
  
   max_candies = 0
   for i in range(n + 1):
       if dp[i][0] >= 0 or dp[i][1] >= 0:
           max_candies = i
  
   return f"{max_candies}\n"


def solve_747_v3(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n, x = map(int, lines[0].split())
   candies = []
   for i in range(1, n + 1):
       t, h, m = map(int, lines[i].split())
       candies.append((h, m, t))
  
   candies.sort()
  
   max_eaten = [0]
  
   def dfs(idx, last_type, jump_height, eaten):
       if idx == n:
           max_eaten[0] = max(max_eaten[0], eaten)
           return
      
       h, m, t = candies[idx]
      
       if jump_height >= h and last_type != t:
           dfs(idx + 1, t, jump_height + m, eaten + 1)
      
       dfs(idx + 1, last_type, jump_height, eaten)
  
   dfs(0, -1, x, 0)
   return f"{max_eaten[0]}\n"


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
               if not (c + t > b or d + t < a):
                   found = True
                   break
           if found:
               break
       if found:
           count += 1
  
   return f"{count}\n"


def solve_1303_v2(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   p, q, l, r = map(int, lines[0].split())
   z = [tuple(map(int, lines[i].split())) for i in range(1, p + 1)]
   x = [tuple(map(int, lines[i].split())) for i in range(p + 1, p + q + 1)]
  
   result = 0
   for t in range(l, r + 1):
       ok = False
       for c, d in x:
           for a, b in z:
               if max(a, c + t) <= min(b, d + t):
                   ok = True
                   break
           if ok:
               break
       if ok:
           result += 1
  
   return f"{result}\n"


def solve_1303_v3(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   p, q, l, r = map(int, lines[0].split())
   z_schedule = []
   x_schedule = []
  
   for i in range(1, p + 1):
       z_schedule.append(tuple(map(int, lines[i].split())))
  
   for i in range(p + 1, p + q + 1):
       x_schedule.append(tuple(map(int, lines[i].split())))
  
   count = 0
   for shift in range(l, r + 1):
       can_chat = False
       for x_start, x_end in x_schedule:
           for z_start, z_end in z_schedule:
               if x_start + shift <= z_end and x_end + shift >= z_start:
                   can_chat = True
                   break
           if can_chat:
               break
       if can_chat:
           count += 1
  
   return f"{count}\n"


def solve_203_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n = int(lines[0])
   s = lines[1]
  
   from collections import deque
   q = deque(range(n))
   votes = list(s)
   active = [True] * n
   d_wait = 0
   r_wait = 0
  
   while True:
       if all(votes[i] == 'D' for i in range(n) if active[i]):
           return "D\n"
       if all(votes[i] == 'R' for i in range(n) if active[i]):
           return "R\n"
      
       i = q.popleft()
       if not active[i]:
           continue
      
       if votes[i] == 'D':
           if r_wait > 0:
               r_wait -= 1
               active[i] = False
           else:
               d_wait += 1
               q.append(i)
       else:
           if d_wait > 0:
               d_wait -= 1
               active[i] = False
           else:
               r_wait += 1
               q.append(i)


def solve_203_v2(input_str: str) -> str:
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


def solve_203_v3(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n = int(lines[0])
   s = lines[1]
  
   senators = list(s)
   d_count = s.count('D')
   r_count = s.count('R')
  
   d_ban = 0
   r_ban = 0
  
   while d_count > 0 and r_count > 0:
       new_senators = []
       for senator in senators:
           if senator == 'D':
               if d_ban > 0:
                   d_ban -= 1
                   d_count -= 1
               else:
                   r_ban += 1
                   new_senators.append('D')
           else:
               if r_ban > 0:
                   r_ban -= 1
                   r_count -= 1
               else:
                   d_ban += 1
                   new_senators.append('R')
       senators = new_senators
  
   return "D\n" if d_count > 0 else "R\n"


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


def solve_3177_v2(input_str: str) -> str:
   from collections import deque
  
   lines = input_str.strip().splitlines()
   n, m = map(int, lines[0].split())
   start = tuple(map(int, lines[1].split()))
  
   allowed = []
   for i in range(2, m + 2):
       a, b = map(int, lines[i].split())
       allowed.append((a - 1, b - 1))
  
   goal = tuple(range(1, n + 1))
  
   q = deque([(start, 0)])
   seen = {start}
  
   while q:
       state, dist = q.popleft()
      
       if state == goal:
           return f"{dist}\n"
      
       for i, j in allowed:
           new_state = list(state)
           new_state[i], new_state[j] = new_state[j], new_state[i]
           new_state = tuple(new_state)
          
           if new_state not in seen:
               seen.add(new_state)
               q.append((new_state, dist + 1))
  
   return ""


def solve_3177_v3(input_str: str) -> str:
   from collections import deque
  
   lines = input_str.strip().splitlines()
   n, m = map(int, lines[0].split())
   initial = tuple(map(int, lines[1].split()))
   moves = []
   for i in range(2, m + 2):
       a, b = map(int, lines[i].split())
       moves.append((a - 1, b - 1))
  
   target = tuple(range(1, n + 1))
  
   bfs_queue = deque([(initial, 0)])
   visited_states = {initial}
  
   while bfs_queue:
       current_state, steps = bfs_queue.popleft()
      
       if current_state == target:
           return f"{steps}\n"
      
       for pos1, pos2 in moves:
           next_state = list(current_state)
           next_state[pos1], next_state[pos2] = next_state[pos2], next_state[pos1]
           next_state = tuple(next_state)
          
           if next_state not in visited_states:
               visited_states.add(next_state)
               bfs_queue.append((next_state, steps + 1))
  
   return ""


def solve_4559_v1(input_str: str) -> str:
   lines = input_str.strip().splitlines()
   n = int(lines[0])
   a = list(map(int, lines[1].split()))
  
   limit = 10 ** 18
   result = 1
  
   for num in a:
       if num == 0:
           return "0\n"
       if result > limit // num:
           return "-1\n"
       result *= num
  
   return f"{result}\n"


def solve_4559_v2(input_str: str) -> str:
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



