class Solution:
    def reverseBits(self, n: int) -> int:
        # binary = bin(n)[2:].zfill(32)
        binary = f"{n:032b}"
        return int(binary[::-1], 2)

    # def reverseBits(self, n: int) -> int:
    #     res = 0
    #     for bit in range(32):
    #         res = (res << 1) | (n & 1)
    #         n >>= 1
        
    #     return res

def main():
    sol = Solution()
    print(sol.reverseBits(43261596))
    print(sol.reverseBits(2147483644))
    print(sol.reverseBits(0b00000010100101000001111010011100))

if __name__ == '__main__':
    main()