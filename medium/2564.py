from typing import List
from collections import defaultdict

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        max_val = 2 ** 32
        seen = defaultdict(lambda: [-1, -1])

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                seen[0] = [i, i]
                continue
            val = 0

            for j in range(i, n):
                val = val * 2 + int(s[j])
                if val > max_val:
                    break
                
                seen[val] = [i, j]
        
        return [seen[first ^ second] for first, second in queries]


    # def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
    #     res = []

    #     for first, second in queries:
    #         val = bin(first ^ second)[2:]
            
    #         try:
    #             index = s.index(val)
    #             res.append([index, index + len(val) - 1])
    #         except ValueError:
    #             res.append([-1, -1])
            
    #     return res
        
def main():
    sol = Solution()
    print(sol.substringXorQueries(s = "101101", queries = [[0,5],[1,2]]))
    print(sol.substringXorQueries(s = "0101", queries = [[12,8]]))
    print(sol.substringXorQueries(s = "1", queries = [[4,5]]))

if __name__ == '__main__':
    main()