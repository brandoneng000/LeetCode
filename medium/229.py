from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # num_count = {}

        # for n in nums:
        #     num_count[n] = num_count.get(n, 0) + 1
        
        # return [n for n in num_count if num_count[n] > (len(nums) // 3)]
        first_major, first_vote, second_major, second_vote, = 0, 0, 1, 0
        for n in nums:
            if n == first_major:
                first_vote += 1
            elif n == second_major:
                second_vote += 1
            elif first_vote == 0:
                first_major, first_vote = n, 1
            elif second_vote == 0:
                second_major, second_vote = n, 1
            else:
                first_vote -= 1
                second_vote -= 1
            
        res = []
        if nums.count(first_major) > len(nums) // 3:
            res.append(first_major)
        if nums.count(second_major) > len(nums) // 3:
            res.append(second_major)
        return res
    
def main():
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([1]))
    print(sol.majorityElement([1,2]))

if __name__ == '__main__':
    main()