import sys

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        
        pos = [0] * n
        for i, node in enumerate(sorted_nodes):
            pos[node] = i
            
        comp = [0] * n
        c_id = 0
        for i in range(1, n):
            if nums[sorted_nodes[i]] - nums[sorted_nodes[i - 1]] > maxDiff:
                c_id += 1
            comp[i] = c_id
            
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        
        right = 0
        for left in range(n):
            while right < n and nums[sorted_nodes[right]] - nums[sorted_nodes[left]] <= maxDiff:
                right += 1
            up[left][0] = right - 1
            
        for j in range(1, LOG):
            for i in range(n):
                ancestor = up[i][j - 1]
                if ancestor != -1:
                    up[i][j] = up[ancestor][j - 1]
                else:
                    up[i][j] = -1
                    
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            u_pos = pos[u]
            v_pos = pos[v]
            
            if u_pos > v_pos:
                u_pos, v_pos = v_pos, u_pos
                
            if comp[u_pos] != comp[v_pos]:
                ans.append(-1)
                continue
                
            steps = 0
            curr = u_pos
            for j in range(LOG - 1, -1, -1):
                nxt = up[curr][j]
                if nxt != -1 and nxt < v_pos:
                    curr = nxt
                    steps += (1 << j)
                    
            ans.append(steps + 1)
            
        return ans