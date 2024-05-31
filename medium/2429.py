class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count('1')
        bits2 = bin(num2).count('1')
        num1_binary = list(bin(num1))[2:]
        num1_binary = ['0'] * (32 - len(num1_binary)) + num1_binary

        # equal bits
        if bits1 == bits2:
            return num1
        # more bits in num1
        elif bits1 > bits2:
            remainder = bits2
            res = ['0'] * 32

            for i in range(32):
                if num1_binary[i] == '1':
                    num1_binary[i] = '0'
                    res[i] = '1'
                    remainder -= 1
                
                if not remainder:
                    break
            
            return int(''.join(res), 2)
        
        # more bits in num2
        else:
            remainder = bits2 - bits1

            for i in range(len(num1_binary) - 1, -1, -1):
                if num1_binary[i] == '0' and remainder:
                    num1_binary[i] = '1'
                    remainder -= 1
                
                if not remainder:
                    break
        
            return int(''.join(num1_binary), 2)


def main():
    sol = Solution()
    print(sol.minimizeXor(num1 = 7, num2 = 2))
    print(sol.minimizeXor(num1 = 3, num2 = 5))
    print(sol.minimizeXor(num1 = 1, num2 = 12))

if __name__ == '__main__':
    main()