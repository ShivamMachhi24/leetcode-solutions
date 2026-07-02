from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        
        max_health = [[-1] * C for _ in range(R)]
        
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
            
        max_health[0][0] = start_health
        
        q = deque([(0, 0)])
        
        while q:
            r, c = q.popleft()
            
            if r == R - 1 and c == C - 1:
                return max_health[r][c] >= 1
                
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C:
                    next_health = max_health[r][c] - grid[nr][nc]
                    
                    if next_health > max_health[nr][nc] and next_health > 0:
                        max_health[nr][nc] = next_health
                        
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
                            
        return False