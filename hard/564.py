class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def half_palindrome(num: int, even: bool):
            if even:
                return int(str(num) + str(num)[::-1])
            else:
                return int(str(num)[:-1] + str(num)[::-1])
        
        size = len(n)
        index = size // 2 - 1 if size % 2 == 0 else size // 2
        first_half = int(n[: index + 1])

        choices = []
        choices.append(half_palindrome(first_half, size % 2 == 0))
        choices.append(half_palindrome(first_half + 1, size % 2 == 0))
        choices.append(half_palindrome(first_half - 1, size % 2 == 0))
        choices.append(10 ** (size - 1) - 1)
        choices.append(10 ** size + 1)
        
        diff = float('inf')
        num = int(n)
        res = 0

        for c in choices:
            if c == num:
                continue
        
            if abs(c - num) < diff:
                diff = abs(c - num)
                res = c
            elif abs(c - num) == diff:
                res = min(res, c)

        return str(res)
        

def main():
    sol = Solution()
    print(sol.nearestPalindromic("99"))
    print(sol.nearestPalindromic("22"))
    print(sol.nearestPalindromic("123"))
    print(sol.nearestPalindromic("1"))

if __name__ == '__main__':
    main()