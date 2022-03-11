class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        long_press = 0
        name_counter = 0
        prev = name[0]
        name += "A"

        for letter in name:
            if letter == prev:
                name_counter += 1
            else:
                counter = 0
                while long_press < len(typed) and typed[long_press] == prev:
                    counter += 1
                    long_press += 1
                if name_counter > counter:
                    return False
                name_counter = 1
                prev = letter

        return long_press == len(typed)
        
def main():
    sol = Solution()
    print(sol.isLongPressedName("alex", "aaleexa"))
    print(sol.isLongPressedName("alex", "aaleex"))
    print(sol.isLongPressedName("saeed", "ssaaeedd"))
    print(sol.isLongPressedName("saeed", "ssaaedd"))
    print(sol.isLongPressedName("a", "b"))

if __name__ == '__main__':
    main()