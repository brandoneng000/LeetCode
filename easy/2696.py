class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            s = s.replace('AB', '')
            s = s.replace('CD', '')
        
        return len(s)

    # def minLength(self, s: str) -> int:
    #     stack = []

    #     for letter in s:
    #         stack.append(letter)
    #         if stack[-2:] == ['A', 'B'] or stack[-2:] == ['C', 'D']:
    #             stack.pop()
    #             stack.pop()
        
    #     return len(stack)
        
def main():
    sol = Solution()
    print(sol.minLength("ABFCACDB"))
    print(sol.minLength("ACBBD"))

if __name__ == '__main__':
    main()