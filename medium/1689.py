class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
        
def main():
    sol = Solution()
    print(sol.minPartitions("32"))
    print(sol.minPartitions("82734"))
    print(sol.minPartitions("27346209830709182346"))

if __name__ == '__main__':
    main()