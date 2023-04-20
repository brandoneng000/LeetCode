class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return '0'
        negative = num < 0
        num = abs(num)
        res = []

        while num:
            res = [str(num % 7)] + res
            num //= 7
        
        return ('-' if negative else '') + "".join(res)

def main():
    sol = Solution()
    print(sol.convertToBase7(100))
    print(sol.convertToBase7(-7))

if __name__ == '__main__':
    main()