class Solution:
    def longestBalanced(self, s: str) -> int:
        def _single(s: str):
            if not s:
                return 0
            
            count = 1
            res = 1

            for i in range(1, n):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    count = 1
                res = max(res, count)
            
            return res
        
        def _duo(s: str, c1: str, c2: str):
            pos = { 0: -1 }
            res = 0
            delta = 0

            for i, char in enumerate(s):
                if char != c1 and char != c2:
                    pos = {}
                    pos[0] = i
                    delta = 0
                    continue

                if char == c1:
                    delta += 1
                else:
                    delta -= 1
                
                if delta in pos:
                    res = max(res, i - pos[delta])
                else:
                    pos[delta] = i
            
            return res

        def _trio(s: str):
            c1 = c2 = c3 = 0
            pos = { (0, 0): -1 }
            res = 0

            for i, char in enumerate(s):
                if char == 'a':
                    c1 += 1
                elif char == 'b':
                    c2 += 1
                else:
                    c3 += 1
                
                key = (c2 - c1, c3 - c1)

                if key in pos:
                    res = max(res, i - pos[key])
                else:
                    pos[key] = i
            
            return res


        n = len(s)
        return max(
            _single(s),
            _duo(s, 'a', 'b'),
            _duo(s, 'b', 'c'),
            _duo(s, 'a', 'c'),
            _trio(s)
        )

        
def main():
    sol = Solution()
    print(sol.longestBalanced("abbac"))
    print(sol.longestBalanced("aabcc"))
    print(sol.longestBalanced("aba"))

if __name__ == '__main__':
    main()