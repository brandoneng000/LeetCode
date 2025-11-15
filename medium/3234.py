class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        res = 0

        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]
        
        for i in range(1, n + 1):
            count_zero = 1 if s[i - 1] == '0' else 0

            j = i

            while j > 0 and count_zero * count_zero <= n:
                count_one = (i - pre[j]) - count_zero

                if count_zero * count_zero <= count_one:
                    res += min((j - pre[j], count_one - count_zero * count_zero + 1))
                j = pre[j]
                count_zero += 1
        
        return res
                
            

    # def numberOfSubstrings(self, s: str) -> int:
    #     res = 0
    #     zero_index = []

    #     for i, bit in enumerate(s):
    #         if bit == '0':
    #             zero_index.append(i)
            
    #         j = 0

    #         while j <= len(zero_index):
    #             target_length = j * j + j

    #             if target_length > i + 1:
    #                 break

    #             left_index = zero_index[-1 - j] if j < len(zero_index) else -1
    #             right_index = zero_index[-j] if j > 0 else i

    #             min_length = i - right_index + 1
    #             max_length = i - left_index

    #             if min_length >= target_length:
    #                 res += max_length - min_length + 1
    #             elif min_length <= target_length <= max_length:
    #                 res+= max_length - target_length + 1
                
    #             j += 1
        
    #     return res


    # def numberOfSubstrings(self, s: str) -> int:
    #     n = len(s)
    #     res = 0
    #     prefix = [0] * n
    #     prefix[0] = int(s[0])

    #     for i in range(1, n):
    #         prefix[i] = prefix[i - 1] + int(s[i])
        
    #     for i in range(n):
    #         one = 0
    #         zero = 0
    #         j = i

    #         while j < n:
    #             one = prefix[j] - (0 if i == 0 else prefix[i - 1])
    #             zero = (j - i + 1) - one

    #             if one >= zero * zero:
    #                 res += 1

    #                 if one > zero * zero:
    #                     diff = int(one ** 0.5) - zero

    #                     if j + diff < n:
    #                         res += diff
    #                     else:
    #                         res += n - j - 1

    #                     j += diff + 1
    #                 else:
    #                     j += 1
    #             else:
    #                 j += zero * zero - one
            
    #     return res
        
def main():
    sol = Solution()
    print(sol.numberOfSubstrings("00011"))
    print(sol.numberOfSubstrings("101101"))

if __name__ == '__main__':
    main()