from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        bits = [0] * 32

        for i in range(32):
            for n in nums:
                bits[32 - i - 1] += (n >> i) & 1
            res += bits[32 - i - 1] * (len(nums) - bits[32 - i - 1])

        return res
    
    

def main():
    sol = Solution()
    print(sol.totalHammingDistance([346450570,966562973]))
    print(sol.totalHammingDistance([4,14,2]))
    print(sol.totalHammingDistance([4,14,4]))
    print(sol.totalHammingDistance([4,14,2,5,1,3,6,1,2,3,5,7,8]))
    print(sol.totalHammingDistance([1,2,5,7])) 
    # 001 010 101 111
    # 4 + 4 + 3

if __name__ == '__main__':
    main()