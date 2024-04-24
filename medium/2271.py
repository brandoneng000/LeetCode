from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        right = 0
        cover = 0
        res = 0

        for left in range(n):
            while right < n and tiles[right][1] - tiles[left][0] + 1 <= carpetLen:
                cover += tiles[right][1] - tiles[right][0] + 1
                right += 1
            
            if right < n and tiles[right][0] - tiles[left][0] + 1 <= carpetLen:
                res = max(res, cover + carpetLen - (tiles[right][0] - tiles[left][0]))
            else:
                res = max(res, cover)
            
            if left != right:
                cover -= tiles[left][1] - tiles[left][0] + 1
            
            right = max(right, left + 1)

        return res
    
def main():
    sol = Solution()
    print(sol.maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))
    print(sol.maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2))

if __name__ == '__main__':
    main()