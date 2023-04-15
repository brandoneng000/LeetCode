from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1
            res |= (count % 3) << i
        
        return res if res < (1 << 31) else res - (1 << 32)

        

def main():
    sol = Solution()
    print(sol.singleNumber([2,2,3,2]))
    print(sol.singleNumber([2,2,-3,2]))
    print(sol.singleNumber([0,1,0,1,0,1,99]))

if __name__ == '__main__':
    main()