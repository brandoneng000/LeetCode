class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        factor = [2, 3, 5]
        indices = [0, 0, 0]
        for i in range(1, n):
            smallest = min(factor)
            ugly[i] = smallest
            if factor[0] == smallest:
                indices[0] += 1
                factor[0] = 2 * ugly[indices[0]]
            if factor[1] == smallest:
                indices[1] += 1
                factor[1] = 3 * ugly[indices[1]]
            if factor[2] == smallest:
                indices[2] += 1
                factor[2] = 5 * ugly[indices[2]]
        return ugly[-1]

    
def main():
    sol = Solution()
    print(sol.nthUglyNumber(10))
    print(sol.nthUglyNumber(1))
    print(sol.nthUglyNumber(11))

if __name__ == '__main__':
    main()