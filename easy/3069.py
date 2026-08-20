from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        res[-1] = nums[1]
        index = 0
        reverse_index = n - 1

        for i in range(2, n):
            if res[index] > res[reverse_index]:
                index += 1
                res[index] = nums[i]
            else:
                reverse_index -= 1
                res[reverse_index] = nums[i]

        l = reverse_index
        r = n - 1

        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

        return res
        

    # def resultArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     arr1 = [nums[0]]
    #     arr2 = [nums[1]]

    #     for i in range(2, n):
    #         if arr1[-1] > arr2[-1]:
    #             arr1.append(nums[i])
    #         else:
    #             arr2.append(nums[i])
        
    #     return arr1 + arr2
        
def main():
    sol = Solution()
    print(sol.resultArray([2,1,3]))
    print(sol.resultArray([5,4,3,8]))

if __name__ == '__main__':
    main()