import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = collections.Counter(s1)
        unique_s1 = set(s1)
        
        for i in range(len(s2)):
            if s2[i] in unique_s1:
                if count_s1 == collections.Counter(s2[i: i + len(s1)]):
                    return True
        
        return False



def main():
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo"))

if __name__ == '__main__':
    main()