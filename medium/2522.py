class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur = 0
        res = 0

        for digit in s:
            val = int(digit)
            total = cur * 10 + val

            if total < k:
                cur = total
            elif total == k:
                cur = 0
                res += 1
            else:
                cur = val

                if cur > k:
                    return -1

                res += 1
        
        return res + (1 if cur else 0)

        
def main():
    sol = Solution()
    print(sol.minimumPartition(s = "165462", k = 60))
    print(sol.minimumPartition(s = "238182", k = 5))

if __name__ == '__main__':
    main()