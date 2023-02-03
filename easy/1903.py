class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = list(num)
        
        while len(num) > 0 and int(num[-1]) % 2 != 1:
            num.pop()
        
        return ''.join(num)

def main():
    sol = Solution()
    print(sol.largestOddNumber("52"))
    print(sol.largestOddNumber("4206"))
    print(sol.largestOddNumber("35427"))

if __name__ == '__main__':
    main()