from typing import List
from string import ascii_lowercase

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        letter_vals = { letter: i for i, letter in enumerate(ascii_lowercase, 1) }
        res = 0
        cur = 0

        for letter, val in zip(chars, vals):
            letter_vals[letter] = val
        
        for letter in s:
            cur += letter_vals[letter]
            res = max(res, cur)
            cur = max(cur, 0)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumCostSubstring(s = "adaa", chars = "d", vals = [-1000]))
    print(sol.maximumCostSubstring(s = "abc", chars = "abc", vals = [-1,-1,-1]))

if __name__ == '__main__':
    main()