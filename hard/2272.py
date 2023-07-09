import collections

class Solution:
    def largestVariance(self, s: str) -> int:
        letters = set(s)
        if len(letters) == len(s) or len(letters) == 1:
            return 0
        
        count = collections.Counter(s)
        res = 0

        for first in letters:
            for second in letters:
                if first == second:
                    continue

                major = 0
                minor = 0
                remainder_minor = count[second]

                for letter in s:
                    if letter == first:
                        major += 1
                    
                    if letter == second:
                        minor += 1
                        remainder_minor -= 1
                    
                    if minor > 0:
                        res = max(res, major - minor)
                    
                    if major < minor and remainder_minor > 0:
                        major = 0
                        minor = 0
        
        return res


    # def largestVariance(self, s: str) -> int:
    #         if len(set(s)) == len(s) or len(set(s)) == 1:
    #             return 0
            
    #         cache = {}
            
    #         for i in range(3, len(s) + 1):
    #             left = 0
    #             right = i
    #             count = collections.Counter(s[left:right])
    #             while right < len(s) + 1:
    #                 cur = s[left: right]
    #                 if cur not in cache and len(set(cur)) >= 2:
    #                     cache[cur] = max(count.values()) - min(count.values())
    #                 count[s[left]] -= 1
    #                 if count[s[left]] == 0:
    #                     count.pop(s[left])
    #                 if right < len(s):
    #                     count[s[right]] += 1
    #                 left += 1
    #                 right += 1

    #         return max(cache.values())
        
                

def main():
    sol = Solution()
    print(sol.largestVariance("lripaa"))
    print(sol.largestVariance("aababbb"))
    print(sol.largestVariance("abcde"))

if __name__ == '__main__':
    main()