class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        s_list = list(s)
        index = 0
        change = False

        while index < n and s_list[index] == 'a':
            index += 1

        while index < n and s_list[index] != 'a':
            s_list[index] = chr(ord(s_list[index]) - 1)
            index += 1
            change = True
        
        if not change:
            s_list[-1] = 'z'
            
        return ''.join(s_list)

        
def main():
    sol = Solution()
    print(sol.smallestString("cbabc"))
    print(sol.smallestString("aa"))
    print(sol.smallestString("acbbc"))
    print(sol.smallestString("leetcode"))

if __name__ == '__main__':
    main()