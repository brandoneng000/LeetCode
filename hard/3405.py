MOD = 1_000_000_007
MX = 10 ** 5

fact = [0] * MX
inv_fact = [0] * MX

def qpow(x: int, n: int):
    res = 1

    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    
    return res

def init():
    if fact[0] != 0:
        return
    
    fact[0] = 1

    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)

    for i in range(MX - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

def comb(n: int, m: int):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD 
        
        
def main():
    sol = Solution()
    print(sol.countGoodArrays(n = 3, m = 2, k = 1))
    print(sol.countGoodArrays(n = 4, m = 2, k = 2))
    print(sol.countGoodArrays(n = 5, m = 2, k = 0))

if __name__ == '__main__':
    main()