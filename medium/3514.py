from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = set()
        cur = set()

        for i in range(n):
            for j in range(n):
                cur.add(nums[i] ^ nums[j])

        for i in range(n):
            for num in cur:
                res.add(nums[i] ^ num)

        return len(res)
        

def main():
    sol = Solution()
    print(sol.uniqueXorTriplets([1,3]))
    print(sol.uniqueXorTriplets([6,7,8,9]))

if __name__ == '__main__':
    main()