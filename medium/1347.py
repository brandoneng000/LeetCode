import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        res = 0

        for letter in s_count:
            res += max(0, s_count[letter] - t_count.get(letter, 0))
        
        return res

def main():
    sol = Solution()
    print(sol.minSteps(s = "bab", t = "aba"))
    print(sol.minSteps(s = "leetcode", t = "practice"))
    print(sol.minSteps(s = "anagram", t = "mangaar"))

if __name__ == '__main__':
    main()