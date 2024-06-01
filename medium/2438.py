from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        power = []
        exponent = 0
        temp = n
        res = []

        while temp:
            if temp & 1:
                power.append(2 ** exponent)
            
            temp >>= 1
            exponent += 1
        
        prefix = [1] + power

        for i in range(1, len(prefix)):
            prefix[i] *= prefix[i - 1]
        
        for start, end in queries:
            res.append(prefix[end + 1] // prefix[start] % mod) 
        
        return res

        
def main():
    sol = Solution()
    print(sol.productQueries(n = 15, queries = [[0,1],[2,2],[0,3]]))
    print(sol.productQueries(n = 2, queries = [[0,0]]))

if __name__ == '__main__':
    main()