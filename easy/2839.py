class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        s1_list = list(s1)
        s2_list = list(s2)

        s1_list[0], s1_list[2] = s1_list[2], s1_list[0]
        if s1_list == s2_list:
            return True
        
        s1_list[1], s1_list[3] = s1_list[3], s1_list[1]
        if s1_list == s2_list:
            return True
        
        s1_list = list(s1)
        s2_list = list(s2)

        s1_list[1], s1_list[3] = s1_list[3], s1_list[1]
        if s1_list == s2_list:
            return True
        
        return False
        
        
def main():
    sol = Solution()
    print(sol.canBeEqual(s1 = "abcd", s2 = "cdab"))
    print(sol.canBeEqual(s1 = "abcd", s2 = "dacb"))

if __name__ == '__main__':
    main()