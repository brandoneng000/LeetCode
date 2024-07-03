from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        cur = 0

        for val in word:
            cur = (cur * 10 + int(val)) % m

            if cur == 0:
                res.append(1)
            else:
                res.append(0)
            
        return res

        
def main():
    sol = Solution()
    print(sol.divisibilityArray(word = "998244353", m = 3))
    print(sol.divisibilityArray(word = "1010", m = 10))

if __name__ == '__main__':
    main()