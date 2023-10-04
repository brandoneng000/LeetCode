from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = {}

        for n in names:
            if n not in res:
                res[n] = ""
            else:
                dupe = 1
                new_name = f"{n}({dupe})"

                while new_name in res:
                    dupe += 1
                    new_name = f"{n}({dupe})"
                
                res[new_name] = ""

        return res.keys()
        

def main():
    sol = Solution()
    print(sol.getFolderNames(["pes","fifa","gta","pes(2019)"]))
    print(sol.getFolderNames(["gta","gta(1)","gta","avalon"]))
    print(sol.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
    print(sol.getFolderNames(["onepiece","onepiece","onepiece(1)","onepiece(2)","onepiece(3)"]))

if __name__ == '__main__':
    main()