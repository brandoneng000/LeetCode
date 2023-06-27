from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        possible_max = nums[0]
        res = 1

        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                res = i + 1
                curr_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])
        
        return res


    # def partitionDisjoint(self, nums: List[int]) -> int:
    #     left = [nums[0]]
    #     right = nums[1:]

    #     while max(left) > min(right):
    #         left.extend(right[:right.index(min(right)) + 1])
    #         right = right[right.index(min(right)) + 1:]
        
    #     return len(left)
        

def main():
    sol = Solution()
    print(sol.partitionDisjoint([5,0,3,8,6]))
    print(sol.partitionDisjoint([1,1,1,0,6,12]))

if __name__ == '__main__':
    main()