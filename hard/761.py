class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ''
        
        n = len(s)
        res = []
        count = 0
        i = j = 0

        while i < n:
            count += 1 if s[i] == '1' else -1

            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[j + 1: i]) + '0')
                j = i + 1
            
            i += 1
        
        res.sort(reverse=True)
        return ''.join(res)


def main():
    sol = Solution()
    print(sol.makeLargestSpecial("11011000"))
    print(sol.makeLargestSpecial("10"))

if __name__ == '__main__':
    main()