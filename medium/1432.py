class Solution:
    def maxDiff(self, num: int) -> int:
        largest = str(num)
        large_rep = '9'
        smallest = str(num)
        small_rep = '1'
        first = smallest[0]

        for digit in largest:
            if digit != '9':
                large_rep = digit
                break
        
        largest = largest.replace(large_rep, '9')

        for digit in smallest:
            if digit == first and digit != '1':
                small_rep = digit
                break
            elif digit != first and digit != '0':
                small_rep = digit
                break
        
        if small_rep == first:
            smallest = smallest.replace(small_rep, '1')
        else:
            smallest = smallest.replace(small_rep, '0')
        
        return int(largest) - int(smallest)
        

def main():
    sol = Solution()
    print(sol.maxDiff(555))
    print(sol.maxDiff(8))

if __name__ == '__main__':
    main()