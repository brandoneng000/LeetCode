class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        res = 1

        for letter in s:
            if letter in cur:
                cur.clear()
                res += 1
            cur.add(letter)
        
        return res
        
def main():
    sol = Solution()
    print(sol.partitionString("hdklqkcssgxlvehva"))
    print(sol.partitionString("abacaba"))
    print(sol.partitionString("ssssss"))

if __name__ == '__main__':
    main()