from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        binary = [bin(num)[2:] for num in nums]
        res = 0

        for i in range(3):
            for j in range(3):
                if i != j:
                    for k in range(3):
                        if i != j and i != k and j != k:
                            res = max(res, int(binary[i] + binary[j] + binary[k], 2))
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.maxGoodNumber([1,2,3]))
    print(sol.maxGoodNumber([2,8,16]))

if __name__ == '__main__':
    main()