class Solution:
    def findLatestTime(self, s: str) -> str:
        res = list(s)

        if res[0] == '?':
            if res[1] != '?' and int(res[1]) > 1:
                res[0] = '0'
            else:
                res[0] = '1'
        
        if res[1] == '?':
            if res[0] == '0':
                res[1] = '9'
            else:
                res[1] = '1'
        
        if res[3] == '?':
            res[3] = '5'
        
        if res[4] == '?':
            res[4] = '9'
        
        return ''.join(res)
        
def main():
    sol = Solution()
    print(sol.findLatestTime("1?:?4"))
    print(sol.findLatestTime("0?:5?"))

if __name__ == '__main__':
    main()