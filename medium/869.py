import collections

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = ['1']
        val = 1
        size = len(str(n))
        for i in range(32):
            val *= 2
            if len(str(val)) == size:
                powers.append(str(val))
            elif len(str(val)) > size:
                break
        
        n_counter = collections.Counter(str(n))
        return any(collections.Counter(p) == n_counter for p in powers)

def main():
    sol = Solution()
    print(sol.reorderedPowerOf2(1))
    print(sol.reorderedPowerOf2(10))

if __name__ == '__main__':
    main()