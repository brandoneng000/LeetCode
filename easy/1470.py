from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for index in range(n):
            result.append(nums[index])
            result.append(nums[index + n])

        return result



def main():
    sol = Solution()
    print(sol.shuffle(nums = [2,5,1,3,4,7], n = 3))
    print(sol.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
    print(sol.shuffle(nums = [1,1,2,2], n = 2))

if __name__ == '__main__':
    main()