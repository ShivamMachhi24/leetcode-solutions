class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        if n == 1:
            return m
        
        def multiply(mat1, mat2):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if mat1[i][k] == 0:
                        continue
                    for j in range(size):
                        res[i][j] = (res[i][j] + mat1[i][k] * mat2[k][j]) % MOD
            return res

        def power(mat, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            base = mat
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(m):
                if j > i:
                    T[2 * i][2 * j + 1] = 1
                elif j < i:
                    T[2 * i + 1][2 * j] = 1
        
        T_pow = power(T, n - 1)
        
        ans = 0
        for i in range(size):
            ans = (ans + sum(T_pow[i])) % MOD
            
        return ans