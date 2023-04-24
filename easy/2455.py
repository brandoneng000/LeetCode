from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0

        for n in nums:
            if not n % 6:
                count += 1
                total += n
        
        return total // (count if count != 0 else 1)

def main():
    sol = Solution()
    print(sol.averageValue([1,3,6,10,12,15]))
    print(sol.averageValue([1,2,4,7,10]))

if __name__ == '__main__':
    main()