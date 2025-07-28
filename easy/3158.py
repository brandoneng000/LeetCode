from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        found = set()

        for num in nums:
            if num in found:
                res ^= num
            else:
                found.add(num)
        
        return res
        

def main():
    sol = Solution()
    print(sol.duplicateNumbersXOR([1,2,1,3]))
    print(sol.duplicateNumbersXOR([1,2,3]))
    print(sol.duplicateNumbersXOR([1,2,2,1]))

if __name__ == '__main__':
    main()