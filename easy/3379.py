from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                j = (i + nums[i]) % n
                res.append(nums[j])
            elif nums[i] < 0:
                j = (i + nums[i]) % n
                res.append(nums[j])
            else:
                res.append(nums[i])

        return res

def main():
    sol = Solution()
    print(sol.constructTransformedArray([3,-2,1,1]))
    print(sol.constructTransformedArray([-1,4,-1]))

if __name__ == '__main__':
    main()