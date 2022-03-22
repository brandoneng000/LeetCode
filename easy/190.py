class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for bit in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        
        return res

def main():
    sol = Solution()
    print(sol.reverseBits(0b00000010100101000001111010011100))

if __name__ == '__main__':
    main()