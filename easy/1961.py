from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""

        for word in words:
            prefix += word
            if len(prefix) == len(s):
                break
            elif len(word) > len(s):
                return False
        
        return s == prefix
        

def main():
    sol = Solution()
    print(sol.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]))
    print(sol.isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"]))

if __name__ == '__main__':
    main()