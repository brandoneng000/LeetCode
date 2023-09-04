class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, res = { 0: -1 }, 0, 0

        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            
            if n not in d:
                d[n] = i
            else:
                res = max(res, i - d[n])
        
        return res

        
def main():
    sol = Solution()
    print(sol.findTheLongestSubstring("eleetminicoworoep"))
    print(sol.findTheLongestSubstring("leetcodeisgreat"))
    print(sol.findTheLongestSubstring("bcbcbc"))

if __name__ == '__main__':
    main()