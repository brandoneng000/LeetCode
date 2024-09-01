class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""

        n = len(s)
        min_size = n
        res = []
        left = 0
        cur = 0

        for right in range(n):
            cur += s[right] == '1'

            while cur == k:
                min_size = min(min_size, right - left + 1)
                cur -= s[left] == '1'
                left += 1

            if right - left + 1 > min_size:
                cur -= s[left] == '1'
                left += 1

        cur = s[:min_size - 1].count('1')
        left = 0

        for right in range(min_size - 1, n):
            cur += s[right] == '1'

            if cur == k:
                res.append(s[left: right + 1])
            
            cur -= s[left] == '1'
            left += 1
        
        return min(res)

def main():
    sol = Solution()
    print(sol.shortestBeautifulSubstring(s = "1101011", k = 3))
    print(sol.shortestBeautifulSubstring(s = "01011101000111110", k = 5))
    print(sol.shortestBeautifulSubstring(s = "100011001", k = 3))
    print(sol.shortestBeautifulSubstring(s = "1011", k = 2))
    print(sol.shortestBeautifulSubstring(s = "000", k = 1))

if __name__ == '__main__':
    main()