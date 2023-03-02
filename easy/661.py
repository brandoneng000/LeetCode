from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        
        for row in range(len(img)):
            vals = []

            for col in range(len(img[0])):
                total = 0
                count = 0
                for row_adj in range(-1, 2):
                    if row == 0 and row_adj == -1:
                        continue
                    if row == len(img) - 1 and row_adj == 1:
                        continue
                    if row == 1:
                        pass
                    for col_adj in range(-1, 2):
                        if col == 0 and col_adj == -1:
                            continue
                        if col == len(img[0]) - 1 and col_adj == 1:
                            continue
                        total += img[row + row_adj][col + col_adj]
                        count += 1
                
                vals.append(total // count)      
            res.append(vals)
                
        return res

def main():
    sol = Solution()
    # print(sol.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))

if __name__ == '__main__':
    main()