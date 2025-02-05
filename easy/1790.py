from typing import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return sum(s1[i] != s2[i] for i in range(len(s1))) < 3 and Counter(s1) == Counter(s2)

    # def areAlmostEqual(self, s1: str, s2: str) -> bool:
    #     n = len(s1)
    #     count_s1 = Counter()
    #     count_s2 = Counter()
    #     count = 0

    #     for i in range(n):
    #         count_s1[s1[i]] += 1
    #         count_s2[s2[i]] += 1
    #         count += s1[i] != s2[i]
        
    #     return count < 3 and count_s1 == count_s2


    # def areAlmostEqual(self, s1: str, s2: str) -> bool:
    #     if s1 == s2:
    #         return True
        
    #     count = 0
    #     for index in range(len(s1)):
    #         if s1[index] != s2[index]:
    #             count += 1

    #     return count < 3 and Counter(s1) == Counter(s2)

def main():
    sol = Solution()
    print(sol.areAlmostEqual(s1 = "bank", s2 = "kanb"))
    print(sol.areAlmostEqual(s1 = "attack", s2 = "defend"))
    print(sol.areAlmostEqual(s1 = "kelb", s2 = "kelb"))
    print(sol.areAlmostEqual(s1 = "asdf", s2 = "fdsa"))

if __name__ == '__main__':
    main()