class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        res = 0
        cur_key = s[0]

        for key in s:
            res += cur_key != key
            cur_key = key
        
        return res

        
def main():
    sol = Solution()
    print(sol.countKeyChanges("aAbBcC"))
    print(sol.countKeyChanges("AaAaAaaA"))

if __name__ == '__main__':
    main()