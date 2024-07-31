from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        def helper(i: int, front: str, back: int):
            if i == n:
                return 0
            if (i, front, back) in dp:
                return dp[(i, front, back)]
            
            a = helper(i + 1, front, words[i][-1]) - (1 if back == words[i][0] else 0)
            b = helper(i + 1, words[i][0], back) - (1 if front == words[i][-1] else 0)

            dp[(i, front, back)] = min(a, b) + len(words[i])

            return dp[(i, front, back)]
        
        n = len(words)
        dp = {}

        return helper(1, words[0][0], words[0][-1]) + len(words[0])

        
        
def main():
    sol = Solution()
    print(sol.minimizeConcatenatedLength(["aa","ab","bc"]))
    print(sol.minimizeConcatenatedLength(["ab","b"]))
    print(sol.minimizeConcatenatedLength(["aaa","c","aba"]))

if __name__ == '__main__':
    main()