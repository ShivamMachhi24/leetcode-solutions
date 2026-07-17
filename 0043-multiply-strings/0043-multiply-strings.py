class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1 = 0
        for char in num1:
            n1 = n1 * 10 + (ord(char) - ord('0'))
            
        n2 = 0
        for char in num2:
            n2 = n2 * 10 + (ord(char) - ord('0'))
            
        product = n1 * n2
        
        res = []
        while product > 0:
            digit = product % 10
            res.append(chr(digit + ord('0')))
            product //= 10
            
        return "".join(res[::-1])