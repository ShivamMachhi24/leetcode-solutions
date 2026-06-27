from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_len = 1
        
        if 1 in counts:
            ones_count = counts[1]
            if ones_count % 2 == 0:
                max_len = max(max_len, ones_count - 1)
            else:
                max_len = max(max_len, ones_count)
        
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            current_base = x
            
            while current_base in counts and counts[current_base] >= 2:
                current_len += 2
                current_base = current_base ** 2
            
            if current_base in counts and counts[current_base] >= 1:
                current_len += 1
            else:
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len
