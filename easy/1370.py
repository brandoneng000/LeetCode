class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        dictionary = Counter(sorted(s))
        order = list(dictionary.keys())
        res = ""

        while dictionary:
            for letter in order:
                res += letter
                dictionary[letter] -= 1

            for letter, value in list(dictionary.items()):
                if value == 0:
                    del dictionary[letter]
                    order.remove(letter)

            order.reverse()

        return res
        


        # res = ""
        # smallest = ""
        # largest = "}"

        # while s:
        #     temp = s
        #     while temp and smallest < min(temp):
        #         smallest = min(temp)
        #         s = s.replace(smallest, "", 1)
        #         temp = temp.replace(smallest, "")
        #         res += smallest
        #     smallest = ""
        #     temp = s
        #     while temp and largest > max(temp):
        #         largest = max(temp)
        #         s = s.replace(largest, "", 1)
        #         temp = temp.replace(largest, "")
        #         res += largest
        #     largest = "}"

        # return res
                



def main():
    sol = Solution()
    print(sol.sortString("aaaabbbbcccc"))
    print(sol.sortString("rat"))


if __name__ == '__main__':
    main()