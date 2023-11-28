class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 1000000007
        seats = 0
        plants = 1
        plants_between = []

        for space in corridor:
            if seats == 2 and space == 'P':
                plants += 1
            elif space == 'S':
                if seats == 2:
                    seats = 0
                    plants_between.append(plants)
                    plants = 1
                seats += 1
        
        if seats == 2 and not plants_between:
            return 1
        
        if not plants_between or seats == 1:
            return 0
        
        res = 1
        for p in plants_between:
            res *= p
        
        return res % mod


def main():
    sol = Solution()
    print(sol.numberOfWays("SSPPSPS"))
    print(sol.numberOfWays("PPSPSP"))
    print(sol.numberOfWays("S"))
    print(sol.numberOfWays("SSPPSSPPSSPPSS"))
    print(sol.numberOfWays("SSPPSSPPPSSPPSS"))

if __name__ == '__main__':
    main()