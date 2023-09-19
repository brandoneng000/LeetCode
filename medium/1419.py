import collections

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak_count = collections.Counter()
        frogs = 0
        res = 0

        for c in croakOfFrogs:
            if c == 'c':
                frogs += 1
            elif c == 'k':
                frogs -= 1
            
            croak_count[c] += 1

            for u, v in zip("croa", "roak"):
                if croak_count[u] < croak_count[v]:
                    return -1

            res = max(res, frogs)
        
        return res if all(croak_count[c] == croak_count['c'] for c in croak_count) else -1
        
def main():
    sol = Solution()
    print(sol.minNumberOfFrogs("croakcroak"))
    print(sol.minNumberOfFrogs("crcoakroak"))
    print(sol.minNumberOfFrogs("croakcrook"))

if __name__ == '__main__':
    main()