from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i + 1 for i in range(m)]
        res = []

        for val in queries:
            res.append(p.index(val))
            temp = p.pop(res[-1])
            p = [temp] + p
        
        return res

def main():
    sol = Solution()
    print(sol.processQueries(queries = [3,1,2,1], m = 5))
    print(sol.processQueries(queries = [4,1,2,2], m = 4))
    print(sol.processQueries(queries = [7,5,5,8,3], m = 8))

if __name__ == '__main__':
    main()