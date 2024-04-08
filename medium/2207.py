class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def helper(text: str, pattern: str):
            first = 0
            res = 0

            for letter in text:
                if letter == pattern[1] and first > 0:
                    res += first
                if letter == pattern[0]:
                    first += 1
                
            
            return res
        
        return max(helper(pattern[0] + text, pattern), helper(text + pattern[1], pattern))
            
        
def main():
    sol = Solution()
    print(sol.maximumSubsequenceCount(text = "abdcdbc", pattern = "ac"))
    print(sol.maximumSubsequenceCount(text = "aabb", pattern = "ab"))

if __name__ == '__main__':
    main()