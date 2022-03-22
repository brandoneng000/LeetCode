class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        test = num % 9
        
        return 9 if test == 0 else test

def main():
    sol = Solution()
    print(sol.addDigits(38))
    print(sol.addDigits(0))

if __name__ == '__main__':
    main()