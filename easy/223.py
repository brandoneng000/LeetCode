class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # def get_area(bottom_left_x, bottom_left_y, top_right_x, top_right_y) -> int:
        #     height = max(bottom_left_y, top_right_y) - min(bottom_left_y, top_right_y)
        #     width = max(bottom_left_x, top_right_x) - min(bottom_left_x, top_right_x)
        #     return height * width
        
        # bottom_left_x = max(ax1, bx1)
        # bottom_left_y = max(ay1, by1)
        # top_right_x = min(ax2, bx2)
        # top_right_y = min(ay2, by2)
        # overlap = 0
        # if bx1 in range(ax1, ax2 + 1) or bx2 in range(ax1, ax2 + 1) or ax1 in range(bx1, bx2 + 1) or ax2 in range(bx1, bx2 + 1):
        #     if by1 in range(ay1, ay2 + 1) or by2 in range(ay1, ay2 + 1) or ay1 in range(by1, by2 + 1) or ay2 in range(by1, by2 + 1):
        #         overlap = get_area(bottom_left_x, bottom_left_y, top_right_x, top_right_y)

        # return get_area(ax1, ay1, ax2, ay2) + get_area(bx1, by1, bx2, by2) - overlap
        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)
        bottom_left_x = max(ax1, bx1)
        top_right_x = min(ax2, bx2)
        overlap_width = top_right_x - bottom_left_x
        bottom_left_y = max(ay1, by1)
        top_right_y = min(ay2, by2)
        overlap_height = top_right_y - bottom_left_y
        overlap = 0
        if overlap_height > 0 and overlap_width > 0:
            overlap = overlap_width * overlap_height
        
        return area_a + area_b - overlap
        
            

def main():
    sol = Solution()
    print(sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))
    print(sol.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2))
    print(sol.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
    print(sol.computeArea(-2, -2, 2, 2, -3, -3, 3, -1))

if __name__ == '__main__':
    main()