class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        dp = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]
        
        dp[n-1][n-1] = 0
        count[n-1][n-1] = 1
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or dp[r][c] == -1:
                    continue
                
                current_score = dp[r][c]
                current_count = count[r][c]
                
                directions = [(r - 1, c), (r, c - 1), (r - 1, c - 1)]
                
                for nr, nc in directions:
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':
                        cell_val = 0 if board[nr][nc] == 'E' else int(board[nr][nc])
                        next_score = current_score + cell_val
                        
                        if next_score > dp[nr][nc]:
                            dp[nr][nc] = next_score
                            count[nr][nc] = current_count
                        elif next_score == dp[nr][nc]:
                            count[nr][nc] = (count[nr][nc] + current_count) % MOD
                            
        if dp[0][0] == -1:
            return [0, 0]
            
        return [dp[0][0], count[0][0]]