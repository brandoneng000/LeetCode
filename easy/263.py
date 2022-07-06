class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        
        ugly = [2, 3, 5]
        for num in ugly:
            while n % num == 0:
                n /= num
        
        return n == 1



def main():
    sol = Solution()
    print(sol.isUgly(6))
    print(sol.isUgly(1))
    print(sol.isUgly(14))
    print(sol.isUgly(13))

if __name__ == '__main__':
    main()