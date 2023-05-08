from typing import List
import collections

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = "".join(str(n) for n in nums)
        return [int(d) for d in nums]
        
        # res = []

        # for n in nums:
        #     temp = collections.deque()
        #     while n:
        #         temp.appendleft(n % 10)
        #         n //= 10
        #     res.extend(temp)
        
        # return res
    
        # res = []

        # for n in nums:
        #     temp = []
        #     while n:
        #         temp.append(n % 10)
        #         n //= 10
        #     res.extend(temp[::-1])
        
        # return res
        
        # res = []

        # for n in nums:
        #     temp = list(str(n))
        #     res.extend(int(d) for d in temp)
        
        # return res

def main():
    sol = Solution()
    print(sol.separateDigits([13,25,83,77]))
    print(sol.separateDigits([7,1,3,9]))

if __name__ == '__main__':
    main()