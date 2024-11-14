from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        def check_diff(nums1: List[int], nums2: List[int], x: int):
            n = len(nums1)
            m = len(nums2)
            diff = 2
            j = 0

            for i in range(n):
                if nums1[i] == nums2[j] - x:
                    j += 1
                else:
                    diff -= 1
                
                if diff < 0:
                    return False
                
                if j == m:
                    break
            
            return True
            

        nums1.sort()
        nums2.sort()
        diff_choices = set([nums2[0] - num for num in nums1[:3]])
        res = []

        for x in diff_choices:
            if check_diff(nums1, nums2, x):
                res.append(x)
        
        return min(res)

        

        
def main():
    sol = Solution()
    print(sol.minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10]))
    print(sol.minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7]))

if __name__ == '__main__':
    main()