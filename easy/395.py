import collections

class Solution:
    # def longestSubstring(self, s: str, k: int) -> int:
    #     if k == 1:
    #         return len(s)
        
    #     res = 0
    #     cache = {}

    #     for i in range(len(s) - 1):
    #         for j in range(i + 1, len(s)):
    #             if s[i: j] in cache and s[j] in s[i: j]:
    #                 cache[s[i: j + 1]] = cache[s[i: j]] + 1
    #                 res = max(res, cache[s[i: j + 1]])
    #             elif self.check_valid(s[i: j + 1], k):
    #                 cache[s[i: j + 1]] = len(s[i: j + 1])
    #                 res = max(res, cache[s[i: j + 1]])
    #         if res == len(s):
    #             break
        
    #     return res

    # def check_valid(self, s: str, k: int) -> bool:
    #     str_counter = collections.Counter(s)
    #     return all(str_counter[key] >= k for key in str_counter)

    def longestSubstring(self, s: str, k: int) -> int:
        return self.split(s, k, 0, len(s))
    
    def split(self, s: str, k: int, start: int, end: int) -> int:
        if end < k: return 0
        str_counter = collections.Counter(s[start: end])
        for mid in range(start, end):
            if str_counter[s[mid]] >= k:
                continue
            
            next = mid + 1
            while next < end and str_counter[s[next]] < k:
                next += 1
            return max(self.split(s, k, start, mid), self.split(s, k, next, end))
    
        return end - start

        
def main():
    sol = Solution()
    print(sol.longestSubstring(s = "aaabb", k = 3))
    print(sol.longestSubstring(s = "ababbc", k = 2))
    print(sol.longestSubstring(s = "abcabc", k = 2))

if __name__ == '__main__':
    main()