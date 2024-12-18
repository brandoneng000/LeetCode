from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        balls = {}
        res = []

        for i, color in queries:
            if i in balls:
                colors[balls[i]] -= 1

                if colors[balls[i]] == 0:
                    colors.pop(balls[i])

            balls[i] = color
            colors[color] = colors.get(color, 0) + 1
            res.append(len(colors))
        
        return res


def main():
    sol = Solution()
    print(sol.queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]))
    print(sol.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]))

if __name__ == '__main__':
    main()