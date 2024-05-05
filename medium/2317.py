from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        bits = [0] * 32
        res = 0

        for num in nums:
            for i in range(32):
                bits[i] += (num & (1 << (31 - i))) != 0

        for i in range(32):
            res += (1 << (31 - i)) if bits[i] != 0 else 0
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumXOR([3,2,4,6]))
    print(sol.maximumXOR([1,2,3,9,2]))

if __name__ == '__main__':
    main()