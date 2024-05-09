from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        h = sorted(happiness)

        for i in range(k):
            res += max(0, h.pop() - i)
        
        return res

def main():
    sol = Solution()
    print(sol.maximumHappinessSum(happiness = [1,2,3], k = 2))
    print(sol.maximumHappinessSum(happiness = [1,1,1,1], k = 2))
    print(sol.maximumHappinessSum(happiness = [2,3,4,5], k = 1))

if __name__ == '__main__':
    main()