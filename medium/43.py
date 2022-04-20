class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        product = 0
        temp = 0

        for index, first in enumerate(num1[::-1]):
            cur = ord(first) - ord("0")

            for index_sec, second in enumerate(num2[::-1]):
                multiplier = ord(second) - ord("0")
                prod = cur * multiplier * (10 ** index_sec)
                temp += prod
            
            product += temp * (10 ** index)
            temp = 0
        
        return str(product)
        
def main():
    sol = Solution()
    print(sol.multiply("123", "456"))

if __name__ == '__main__':
    main()