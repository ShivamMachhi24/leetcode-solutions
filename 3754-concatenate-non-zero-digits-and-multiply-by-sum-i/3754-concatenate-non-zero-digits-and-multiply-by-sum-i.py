class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        x = 0
        digit_sum = 0
        multiplier = 1
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                digit_sum += digit
                x += digit * multiplier
                multiplier *= 10
            n //= 10
            
        return x * digit_sum