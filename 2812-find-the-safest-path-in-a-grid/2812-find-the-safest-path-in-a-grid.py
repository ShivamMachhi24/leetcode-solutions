import heapq
from collections import deque
from typing import List


class Solution:

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dist = [[float("inf")] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float("inf"):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        max_heap = [(-dist[0][0], 0, 0)]
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]

        while max_heap:
            current_safeness, r, c = heapq.heappop(max_heap)
            current_safeness = -current_safeness

            if r == n - 1 and c == n - 1:
                return current_safeness

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    path_safeness = min(current_safeness, dist[nr][nc])

                    if path_safeness > safeness[nr][nc]:
                        safeness[nr][nc] = path_safeness
                        heapq.heappush(max_heap, (-path_safeness, nr, nc))

        return 0