from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for num in count:
            if count[num] == 1 and count[num - 1] == 0 and count[num + 1] == 0:
                res.append(num)

        return res

        

def main():
    sol = Solution()
    print(sol.findLonely([10,6,5,8]))
    print(sol.findLonely([1,3,5,3]))

if __name__ == '__main__':
    main()