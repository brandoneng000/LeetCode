class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        left, right = 0, n - 1

        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
        
        s1, s2 = a[left: right + 1], b[left: right + 1]

        left, right = 0, n - 1
        while left < right and b[left] == a[right]:
            left += 1
            right -= 1
        s3, s4, = a[left: right + 1], b[left: right + 1]

        return any(s == s[::-1] for s in (s1, s2, s3, s4))

    # def checkPalindromeFormation(self, a: str, b: str) -> bool:
    #     n = len(a)
        
    #     for i in range(n):
    #         pre_a, suf_a = a[:i], a[i:]
    #         pre_b, suf_b = b[:i], b[i:]
            
    #         ab = pre_a + suf_b
    #         ba = pre_b + suf_a

    #         if ab == ab[::-1] or ba == ba[::-1]:
    #             return True
        
    #     return False

        
def main():
    sol = Solution()
    # print(sol.checkPalindromeFormation(a = "x", b = "y"))
    # print(sol.checkPalindromeFormation(a = "xbdef", b = "xecab"))
    print(sol.checkPalindromeFormation(a = "ulacfd", b = "jizalu"))

if __name__ == '__main__':
    main()