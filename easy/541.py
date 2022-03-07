class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        reverse = ""
        index = 0

        while index <= len(s) - 2 * k:
            sub = s[index: index + k]
            reverse += sub[::-1]
            index += k
            reverse += s[index: index + k]
            index += k
        

        if len(s) - index < 2 * k and len(s) - index >= k:
            sub = s[index: index + k]
            reverse += sub[::-1]
            index += k
            reverse += s[index:]
        elif len(s) - index < k:
            sub = s[index:]
            reverse += sub[::-1]
            index += k

        return reverse

def main():
    sol = Solution()
    print(sol.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))
    print(sol.reverseStr("abcdefg", 3))
    print(sol.reverseStr("abcdefg", 2))
    print(sol.reverseStr("ab", 3))
    print(sol.reverseStr("abcdefghi", 3))

if __name__ == '__main__':
    main()