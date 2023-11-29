class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     return sum((n >> i) & 1 for i in range(32))

    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
        

def main():
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011))
    print(sol.hammingWeight(0b00000000000000000000000010000000))
    print(sol.hammingWeight(0b11111111111111111111111111111101))

if __name__ == '__main__':
    main()