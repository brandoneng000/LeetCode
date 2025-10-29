class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 1

        while res < n:
            res *= 2
            res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.smallestNumber(5))
    print(sol.smallestNumber(10))
    print(sol.smallestNumber(3))

if __name__ == '__main__':
    main()