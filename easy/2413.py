class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n & 1 else n

def main():
    sol = Solution()
    print(sol.smallestEvenMultiple(5))
    print(sol.smallestEvenMultiple(6))

if __name__ == '__main__':
    main()