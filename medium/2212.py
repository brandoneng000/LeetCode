from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def helper(cur_score: int, bob_arrows: List[int], index: int, remain_arrows: int):
            if index == 12:
                if cur_score > self.max_score:
                    self.max_score = cur_score
                    self.best_bob = bob_arrows.copy()
                return
            
            helper(cur_score, bob_arrows, index + 1, remain_arrows)

            if remain_arrows > aliceArrows[index]:
                prev = bob_arrows[index]
                bob_arrows[index] = aliceArrows[index] + 1
                helper(cur_score + index, bob_arrows, index + 1, remain_arrows - bob_arrows[index])
                bob_arrows[index] = prev

        
        n = len(aliceArrows)
        self.max_score = 0
        self.best_bob = [0] * n

        helper(0, [0] * n, 0, numArrows)
        self.best_bob[0] += numArrows - sum(self.best_bob)

        return self.best_bob


        
def main():
    sol = Solution()
    print(sol.maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]))
    print(sol.maximumBobPoints(numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]))

if __name__ == '__main__':
    main()