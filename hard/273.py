class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(num: int):
            if num > 99:
                if num % 100 == 0:
                    return f"{d[num // 100]} Hundred"
                else:
                    return f"{d[num // 100]} Hundred {helper(num % 100)}"
            else:
                if num < 20:
                    return d[num]
                elif num % 10 == 0:
                    return d[num]
                else:
                    tens, ones = divmod(num, 10)
                    tens *= 10

                    return f"{d[tens]} {d[ones]}"

        d = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        num_split = [0]
        denom = ["", " Thousand", " Million", " Billion"]
        temp = num
        count = 0

        while temp:
            num_split[-1] += (temp % 10) * (10 ** count)
            temp //= 10
            count += 1

            if count == 3 and temp:
                count = 0
                num_split.append(0)                
            
        res = []

        for i, num in enumerate(num_split):
            if num == 0 and len(num_split) > 1:
                pass
            else:
                res.append(f"{helper(num)}{denom[i]}")

        return " ".join(res[::-1])


def main():
    sol = Solution()
    print(sol.numberToWords(1000))
    # print(sol.numberToWords(1000000))
    # print(sol.numberToWords(1000000000))
    # print(sol.numberToWords(100))
    # print(sol.numberToWords(90))
    # print(sol.numberToWords(53))
    # print(sol.numberToWords(123))
    # print(sol.numberToWords(1235))
    print(sol.numberToWords(1234567))

if __name__ == '__main__':
    main()