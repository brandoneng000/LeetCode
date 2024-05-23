from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (startPos - endPos - k) % 2:
            return 0

        mod = 1000000007
        return comb(k, (endPos - startPos + k) // 2) % mod

        
def main():
    sol = Solution()
    print(sol.numberOfWays(startPos = 1, endPos = 2, k = 3))
    print(sol.numberOfWays(startPos = 2, endPos = 5, k = 10))

if __name__ == '__main__':
    main()