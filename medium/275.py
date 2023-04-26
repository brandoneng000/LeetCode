from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # left, right = 0, len(citations) - 1
        # while left < right:
        #     middle = (left + right) // 2
        #     index = len(citations) - middle
        #     if citations[middle] >= index:
        #         right = middle
        #     else:
        #         left = middle + 1
        
        # if left == len(citations) - 1 and citations[-1] == 0:
        #     return 0
        # return len(citations) - right

        left, right = 0, len(citations) - 1

        while left <= right:
            middle = (left + right) // 2
            if citations[middle] == len(citations) - middle:
                return len(citations) - middle
            elif citations[middle] < len(citations) - middle:
                left = middle + 1
            else:
                right = middle - 1
        
        return len(citations) - left

def main():
    sol = Solution()
    print(sol.hIndex([0,1,3,5,6]))
    print(sol.hIndex([1,2,100]))
    print(sol.hIndex([0,0,0,0,0,0,0,0,0,0,0,0]))

if __name__ == '__main__':
    main()