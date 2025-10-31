from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        used = set()
        res = []

        for num in nums:
            if num in used:
                res.append(num)
            used.add(num)
        
        return res
        
def main():
    sol = Solution()
    print(sol.getSneakyNumbers([0,1,1,0]))
    print(sol.getSneakyNumbers([0,3,2,1,3,2]))
    print(sol.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))

if __name__ == '__main__':
    main()