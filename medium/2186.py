from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        res = 0

        for letter in set(s_count) | set(t_count):
            res += abs(s_count[letter] - t_count[letter])
        
        return res

        
def main():
    sol = Solution()
    print(sol.minSteps(s = "leetcode", t = "coats"))
    print(sol.minSteps(s = "night", t = "thing"))

if __name__ == '__main__':
    main()