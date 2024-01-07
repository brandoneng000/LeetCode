class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = list(range(n))
        origin = list(range(n))
        count = 0
        
        while True:
            next = arr.copy()
            for i in range(n):
                if i % 2 == 0:
                    next[i] = arr[i // 2]
                else:
                    next[i] = arr[n // 2 + (i - 1) // 2]

            arr = next
            count += 1
            if arr == origin:
                break
        
        return count
        
def main():
    sol = Solution()
    print(sol.reinitializePermutation(2))
    print(sol.reinitializePermutation(4))
    print(sol.reinitializePermutation(6))

if __name__ == '__main__':
    main()