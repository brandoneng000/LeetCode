class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cur_sum = 0
        res = 0

        for bit in s[::-1]:
            if bit == '0':
                res += 1
            elif cur_sum + (1 << res) <= k:
                cur_sum += (1 << res)
                res += 1
            
        return res
        
def main():
    sol = Solution()
    print(sol.longestSubsequence(s = "1001010", k = 5))
    print(sol.longestSubsequence(s = "00101001", k = 1))

if __name__ == '__main__':
    main()