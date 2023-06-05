from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def helper(sub: str, index: int):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[index].isalpha():
                    helper(sub + s[index].swapcase(), index + 1)
                helper(sub + s[index], index + 1)

        res = []
        helper("", 0)
        return res
    
    # def letterCasePermutation(self, s: str) -> List[str]:
        # permutations = []
        # string = []
        # char_index = []
        # s = list(s)
        # res = []
        # for i, c in enumerate(s):
        #     if c.isalpha():
        #         string.append(c)
        #         char_index.append(i)
            

        # def helper(cur: List[str], index: int):
        #     if len(cur) == len(string):
        #         permutations.append("".join(cur))
        #         return
            
        #     for i in range(index, len(string)):
        #         cur.append(string[i].lower())
        #         helper(cur, i + 1)
        #         cur.pop()
        #         cur.append(string[i].capitalize())
        #         helper(cur, i + 1)
        #         cur.pop()
        
        # helper([], 0)
        # for p in permutations:
        #     for i, c in zip(char_index, p):
        #         s[i] = c
        #     res.append("".join(s))

        # return res

def main():
    sol = Solution()
    print(sol.letterCasePermutation("abc"))
    print(sol.letterCasePermutation("a1b2"))
    print(sol.letterCasePermutation("3z4"))

if __name__ == '__main__':
    main()