class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if not k:
            return s
        
        n = len(s)
        res = list(s)

        for i in range(n):
            if s[i] == 'a':
                continue
            
            char_val = ord(s[i]) - ord('a')
            distance_forward = 26 - char_val
            distance_backward = char_val

            if min(distance_backward, distance_forward) <= k:
                k -= min(distance_backward, distance_forward)
                res[i] = 'a'
            else:
                res[i] = chr(ord('a') + char_val - k)
                break
        
        return ''.join(res)

        
def main():
    sol = Solution()
    print(sol.getSmallestString(s = "zbbz", k = 3))
    print(sol.getSmallestString(s = "xaxcd", k = 4))
    print(sol.getSmallestString(s = "lol", k = 0))

if __name__ == '__main__':
    main()