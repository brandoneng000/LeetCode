from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ascend, descend = 0, 0

        for index, val in enumerate(rating):
            left_less, left_greater = 0, 0
            right_less, right_greater = 0, 0

            for left in rating[:index]:
                if left < val:
                    left_less += 1
                if left > val:
                    left_greater += 1
                
            for right in rating[index + 1:]:
                if right > val:
                    right_greater += 1
                if right < val:
                    right_less += 1
            
            ascend += left_less * right_greater
            descend += left_greater * right_less
        
        return ascend + descend


    # def numTeams(self, rating: List[int]) -> int:
    #     n = len(rating)
        
    #     def helper(rating: List[int]):
    #         res = 0
            
    #         for left in range(n - 2):
    #             for right in range(n - 1, left + 1, -1):
    #                 if rating[left] > rating[right]:
    #                     continue
                    
    #                 for center in range(left, right):
    #                     if rating[left] < rating[center] < rating[right]:
    #                         res += 1
        
    #         return res
        
    #     return helper(rating) + helper(rating[::-1])


def main():
    sol = Solution()
    print(sol.numTeams([2,5,3,4,1]))
    print(sol.numTeams([2,1,3]))
    print(sol.numTeams([1,2,3,4]))

if __name__ == '__main__':
    main()