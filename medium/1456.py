class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cur = sum(letter in vowels for letter in s[:k])
        left = 0
        res = cur

        for c in s[k:]:
            cur -= s[left] in vowels
            left += 1
            cur += c in vowels
            res = max(res, cur)
        
        return res


def main():
    sol = Solution()
    print(sol.maxVowels(s = "abciiidef", k = 3))
    print(sol.maxVowels(s = "aeiou", k = 2))
    print(sol.maxVowels(s = "leetcode", k = 3))

if __name__ == '__main__':
    main()