from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        palin_set = set()
        def is_palindrome(cur_s: str) -> bool:
            return cur_s == cur_s[::-1]

        for size in range(len(s) - 1, -1, -1):
            for window in range(len(s) - size):
                cur = s[window: window + size + 1]
                if cur in palin_set:
                    res += 1
                elif is_palindrome(cur):
                    res += 1
                    for i in range(len(cur) // 2):
                        palin_set.add(cur[i: len(cur) - i])
        
        return res
            

def main():
    sol = Solution()
    print(sol.countSubstrings("abccba"))

    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))

if __name__ == '__main__':
    main()