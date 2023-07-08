from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [sum(num for num in nums if num % 2 == 0)]

        for val, i in queries:
            prev = nums[i]
            nums[i] += val
            prev_check = prev % 2
            nums_check = nums[i] % 2
            if nums_check == 0 and prev_check == 0:
                res.append(res[-1] + val)
            elif nums_check == 1 and prev_check == 0:
                res.append(res[-1] - prev)
            elif nums_check == 0 and prev_check == 1:
                res.append(res[-1] + nums[i])
            else:
                res.append(res[-1])
        
        return res[1:]

def main():
    sol = Solution()
    print(sol.sumEvenAfterQueries(nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))
    print(sol.sumEvenAfterQueries(nums = [1], queries = [[4,0]]))

if __name__ == '__main__':
    main()