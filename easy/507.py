class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # divisors = set([1])
        # low, high = 1, num

        # while low < high:
        #     low += 1
        #     if num % low == 0:
        #         divisors.add(low)
        #         high = num // low
        #         divisors.add(high)
        #     if sum(divisors) > num:
        #         return False
                
        # return sum(divisors) == num

        if num <= 0:
            return False
        
        sum = 0
        i = 1
        # Only iterates to sqrt of num
        while i * i <= num:
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num // i

            i += 1

        return sum - num == num

def main():
    sol = Solution()
    print(sol.checkPerfectNumber(28))
    print(sol.checkPerfectNumber(7))
    print(sol.checkPerfectNumber(30402457))


if __name__ == '__main__':
    main()