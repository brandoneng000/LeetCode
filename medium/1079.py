from typing import List
import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles_count = collections.Counter(tiles)

        def dfs():
            count = 0
            for tile in tiles_count:
                if tiles_count[tile] > 0:
                    tiles_count[tile] -= 1
                    count += dfs() + 1
                    tiles_count[tile] += 1

            return count

        return dfs()


    # def numTilePossibilities(self, tiles: str) -> int:
    #     n = len(tiles)
    #     tiles_count = collections.Counter(tiles)
    #     sequences = set()

    #     def helper(cur: List[str], size: int):
    #         if len(cur) == size:
    #             sequences.add(tuple(cur))
    #             return
            
    #         for tile in tiles_count:
    #             if tiles_count[tile] > 0:
    #                 tiles_count[tile] -= 1
    #                 cur.append(tile)
    #                 helper(cur, size)
    #                 tiles_count[tile] += 1
    #                 cur.pop()
            
        
    #     for i in range(1, n + 1):
    #         helper([], i)

    #     return len(sequences)

def main():
    sol = Solution()
    print(sol.numTilePossibilities("AAB"))
    print(sol.numTilePossibilities("AAABBC"))
    print(sol.numTilePossibilities("V"))

if __name__ == '__main__':
    main()