class Solution:
    def magicalString(self, n: int) -> int:
        s = [1,2,2]
        index = 2
        while len(s) < n:
            s += s[index] * [3 - s[-1]]
            index += 1
        
        return s[:n].count(1)


def main():
    sol = Solution()
    print(sol.magicalString(600))
    print(sol.magicalString(6))
    print(sol.magicalString(1))

if __name__ == '__main__':
    main()