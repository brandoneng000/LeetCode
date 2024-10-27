from typing import List

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        negative_one = 0
        res = []

        for num in nums:
            if num == -1:
                negative_one += 1

                if negative_one > len(seen):
                    res.append(-1)
                else:
                    res.append(seen[-negative_one])
            else:
                seen.append(num)
                negative_one = 0

        return res

        
def main():
    sol = Solution()
    print(sol.lastVisitedIntegers([1,2,-1,-1,-1]))
    print(sol.lastVisitedIntegers([1,-1,2,-1,-1]))

if __name__ == '__main__':
    main()