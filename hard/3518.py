class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def comb(n: int, m: int, k_limit: int) -> int:
            res = 1
            m = min(m, n - m)

            for i in range(1, m + 1):
                res = res * (n - i + 1) // i

                if res > k_limit:
                    return k_limit + 1

            return res

        def permutations(rem: int) -> int:
            ways = 1

            for i in range(26):
                if bucket[i] == 0:
                    continue

                ways *= comb(rem, bucket[i], k)

                if ways > k:
                    break
                rem -= bucket[i]

            return ways

        partition = len(s) // 2
        bucket = [0] * 26
        a = ord('a')

        for i in range(partition):
            bucket[ord(s[i]) - a] += 1

        left_chars = []
        start_index = 1

        for pos in range(partition):
            for i in range(26):
                if bucket[i] == 0:
                    continue

                bucket[i] -= 1

                ways = permutations(partition - pos - 1)

                if start_index + ways > k:
                    left_chars.append(chr(i + a))
                    break

                bucket[i] += 1
                start_index += ways

        if len(left_chars) < partition:
            return ""

        mid = s[partition] if len(s) % 2 != 0 else ""
        left_str = ''.join(left_chars)
        right_str = left_str[::-1]

        return left_str + mid + right_str


def main():
    sol = Solution()
    print(sol.smallestPalindrome(s = "abba", k = 2))
    print(sol.smallestPalindrome(s = "aa", k = 2))
    print(sol.smallestPalindrome(s = "bacab", k = 1))

if __name__ == '__main__':
    main()