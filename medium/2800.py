class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def helper(str1: str, str2: str):
            if str2 in str1:
                return str1
            
            for i in range(len(str1)):
                if str2.startswith(str1[i:]):
                    return str1[:i] + str2
            
            return str1 + str2

        res = ''
        res_length = float('inf')

        ab = helper(a, b)
        ba = helper(b, a)
        bc = helper(b, c)
        cb = helper(c, b)
        ac = helper(a, c)
        ca = helper(c, a)

        abc = helper(ab, c)
        bac = helper(ba, c)
        bca = helper(bc, a)
        cba = helper(cb, a)
        acb = helper(ac, b)
        cab = helper(ca, b)

        for combo in [abc, bac, bca, cba, acb, cab]:
            if len(combo) < res_length:
                res = combo
                res_length = len(combo)
            elif len(combo) == res_length:
                res = min(res, combo)
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.minimumString(a = "abc", b = "bca", c = "aaa"))
    print(sol.minimumString(a = "ab", b = "ba", c = "aba"))

if __name__ == '__main__':
    main()