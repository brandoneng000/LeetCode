class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        count = 0

        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            result = max(result, count)
        
        return result
        
def main():
    sol = Solution()
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(sol.maxDepth("(1)+((2))+(((3)))"))

if __name__ == '__main__':
    main()