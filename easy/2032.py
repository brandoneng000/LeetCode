from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = set()
        num_count = {}

        for num in set(nums1):
            num_count[num] = num_count.get(num, 0)
        
        for num in set(nums2):
            if num in num_count:
                result.add(num)
            else:
                num_count[num] = num_count.get(num, 0)
        
        for num in set(nums3):
            if num in num_count:
                result.add(num)
        
        return list(result)

def main():
    sol = Solution()
    print(sol.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))
    print(sol.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))
    print(sol.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))

if __name__ == '__main__':
    main()