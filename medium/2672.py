from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        res = []
        cur = 0

        for i, color in queries:
            if color == colors[i]:
                res.append(cur)
                continue

            if i + 1 < n and colors[i] != 0 and colors[i] == colors[i + 1]:
                cur -= 1
            
            if i > 0 and colors[i] != 0 and colors[i] == colors[i - 1]:
                cur -= 1
            
            colors[i] = color
            if i + 1 < n and colors[i] == colors[i + 1]:
                cur += 1
            
            if i > 0 and colors[i] == colors[i - 1]:
                cur += 1

            res.append(cur)
        
        return res

def main():
    sol = Solution()
    print(sol.colorTheArray(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]))
    print(sol.colorTheArray(n = 1, queries = [[0,100000]]))

if __name__ == '__main__':
    main()