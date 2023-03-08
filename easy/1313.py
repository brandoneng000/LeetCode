from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums), 2):
            result.append([nums[index + 1]] * nums[index])
        
        return sum(result, [])

def main():
    sol = Solution()
    print(sol.decompressRLElist([1,2,3,4]))
    print(sol.decompressRLElist([1,1,2,3]))

if __name__ == '__main__':
    main()