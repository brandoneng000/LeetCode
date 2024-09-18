from collections import Counter

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        res = -1
        count = Counter()

        for i in range(n):
            for j in range(i + 1, n + 1):
                string = s[i:j]

                if len(set(string)) == 1:
                    count[string] += 1
        
        for string, c in count.items():
            if c >= 3:
                res = max(res, len(string))
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumLength("aaaa"))
    print(sol.maximumLength("abcdef"))
    print(sol.maximumLength("abcaba"))

if __name__ == '__main__':
    main()