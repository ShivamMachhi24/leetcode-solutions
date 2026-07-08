class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pref_x = [0] * (n + 1)
        pref_sum = [0] * (n + 1)
        cnt = [0] * (n + 1)
        
        for i in range(n):
            d = int(s[i])
            if d != 0:
                pref_x[i + 1] = (pref_x[i] * 10 + d) % MOD
                pref_sum[i + 1] = pref_sum[i] + d
                cnt[i + 1] = cnt[i] + 1
            else:
                pref_x[i + 1] = pref_x[i]
                pref_sum[i + 1] = pref_sum[i]
                cnt[i + 1] = cnt[i]
                
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            k = cnt[r + 1] - cnt[l]
            s_val = pref_sum[r + 1] - pref_sum[l]
            
            x_val = (pref_x[r + 1] - pref_x[l] * pow10[k]) % MOD
            ans.append((x_val * s_val) % MOD)
            
        return ans
