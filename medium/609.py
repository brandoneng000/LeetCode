from typing import List
import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data = collections.defaultdict(list)
        for directory in paths:
            dir_name, *dir_files = directory.split()
            for file in dir_files:
                file_name, content = file.split('(')
                content = content.rstrip(')')
                data[content].append(f"{dir_name}/{file_name}")
        
        return [data[key] for key in data if len(data[key]) > 1]

def main():
    sol = Solution()
    print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
    print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))

if __name__ == '__main__':
    main()