from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        res = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
            res = max(res, score)
        
        return res
                

def main():
    sol = Solution()
    print(sol.bagOfTokensScore(tokens = [71,55,82], power = 54))
    print(sol.bagOfTokensScore(tokens = [100], power = 50))
    print(sol.bagOfTokensScore(tokens = [100,200], power = 150))
    print(sol.bagOfTokensScore(tokens = [100,200,300,400], power = 200))

if __name__ == '__main__':
    main()