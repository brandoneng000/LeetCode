class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        
def main():
    sol = Solution()
    print(sol.countSegments("Hello, my name is John"))

if __name__ == '__main__':
    main()