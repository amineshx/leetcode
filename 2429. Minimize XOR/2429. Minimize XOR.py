class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x, y = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if x > y and (1 << i) & num1 > 0:
                res ^= 1 << i
                x -= 1
            if x < y and (1 << i) & num1 == 0:
                res ^= 1 << i
                x += 1
        return res
