class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while True:
            while start < len(s) and s[start] not in vowels:
                start += 1
            while end >= 0 and s[end] not in vowels:
                end -= 1

            if start >= end:
                break

            s = s[:start] + s[end] + s[start + 1:end] + s[start] + s[end + 1:]

            start += 1
            end -= 1

        return s

        
def main():
    sol = Solution()
    print(sol.reverseVowels("aA"))
    print(sol.reverseVowels("hello"))
    print(sol.reverseVowels("leetcode"))
    print(sol.reverseVowels("oitghanweoirgnbaeriubhiauprehbis"))

if __name__ == '__main__':
    main()