class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        def helper(powers_five, original_s):
            if not powers_five:
                return float('inf')

            s = original_s
            for i, p in enumerate(powers_five, 2):
                s = s.replace(p, str(i))
            
            if '0' in s:
                res = float('inf')
            else:
                res = len(s)
            
            return min(res, helper(powers_five[1:], original_s))

        powers_five = ['11110100001001', '110000110101', '1001110001', '1111101', '11001', '101']
        res = helper(powers_five, s)
        
        return res if res != float('inf') else -1
        
def main():
    sol = Solution()
    print(sol.minimumBeautifulSubstrings("101101111101"))
    print(sol.minimumBeautifulSubstrings("11110100001001"))
    print(sol.minimumBeautifulSubstrings("1011"))
    print(sol.minimumBeautifulSubstrings("111"))
    print(sol.minimumBeautifulSubstrings("0"))

if __name__ == '__main__':
    main()