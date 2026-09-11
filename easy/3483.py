from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10
        res = 0

        for d in digits:
            cnt[d] += 1

        for i in range(1, 10):
            if cnt[i] == 0:
                continue

            cnt[i] -= 1

            for j in range(10):
                if cnt[j] == 0:
                    continue

                cnt[j] -= 1

                for k in range(0, 10, 2):
                    if cnt[k] == 0:
                        continue

                    res += 1

                cnt[j] += 1

            cnt[i] += 1

        return res

def main():
    sol = Solution()
    print(sol.totalNumbers([1,2,3,4]))
    print(sol.totalNumbers([0,2,2]))
    print(sol.totalNumbers([6,6,6]))
    print(sol.totalNumbers([1,3,5]))

if __name__ == '__main__':
    main()