from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = 10 ** ((intLength - 1) // 2)
        res = [q - 1 + base for q in queries]

        for i, val in enumerate(res):
            val = str(val) + str(val)[-1 - intLength % 2:: -1]
            res[i] = int(val) if len(val) == intLength else -1

        return res

        
def main():
    sol = Solution()
    print(sol.kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3))
    print(sol.kthPalindrome(queries = [2,4,6], intLength = 4))

if __name__ == '__main__':
    main()