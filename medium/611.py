from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(0, len(nums) - 2):
            k = i + 2 
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    break
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        
        return res
    
    
    # def triangleNumber(self, nums: List[int]) -> int:
    #     self.res = 0

    #     def gen_tri(cur: List[int], index: int):
    #         if len(cur) == 3 and self.check_tri(cur):
    #             self.res += 1
    #             return
            
    #         for i in range(index, len(nums)):
    #             cur.append(nums[i])
    #             gen_tri(cur, i + 1)
    #             cur.pop()

    #     gen_tri([], 0)
    #     return self.res

    # def check_tri(self, sides: List[int]) -> bool:
    #     return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1] 

def main():
    sol = Solution()
    print(sol.triangleNumber([2,2,3,4]))
    print(sol.triangleNumber([4,2,3,4]))

if __name__ == '__main__':
    main()