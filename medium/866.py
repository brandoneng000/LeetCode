class Solution:
    def primePalindrome(self, n: int) -> int:
        while True:
            if self.is_palindrome(n) and self.is_prime(n):
                return n
            n += 1
            if 10000000 < n < 100000000:
                n = 100000000
            
    def is_palindrome(self, num: int):
        return str(num) == str(num)[::-1]

    def is_prime(self, num: int):
        if num < 2 or num % 2 == 0:
            return num == 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True


def main():
    sol = Solution()
    print(sol.primePalindrome(6))
    print(sol.primePalindrome(8))
    print(sol.primePalindrome(13))
    print(sol.primePalindrome(100000))
    print(sol.primePalindrome(100000000))

if __name__ == '__main__':
    main()