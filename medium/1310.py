from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = arr.copy()

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] ^ prefix[i - 1]
        
        for left, right in queries:
            left = prefix[left - 1] if left > 0 else 0
            res.append(prefix[right] ^ left)
        
        return res

    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     res = []
        
    #     for left, right in queries:
    #         cur = 0

    #         for index in range(left , right + 1):
    #             cur ^= arr[index]
            
    #         res.append(cur)
        
    #     return res

def main():
    sol = Solution()
    print(sol.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
    print(sol.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))

if __name__ == '__main__':
    main()