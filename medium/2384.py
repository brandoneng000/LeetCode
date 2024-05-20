from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        center = ""
        right_side = []

        for digit in "0123456789":
            if count[digit] % 2 == 1:
                center = digit
            right_side.extend(digit * (count[digit] // 2))

        res = ''.join(right_side[::-1] + [center] + right_side).strip('0')
        return res if res else '0'


def main():
    sol = Solution()
    print(sol.largestPalindromic("444947137"))
    print(sol.largestPalindromic("00009"))

if __name__ == '__main__':
    main()