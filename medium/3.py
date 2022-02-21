class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sub = []
        for letter in s:
            # if letter not in sub:
            #     sub.append(letter)
            # else:
            while letter in sub:
                sub.pop(0)
            sub.append(letter)
        
            if longest < len(sub):
                longest = len(sub)
            
        return longest

def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb"'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring('pwwkew'))
    print(sol.lengthOfLongestSubstring('abcad'))

if __name__ == '__main__':
    main()