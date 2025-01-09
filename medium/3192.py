from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        inverted = False
        res = 0

        for bit in nums:
            if not inverted and bit == 0:
                res += 1
                inverted = True
            elif inverted and bit == 1:
                res += 1
                inverted = False
        
        return res
        
def main():
    sol = Solution()
    print(sol.minOperations([0,1,1,0,1]))
    print(sol.minOperations([1,0,0,0]))

if __name__ == '__main__':
    main()