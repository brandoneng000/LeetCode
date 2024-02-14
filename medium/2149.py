from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        index = 0

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        for p, n in zip(positive, negative):
            nums[index] = p
            nums[index + 1] = n
            index += 2
        
        return nums

    # def rearrangeArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res = [0 for _ in range(n)]
    #     positive = 0
    #     negative = 1

    #     for num in nums:
    #         if num < 0:
    #             res[negative] = num
    #             negative += 2
    #         else:
    #             res[positive] = num
    #             positive += 2
            
    #     return res

def main():
    sol = Solution()
    print(sol.rearrangeArray([3,1,-2,-5,2,-4]))
    print(sol.rearrangeArray([-1,1]))

if __name__ == '__main__':
    main()