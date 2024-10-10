from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def helper(index: int):
            last_index = {}
            count = 0

            for i in range(index):
                last_index[changeIndices[i]] = i

            if len(last_index) != n:
                return False

            for i in range(index):
                if i == last_index[changeIndices[i]]:
                    if count < nums[changeIndices[i] - 1]:
                        return False
                    else:
                        count -= nums[changeIndices[i] - 1]
                else:
                    count += 1
            
            return True

        n, m = len(nums), len(changeIndices)
        left = 0
        right = m + 1

        while left < right:
            middle = (left + right) // 2

            if helper(middle):
                right = middle
            else:
                left = middle + 1
        
        return -1 if right == m + 1 else right

        
def main():
    sol = Solution()
    print(sol.earliestSecondToMarkIndices(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]))
    print(sol.earliestSecondToMarkIndices(nums = [1,3], changeIndices = [1,1,1,2,1,1,1]))
    print(sol.earliestSecondToMarkIndices(nums = [0,1], changeIndices = [2,2,2]))

if __name__ == '__main__':
    main()