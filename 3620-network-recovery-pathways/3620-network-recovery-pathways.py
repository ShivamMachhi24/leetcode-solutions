from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        adj = [[] for _ in range(n)]
        in_degree_orig = [0] * n
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree_orig[v] += 1
                
        def check(min_allowed_cost: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            in_deg = [0] * n
            for u in range(n):
                if online[u]:
                    for v, cost in adj[u]:
                        if cost >= min_allowed_cost:
                            in_deg[v] += 1
            
            queue = deque([i for i in range(n) if in_deg[i] == 0 and online[i]])
            
            while queue:
                u = queue.popleft()
                
                if dist[u] == float('inf'):
                    pass
                
                for v, cost in adj[u]:
                    if cost >= min_allowed_cost:
                        if dist[u] != float('inf') and dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                        
                        in_deg[v] -= 1
                        if in_deg[v] == 0:
                            queue.append(v)
                            
            return dist[n - 1] <= k

        low, high = 0, 10**9
        ans = -1
        
        while low <= high:
            mid = (low + high)
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans