class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            cur_sum = 0
            cnt = 0

            for digit in s:
                num = int(digit)

                if cnt == k:
                    new_s += str(cur_sum)
                    cnt = 0
                    cur_sum = 0

                cur_sum += num
                cnt += 1
            new_s += str(cur_sum)
            s = new_s

        return s

    # def digitSum(self, s: str, k: int) -> str:
    #     while len(s) > k:
    #         temp = ""
    #         for index in range(0, len(s), k):
    #             temp += str(sum(map(int, s[index: index + k])))
    #         s = temp
        
    #     return s


def main():
    sol = Solution()
    print(sol.digitSum(s = "11111222223", k = 3))
    print(sol.digitSum(s = "00000000", k = 3))
    print(sol.digitSum(s = "1234", k = 2))

if __name__ == '__main__':
    main()