from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find_factors(num: int):
            if num in cache:
                return cache[num]
            
            res = 1 + num
            count = 2
            
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 2 if i * i != num else 1
                    res += i + num // i
                if count > 4:
                    break
            
            if count == 4:
                cache[num] = res
            else:
                cache[num] = 0
            
            return cache[num]

        cache = {}
        return sum(find_factors(n) for n in nums)
    
    # def sumFourDivisors(self, nums: List[int]) -> int:
    #     def find_factors(num: int):
    #         if num in cache:
    #             return cache[num]
            
    #         res = set([1, num])
            
    #         for i in range(2, int(num ** 0.5) + 1):
    #             if num % i == 0:
    #                 res.add(i)
    #                 res.add(num // i)
    #             if len(res) > 4:
    #                 break
            
    #         if len(res) == 4:
    #             cache[num] = sum(res)
    #         else:
    #             cache[num] = 0
            
    #         return cache[num]

    #     cache = {}
    #     return sum(find_factors(n) for n in nums)


def main():
    sol = Solution()
    print(sol.sumFourDivisors([8]))
    print(sol.sumFourDivisors([21,4,7]))
    print(sol.sumFourDivisors([21,21]))
    print(sol.sumFourDivisors([1,2,3,4,5]))

if __name__ == '__main__':
    main()