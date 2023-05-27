from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        prev = -1

        for i in range(len(nums) - 1):
            if nums[i + 1] >= nums[i]:
                prev = i
            else:
                if nums[prev] > nums[i + 1] and prev >= 0:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[prev] if prev != -1 else -float('inf')
                break
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
            
        return True

def main():
    sol = Solution()
    # 323
    print(sol.checkPossibility([5,7,1,8]))
    # 300
    print(sol.checkPossibility([-1,4,2,3]))
    print(sol.checkPossibility([4,2,3]))
    print(sol.checkPossibility([4,2,1]))

if __name__ == '__main__':
    main()