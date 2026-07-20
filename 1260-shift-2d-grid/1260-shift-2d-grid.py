class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  # Handle cases where k >= total elements
        
        # Initialize result grid
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                flat_idx = r * n + c
                new_idx = (flat_idx + k) % total
                
                new_r = new_idx // n
                new_c = new_idx % n
                
                result[new_r][new_c] = grid[r][c]
                
        return result