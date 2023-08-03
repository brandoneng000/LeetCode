from typing import List

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        cur = [['']]
        phone = { '2': 'abc', '3': 'def', '4': 'ghi', 
                  '5': 'jkl', '6': 'mno', '7': 'pqrs',
                  '8': 'tuv', '9': 'wxyz'}
        
        for num in digits:
            next = []
            for cur_letters in cur:
                for next_letter in phone[num]:
                    next.append(cur_letters + [next_letter])
            cur = next
        
        return [''.join(letters) for letters in cur]

    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits: 
    #         return []
        
    #     n = len(digits)
    #     res = []
    #     phone = { '2': 'abc', '3': 'def', '4': 'ghi', 
    #               '5': 'jkl', '6': 'mno', '7': 'pqrs',
    #               '8': 'tuv', '9': 'wxyz'}
        
    #     def helper(cur: List[str], i: int):
    #         if i == n:
    #             res.append(''.join(cur))
    #             return
            
    #         for letter in phone[digits[i]]:
    #             cur.append(letter)
    #             helper(cur, i + 1)
    #             cur.pop()
        
    #     helper([], 0)
    #     return res
        

def main():
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations(""))
    print(sol.letterCombinations("2"))

if __name__ == '__main__':
    main()