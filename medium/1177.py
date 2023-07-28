from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = 26
        a = ord('a')
        dp = [[0] * n]
        for i in range(1, len(s) + 1):
            new_string = dp[i - 1][:]
            j = ord(s[i - 1]) - a
            new_string[j] += 1
            dp.append(new_string)
        
        res = []

        for start, end, rep in queries:
            left = dp[start]
            right = dp[end + 1]
            res.append(sum((right[i] - left[i]) & 1 for i in range(n)) // 2 <= rep)
        
        return res

    # def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    #     def check_palin(start: int, end: int, replace: int):
    #         if (start, end) in cache:
    #             return cache[start, end] <= replace
            
    #         count = 0
    #         string_count = collections.Counter(s[start: end + 1])

    #         for letter in string_count:
    #             count += string_count[letter] % 2
            
    #         cache[start, end] = count // 2
    #         return cache[start, end] <= replace

    #     res = []
    #     cache = {}
    #     for start, end, rep in queries:
    #         res.append(check_palin(start, end, rep))
        
    #     return res

def main():
    sol = Solution()
    print(sol.canMakePaliQueries(s = "qzcdmvmfinetotshixuto", queries = [[8,16,1]]))
    print(sol.canMakePaliQueries(s = "hunu", queries = [[0,3,1]]))
    print(sol.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
    print(sol.canMakePaliQueries(s = "lyb", queries = [[0,1,0],[2,2,1]]))

if __name__ == '__main__':
    main()