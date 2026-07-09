class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            component[i] = curr_id
            
        answer = []
        for u, v in queries:
            if component[u] == component[v]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer