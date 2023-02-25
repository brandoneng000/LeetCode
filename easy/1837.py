class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n > 0:
            result += n % k
            n //= k
        
        return result

def main():
    sol = Solution()
    print(sol.sumBase(34, 6))
    print(sol.sumBase(10, 10))

if __name__ == '__main__':
    main()