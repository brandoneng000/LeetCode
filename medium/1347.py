import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = [0] * 26
        t_count = [0] * 26
        res = 0

        for c in s:
            s_count[ord(c) - 97] += 1
        
        for c in t:
            t_count[ord(c) - 97] += 1
        
        for i in range(26):
            res += max(0, s_count[i] - t_count[i])
        
        return res

    # def minSteps(self, s: str, t: str) -> int:
    #     s_count = collections.Counter(s)
    #     t_count = collections.Counter(t)
    #     res = 0

    #     for letter in s_count:
    #         res += max(0, s_count[letter] - t_count.get(letter, 0))
        
    #     return res

def main():
    sol = Solution()
    print(sol.minSteps(s = "bab", t = "aba"))
    print(sol.minSteps(s = "leetcode", t = "practice"))
    print(sol.minSteps(s = "anagram", t = "mangaar"))

if __name__ == '__main__':
    main()