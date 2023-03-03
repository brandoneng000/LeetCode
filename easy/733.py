from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        original_color = image[sr][sc]
        visited = set()

        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            if image[r][c] == original_color and (r, c) not in visited:
                image[r][c] = color
                visited.add((r, c))
                for r_adj, c_adj in directions:
                    if 0 <= r + r_adj < len(image) and 0 <= c + c_adj < len(image[0]):
                        if image[r + r_adj][c + c_adj] == original_color:
                            stack.append((r + r_adj, c + c_adj))
        
        return image

def main():
    sol = Solution()
    print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
    print(sol.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))

if __name__ == '__main__':
    main()