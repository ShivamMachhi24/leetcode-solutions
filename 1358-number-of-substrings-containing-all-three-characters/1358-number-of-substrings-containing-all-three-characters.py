class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for right, char in enumerate(s):
            last_seen[char] = right
            
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
                
        return count