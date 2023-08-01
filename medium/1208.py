class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0

        for right in range(len(s)):
            maxCost -= abs(ord(s[right]) - ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
            
        return right - left + 1

    # def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    #     costs = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
    #     left = 0
    #     res = 0
    #     cur_max = 0
    #     cost = maxCost

    #     for right in range(len(costs)):
    #         if costs[right] <= cost:
    #             cost -= costs[right]
    #             cur_max += 1
    #         else:
    #             cost += costs[left]
    #             cost -= costs[right]
    #             left += 1
            
    #         res = max(res, cur_max)
        
    #     return res

def main():
    sol = Solution()
    print(sol.equalSubstring(s = "ujteygggjwxnfl", t = "nstsenrzttikoy", maxCost = 43))
    print(sol.equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19))
    print(sol.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
    print(sol.equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
    print(sol.equalSubstring(s = "abcd", t = "acde", maxCost = 0))

if __name__ == '__main__':
    main()