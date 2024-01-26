from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check_subseq(s: str, p: str):
            index = 0

            for i in range(len(s)):
                if p[index] == s[i]:
                    index += 1
                if index == len(p):
                    return True
            
            return False

        left, right = 0, len(removable)

        while left <= right:
            middle = (left + right) // 2
            str_list = list(s)

            for i in range(middle):
                str_list[removable[i]] = ''
            
            if check_subseq(''.join(str_list), p):
                left = middle + 1
            else:
                right = middle - 1
        
        return right

        
def main():
    sol = Solution()
    print(sol.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))
    print(sol.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))
    print(sol.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]))

if __name__ == '__main__':
    main()