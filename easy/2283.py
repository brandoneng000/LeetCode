import collections

class Solution:
    def digitCount(self, num: str) -> bool:
        check = ""

        for index, digit in enumerate(num):
            check += str(index) * int(digit)
        
        return  "".join(sorted(num)) == check

        # check = {}

        # for index, digit in enumerate(num):
        #     check[str(index)] = int(digit)
        
        # check = collections.Counter(check)
        # num = collections.Counter(num)

        # return num == check

        # num_count = collections.Counter(num)

        # for index, digit in enumerate(num):
        #     if int(digit) != num_count.get(str(index), 0):
        #         return False

        # return True


def main():
    sol = Solution()
    print(sol.digitCount("1210"))
    print(sol.digitCount("030"))
    print(sol.digitCount("0"))
    print(sol.digitCount("1"))

if __name__ == '__main__':
    main()