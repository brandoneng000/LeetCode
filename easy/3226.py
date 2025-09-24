class Solution:
    def minChanges(self, n: int, k: int) -> int:
        binary_n = f'{n:020b}'
        binary_k = f'{k:020b}'
        res = 0

        for i in range(20):
            if binary_n[i] != binary_k[i]:
                if binary_n[i] == '1':
                    res += 1
                else:
                    return -1
        
        return res
        

        
def main():
    sol = Solution()
    print(sol.minChanges(n = 13, k = 4))
    print(sol.minChanges(n = 21, k = 21))
    print(sol.minChanges(n = 14, k = 13))

if __name__ == '__main__':
    main()