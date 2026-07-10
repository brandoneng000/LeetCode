from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        new_nums = sorted(enumerate(nums), key=lambda x: x[1])
        get_i = [0] * n

        for i, (orig, _) in enumerate(new_nums):
            get_i[orig] = i

        LOG = 18
        st = [[0] * LOG for _ in range(n)]
        res = []
        r = 0

        for i in range(n):
            if r < i:
                r = i
            
            while (
                r + 1 < n
                and new_nums[r + 1][1] - new_nums[r][1] <= maxDiff
                and new_nums[r + 1][1] - new_nums[i][1] <= maxDiff
            ):
                r += 1
            
            st[i][0] = r

        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
        
        for u, v in queries:
            a, b = get_i[u], get_i[v]

            if a > b:
                a, b = b, a
            if a == b:
                res.append(0)
                continue
        
            curr, steps = a, 0

            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
            
            res.append(steps + 1 if st[curr][0] >= b else -1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.pathExistenceQueries(n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]))
    print(sol.pathExistenceQueries(n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]))
    print(sol.pathExistenceQueries(n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]))

if __name__ == '__main__':
    main()