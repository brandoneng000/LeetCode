from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row_size = len(image)
        col_size = len(image[0])

        for r in range(row_size):
            for c in range(col_size // 2):
                image[r][c], image[r][col_size - c - 1] = image[r][col_size - c - 1], image[r][c]

        for r in range(row_size):
            for c in range(col_size):
                image[r][c] = 0 if image[r][c] else 1
        
        return image

def main():
    sol = Solution()
    print(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

if __name__ == '__main__':
    main()