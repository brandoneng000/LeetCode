# import collections
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        count_s1 = Counter(s1)
        cur = Counter(s2[:m - 1])
        left = 0

        for right in range(m - 1, n):
            cur[s2[right]] += 1

            if cur == count_s1:
                return True
            
            cur[s2[left]] -= 1

            if cur[s2[left]] == 0:
                del cur[s2[left]]
            left += 1

        return False
        

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     m = len(s1)
    #     n = len(s2)
    #     sorted_s1 = sorted(s1)
    #     unique_s1 = set(s1)
        
    #     for i in range(n - m + 1):
    #         if s2[i] in unique_s1 and sorted_s1 == sorted(s2[i: i + m]):
    #             return True

    #     return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     count_s1 = collections.Counter(s1)
    #     unique_s1 = set(s1)
        
    #     for i in range(len(s2)):
    #         if s2[i] in unique_s1:
    #             if count_s1 == collections.Counter(s2[i: i + len(s1)]):
    #                 return True
        
    #     return False



def main():
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo"))

if __name__ == '__main__':
    main()