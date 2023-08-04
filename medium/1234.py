import collections

class Solution:
    def balancedString(self, s: str) -> int:
        char_count = collections.Counter(s)
        res = n = len(s)
        i = 0

        for j, c in enumerate(s):
            char_count[c] -= 1
            while i < n and all(n / 4 >= char_count[char] for char in "QWER"):
                res = min(res, j - i + 1)
                char_count[s[i]] += 1
                i += 1
        
        return res

def main():
    sol = Solution()
    print(sol.balancedString("QWER"))
    print(sol.balancedString("QQWE"))
    print(sol.balancedString("QQQW"))

if __name__ == '__main__':
    main()