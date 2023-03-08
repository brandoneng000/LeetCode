class Solution:
    def maximum69Number(self, num: int) -> int:
        if str(num).count('6') == 0:
            return num
        else:
            return int(str(num).replace('6', '9', 1))

def main():
    sol = Solution()
    print(sol.maximum69Number(9669))
    print(sol.maximum69Number(9996))
    print(sol.maximum69Number(9999))

if __name__ == '__main__':
    main()