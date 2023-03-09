from typing import List
import collections

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [sum(m) for m in mat]
        result = []
        mat_dict = collections.defaultdict(list)
        
        for index, val in enumerate(mat):
            mat_dict[val].append(index)

        for val in sorted(mat_dict.keys()):
            result.append(mat_dict[val])
        
        return sum(result, [])[:k]
        

def main():
    sol = Solution()
    print(sol.kWeakestRows([[1,1,0,0,0],\
                            [1,1,1,1,0],\
                            [1,0,0,0,0],\
                            [1,1,0,0,0],\
                            [1,1,1,1,1]], k = 3))
    print(sol.kWeakestRows([[1,0,0,0],\
                            [1,1,1,1],\
                            [1,0,0,0],\
                            [1,0,0,0]], k = 2))

if __name__ == '__main__':
    main()