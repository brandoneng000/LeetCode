from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def check_row(nums: List[int], k: int, shift: int):
            temp = nums[k * shift:] + nums[:k * shift]
            return temp == nums

        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            if not check_row(mat[i], k, -1 if i % 2 else 1):
                return False
        
        return True

        
def main():
    sol = Solution()
    print(sol.areSimilar(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4))
    print(sol.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2))
    print(sol.areSimilar(mat = [[2,2],[2,2]], k = 3))

if __name__ == '__main__':
    main()