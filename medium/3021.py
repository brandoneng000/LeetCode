class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_even = n_odd = n // 2
        n_odd += n % 2

        m_even = m_odd = m // 2
        m_odd += m % 2

        return n_even * m_odd + n_odd * m_even

def main():
    sol = Solution()
    print(sol.flowerGame(n = 3, m = 2))
    print(sol.flowerGame(n = 1, m = 1))

if __name__ == '__main__':
    main()