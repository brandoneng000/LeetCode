from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums:
            diff ^= n
        diff &= -diff
        res = [0, 0]
        for n in nums:
            if diff & n:
                res[0] ^= n
            else:
                res[1] ^= n
        
        return res



def main():
    sol = Solution()
    print(sol.singleNumber([1,2,1,3,2,5]))
    print(sol.singleNumber([-1,0]))
    print(sol.singleNumber([0,1]))

if __name__ == '__main__':
    main()