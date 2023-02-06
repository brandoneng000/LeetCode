from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            largest = max(stones)
            stones.remove(largest)
            second = max(stones)
            stones.remove(second)

            smash = largest - second
            if smash != 0:
                stones.append(smash)
        
        return stones[0] if stones else 0



def main():
    sol = Solution()
    print(sol.lastStoneWeight([2,7,4,1,8,1]))
    print(sol.lastStoneWeight([2,7,4,1,8,1,1]))
    print(sol.lastStoneWeight([1]))
    print(sol.lastStoneWeight([1, 1]))

if __name__ == '__main__':
    main()