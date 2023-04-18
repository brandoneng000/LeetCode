class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # difference = x ^ y
        # count = 0

        # while difference:
        #     if difference & 1:
        #         count += 1
        #     difference >>= 1
            
        # return count
        x ^= y
        y = 0

        while x:
            y += x & 1
            x >>= 1
            
        return y
        
def main():
    sol = Solution()
    print(sol.hammingDistance(x = 1, y = 4))
    print(sol.hammingDistance(x = 3, y = 1))
    print(sol.hammingDistance(x = 93, y = 73))
    print(sol.hammingDistance(x = 4, y = 2))

if __name__ == '__main__':
    main()