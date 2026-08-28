class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        def check(c):
            left = prefix.copy()
            left.append(c)

            for i in range(25, -1, -1):
                left.extend([chr(a + i)] * cnt[i])

            palindrome = left + [odd_char] + left[::-1]
            return ''.join(palindrome) > target

        n = len(s)

        if n == 1:
            return s if s > target else ""

        cnt = [0] * 26
        a = ord('a')

        for c in s:
            cnt[ord(c) - a] += 1

        odd_char = ""

        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd_char != "":
                    return ""
                odd_char = chr(a + i)
            cnt[i] //= 2

        prefix = []

        for i in range(n // 2):
            found = False

            for j in range(26):
                if cnt[j] == 0:
                    continue

                cnt[j] -= 1

                if check(chr(a + j)):
                    prefix.append(chr(a + j))
                    found = True
                    break
                else:
                    cnt[j] += 1
            if not found:
                return ""

            if prefix[i] > target[i]:
                left = prefix[:]

                for j in range(26):
                    left.extend([chr(a + j)] * cnt[j])

                palindrome = left + [odd_char] + left[::-1]
                return ''.join(palindrome)

        res = prefix + [odd_char] + prefix[::-1]
        return ''.join(res)

def main():
    sol = Solution()
    print(sol.lexPalindromicPermutation(s = "baba", target = "abba"))
    print(sol.lexPalindromicPermutation(s = "baba", target = "bbaa"))
    print(sol.lexPalindromicPermutation(s = "abc", target = "abb"))
    print(sol.lexPalindromicPermutation(s = "aac", target = "abb"))

if __name__ == '__main__':
    main()