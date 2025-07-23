class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        res = 0
        s_dict = {}
        t_dict = {}

        for i in range(n):
            s_dict[s[i]] = i
            t_dict[t[i]] = i
        
        for letter in s_dict:
            res += abs(s_dict[letter] - t_dict[letter])
        
        return res
        
def main():
    sol = Solution()
    print(sol.findPermutationDifference(s = "abc", t = "bac"))
    print(sol.findPermutationDifference(s = "abcde", t = "edbac"))

if __name__ == '__main__':
    main()