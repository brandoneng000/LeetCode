class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}
        
        def helper(index: int, k: int, prev_char: str, prev_count: int):
            if (index, k, prev_char, prev_count) in cache:
                return cache[(index, k, prev_char, prev_count)] 
            
            if k < 0:
                return float('inf')
            if index == len(s):
                return 0

            if s[index] == prev_char:
                increment = 1 if prev_count in [1, 9, 99] else 0
                res = increment + helper(index + 1, k, prev_char, prev_count + 1)
            else:
                res = min(helper(index + 1, k - 1, prev_char, prev_count), 1 + helper(index + 1, k, s[index], 1))
            
            cache[(index, k, prev_char, prev_count)] = res
            return res

        return helper(0, k, "", 0)
        
def main():
    sol = Solution()
    print(sol.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
    print(sol.getLengthOfOptimalCompression(s = "aabbaa", k = 2))
    print(sol.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))

if __name__ == '__main__':
    main()