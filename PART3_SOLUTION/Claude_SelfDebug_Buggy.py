"""
Buggy versions of solutions for Part 3 - Fault Detection Check
These versions contain realistic bugs to test if our enhanced test suites catch them.
"""

# ============================================================================
# BUG 1: solve_3177_v2 - OFF-BY-ONE ERROR IN INDEX CONVERSION
# ============================================================================
# Bug Description: Forgot to subtract 1 when converting from 1-indexed to 0-indexed
# This is a VERY realistic bug - happens all the time when dealing with problem
# statements that use 1-indexed arrays but Python uses 0-indexed.
# 
# Original line 517: allowed.append((a - 1, b - 1))
# Buggy version: allowed.append((a, b))  # BUG: Not converting to 0-indexed!
# ============================================================================

def solve_3177_v2_buggy(input_str: str) -> str:
    from collections import deque
    
    lines = input_str.strip().splitlines()
    n, m = map(int, lines[0].split())
    start = tuple(map(int, lines[1].split()))
    
    allowed = []
    for i in range(2, m + 2):
        a, b = map(int, lines[i].split())
        # BUG: Forgot to subtract 1 for 0-indexed conversion!
        allowed.append((a, b))  # Should be (a-1, b-1)
    
    goal = tuple(range(1, n + 1))
    
    q = deque([(start, 0)])
    seen = {start}
    
    while q:
        state, dist = q.popleft()
        
        if state == goal:
            return f"{dist}\n"
        
        for i, j in allowed:
            # This will cause IndexError or wrong swaps!
            try:
                new_state = list(state)
                new_state[i], new_state[j] = new_state[j], new_state[i]
                new_state = tuple(new_state)
                
                if new_state not in seen:
                    seen.add(new_state)
                    q.append((new_state, dist + 1))
            except IndexError:
                # Silently fail on out-of-bounds access
                pass
    
    return ""


# ============================================================================
# BUG 2: solve_203_v2 - REVERSED COMPARISON OPERATOR
# ============================================================================
# Bug Description: Reversed the comparison logic (> instead of <)
# This is a classic logical error that completely inverts the algorithm's behavior.
# Instead of "D wins if D comes first", it becomes "D wins if D comes later"
#
# Original line 428: if d_idx < r_idx:
# Buggy version: if d_idx > r_idx:  # BUG: Reversed logic!
# ============================================================================

def solve_203_v2_buggy(input_str: str) -> str:
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
        
        # BUG: Reversed comparison - should be d_idx < r_idx
        if d_idx > r_idx:  # Wrong! This inverts the logic
            d_queue.append(d_idx + n)
        else:
            r_queue.append(r_idx + n)
    
    return "D\n" if d_queue else "R\n"


# Keep all other solve functions from original (not used in testing, just for completeness)
def solve_3177_v1(input_str: str) -> str:
    raise NotImplementedError("Not implemented for buggy testing")

def solve_3177_v3(input_str: str) -> str:
    raise NotImplementedError("Not implemented for buggy testing")

def solve_203_v1(input_str: str) -> str:
    raise NotImplementedError("Not implemented for buggy testing")

def solve_203_v3(input_str: str) -> str:
    raise NotImplementedError("Not implemented for buggy testing")

