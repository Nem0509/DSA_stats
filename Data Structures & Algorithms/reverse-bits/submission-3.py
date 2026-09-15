class Solution:
    def reverseBits(self, n: int) -> int:
        # 1011010101110-->0111010101101
        return int(bin(n)[:1:-1]+'0'*(34-len(bin(n))),2)