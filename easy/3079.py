from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            num_str = str(num)
            res += int(max(num_str) * len(num_str))
        
        return res
        
def main():
    sol = Solution()
    print(sol.sumOfEncryptedInt([1,2,3]))
    print(sol.sumOfEncryptedInt([10,21,31]))

if __name__ == '__main__':
    main()