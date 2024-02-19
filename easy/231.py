class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)

        # mask = 0b11111111111111111111111111111111

        # for i in range(32):
        #     if n == (mask & (1 << i)):
        #         return True
        
        # return False
        
def main():
    sol = Solution()
    print(sol.isPowerOfTwo(1))
    print(sol.isPowerOfTwo(16))
    print(sol.isPowerOfTwo(3))

if __name__ == '__main__':
    main()