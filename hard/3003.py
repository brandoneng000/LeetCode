class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]
        res = 0
        
        num = mask = count = 0

        for i in range(n - 1):
            binary = 1 << (ord(s[i]) - ord('a'))

            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1

            left[i + 1][0] = num
            left[i + 1][1] = mask
            left[i + 1][2] = count
        
        num = mask = count = 0

        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord('a'))

            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            
            right[i - 1][0] = num
            right[i - 1][1] = mask
            right[i - 1][2] = count

        for i in range(n):
            seg = left[i][0] + right[i][0] + 2
            total_mask = left[i][1] | right[i][1]
            total_count = bin(total_mask).count('1')

            if left[i][2] == k and right[i][2] == k and total_count < 26:
                seg += 1
            elif min(total_count + 1, 26) <= k:
                seg -= 1
            res = max(res, seg)
        
        return res


def main():
    sol = Solution()
    print(sol.maxPartitionsAfterOperations(s = "accca", k = 2))
    print(sol.maxPartitionsAfterOperations(s = "aabaab", k = 3))
    print(sol.maxPartitionsAfterOperations(s = "xxyz", k = 1))

if __name__ == '__main__':
    main()