from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def flip_num(num: int):
            return int(str(num)[::-1])

        n = len(nums)
        INF = 10 ** 33
        indices = {}
        res = INF

        for i in range(n - 1, -1, -1):
            flipped = flip_num(nums[i])

            if flipped in indices:
                res = min(res, abs(i - indices[flipped]))
            
            indices[nums[i]] = i
            
        return res if res != INF else -1
        
        
def main():
    sol = Solution()
    print(sol.minMirrorPairDistance([12,21,45,33,54]))
    print(sol.minMirrorPairDistance([120,21]))
    print(sol.minMirrorPairDistance([21,120]))

if __name__ == '__main__':
    main()