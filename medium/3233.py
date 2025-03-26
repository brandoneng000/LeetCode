class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        res = r - l + 1
        right_limit = int(r ** 0.5)
        prime = [True] * (right_limit + 1)
        prime[0] = prime[1] = False

        for i in range(2, int(right_limit ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, right_limit + 1, i):
                    prime[j] = False

        for num in range(2, right_limit + 1):
            if prime[num]:
                square = num * num
                if l <= square <= r:
                    res -= 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.nonSpecialCount(l = 5, r = 7))
    print(sol.nonSpecialCount(l = 4, r = 16))

if __name__ == '__main__':
    main()