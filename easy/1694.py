class Solution:
    def reformatNumber(self, number: str) -> str:
        res = []
        number = number.replace(" ", "").replace("-", "")
        index = 0
        size = len(number)
        block = ""

        if size <= 3:
            return number

        while index < size:
            block += number[index]
            index += 1

            if len(block) == 3:
                remainder = size - index
                if remainder == 1:
                    block += number[index]
                    res.append(block[:2])
                    res.append(block[2:])
                    break
                elif remainder == 2:
                    res.append(block)
                    res.append(number[-2:])
                    break
                res.append(block)
                block = ""
            
        return "-".join(res)
        
        
def main():
    sol = Solution()
    print(sol.reformatNumber("1-23-45 6"))
    print(sol.reformatNumber("123 4-567"))
    print(sol.reformatNumber("123 4-5678"))
    print(sol.reformatNumber("321 333 3333"))
    print(sol.reformatNumber("12"))

if __name__ == '__main__':
    main()