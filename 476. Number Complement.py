class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = bin(num)[2:]
        complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        
        return int(complement_str, 2)
