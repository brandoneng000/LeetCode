from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        cur = set([0])

        for reward in sorted(rewardValues):
            temp = set()

            for val in cur:
                if val < reward:
                    temp.add(val + reward)
            
            cur.update(temp)
        
        return max(cur)

        
def main():
    sol = Solution()
    print(sol.maxTotalReward([1,1,3,3]))
    print(sol.maxTotalReward([1,6,4,3,2]))

if __name__ == '__main__':
    main()