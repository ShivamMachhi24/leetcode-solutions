class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 1
        bit = [0] * (2 * n + 3)
        
        def update(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        ans = 0
        curr_sum = 0
        
        update(0 + offset, 1)
        
        for num in nums:
            if num == target:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            ans += query(curr_sum + offset - 1)
            
            update(curr_sum + offset, 1)
            
        return ans
