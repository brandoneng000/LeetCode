class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        free = 0

        for seat in s:
            if seat == 'E':
                if free == 0:
                    res += 1
                else:
                    free -= 1
            else:
                free += 1
        
        return res


def main():
    sol = Solution()
    print(sol.minimumChairs("EEEEEEE"))
    print(sol.minimumChairs("ELELEEL"))
    print(sol.minimumChairs("ELEELEELLL"))

if __name__ == '__main__':
    main()