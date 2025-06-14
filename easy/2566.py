class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        t = str_num
        index = 0

        while index < n and str_num[index] == '9':
            index += 1
        
        if index < n:
            str_num = str_num.replace(str_num[index], '9')
        
        t = t.replace(t[0], '0')

        return int(str_num) - int(t)

    # def minMaxDifference(self, num: int) -> int:
    #     str_num = str(num)
    #     smallest = int(str_num.replace(str_num[0], '0'))
    #     largest = num

    #     for digit in str_num:
    #         if digit != '9':
    #             largest = int(str_num.replace(digit, '9'))
    #             break
        
    #     return largest - smallest
        

def main():
    sol = Solution()
    print(sol.minMaxDifference(11891))
    print(sol.minMaxDifference(90))
    print(sol.minMaxDifference(456))
    print(sol.minMaxDifference(333111222))

if __name__ == '__main__':
    main()