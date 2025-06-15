class Solution:
    # def maxDiff(self, num: int) -> int:
    #     def change_num(original: str, x: str):
    #         return str(num).replace(original, x)

    #     min_num = max_num = num
        
    #     for x in "0123456789":
    #         for y in "0123456789":
    #             res = change_num(x, y)

    #             if res[0] != '0':
    #                 res_int = int(res)
    #                 min_num = min(min_num, res_int)
    #                 max_num = max(max_num, res_int)
        
    #     return max_num - min_num

    def maxDiff(self, num: int) -> int:
        largest = str(num)
        smallest = str(num)
        first = smallest[0]

        for digit in largest:
            if digit != '9':
                largest = largest.replace(digit, '9')
                break

        for digit in smallest:
            if digit == first and digit != '1':
                smallest = smallest.replace(digit, '1')
                break
            elif digit != first and digit != '0':
                smallest = smallest.replace(digit, '0')
                break
        
        return int(largest) - int(smallest)
        


    # def maxDiff(self, num: int) -> int:
    #     largest = str(num)
    #     large_rep = '9'
    #     smallest = str(num)
    #     small_rep = '1'
    #     first = smallest[0]

    #     for digit in largest:
    #         if digit != '9':
    #             large_rep = digit
    #             break
        
    #     largest = largest.replace(large_rep, '9')

    #     for digit in smallest:
    #         if digit == first and digit != '1':
    #             small_rep = digit
    #             break
    #         elif digit != first and digit != '0':
    #             small_rep = digit
    #             break
        
    #     if small_rep == first:
    #         smallest = smallest.replace(small_rep, '1')
    #     else:
    #         smallest = smallest.replace(small_rep, '0')
        
    #     return int(largest) - int(smallest)
        

def main():
    sol = Solution()
    print(sol.maxDiff(555))
    print(sol.maxDiff(8))

if __name__ == '__main__':
    main()