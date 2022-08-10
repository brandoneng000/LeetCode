from typing import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        count = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                count += 1

        return count < 3 and Counter(s1) == Counter(s2)

def main():
    sol = Solution()
    print(sol.areAlmostEqual(s1 = "bank", s2 = "kanb"))
    print(sol.areAlmostEqual(s1 = "attack", s2 = "defend"))
    print(sol.areAlmostEqual(s1 = "kelb", s2 = "kelb"))
    print(sol.areAlmostEqual(s1 = "asdf", s2 = "fdsa"))

if __name__ == '__main__':
    main()