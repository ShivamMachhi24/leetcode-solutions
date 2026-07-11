from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = [False] * n
        ans = 0
        
        for node in range(n):
            if not seen[node]:
                group = []
                nodes_queue = deque([node])
                seen[node] = True
                
                while nodes_queue:
                    curr = nodes_queue.popleft()
                    group.append(curr)
                    for neighbor in graph[curr]:
                        if not seen[neighbor]:
                            seen[neighbor] = True
                            nodes_queue.append(neighbor)
                
                valid = True
                required_connections = len(group) - 1
                for member in group:
                    if len(graph[member]) != required_connections:
                        valid = False
                        break
                
                if valid:
                    ans += 1
                    
        return ans