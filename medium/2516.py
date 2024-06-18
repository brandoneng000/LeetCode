from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        limits = Counter(s)

        for letter in 'abc':
            limits[letter] -= k

        if any(limits[letter] < 0 for letter in 'abc'):
            return -1
        
        count = Counter()
        res = left = 0

        for right, letter in enumerate(s):
            count[letter] += 1

            while count[letter] > limits[letter]:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return n - res


    # def takeCharacters(self, s: str, k: int) -> int:
    #     n = len(s)
    #     res = float('inf')
    #     s_count = Counter(s)

    #     if any(s_count[letter] < k for letter in 'abc'):
    #         return -1
        
    #     cur_count = Counter()
    #     for i in range(n):
    #         cur_count[s[i]] += 1
    #         temp_count = cur_count.copy()

    #         for j in range(n - 1, i, -1):
    #             temp_count[s[j]] += 1

    #             if all(temp_count[letter] >= k for letter in 'abc'):
    #                 res = min(res, i + (n - j + 1))
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.takeCharacters(s = "aabaaaacaabc", k = 2))
    print(sol.takeCharacters(s = "a", k = 1))

if __name__ == '__main__':
    main()