from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0] ** 2]
        
        result = []
        index = 0

        while index < len(nums) and nums[index] < 0:
            index += 1
        
        negatives = nums[:index]
        positives = nums[index:]
        negatives = negatives[::-1]

        pos_index = 0
        neg_index = 0

        while pos_index < len(positives) or neg_index < len(negatives):
            if pos_index == len(positives):
                result.append(negatives[neg_index] ** 2)
                neg_index += 1
            elif neg_index == len(negatives):
                result.append(positives[pos_index] ** 2)
                pos_index += 1
            else:
                if abs(negatives[neg_index]) > positives[pos_index]:
                    result.append(positives[pos_index] ** 2)
                    pos_index += 1
                else:
                    result.append(negatives[neg_index] ** 2)
                    neg_index += 1
        
        return result
        

def main():
    sol = Solution()
    print(sol.sortedSquares([-4,-1,0,3,10]))
    print(sol.sortedSquares([-7,-3,2,3,11]))
    print(sol.sortedSquares([2]))
    print(sol.sortedSquares([-4, -4, -3]))

if __name__ == '__main__':
    main()