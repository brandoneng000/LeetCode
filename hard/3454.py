from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[node] += val
            else:
                middle = (l + r) // 2
                update(node * 2, l, middle, ql, qr, val)
                update(node * 2 + 1, middle, r, ql, qr, val)
            
            if count[node] > 0:
                seg[node] = xs[r] - xs[l]
            elif r - l == 1:
                seg[node] = 0
            else:
                seg[node] = seg[node * 2] + seg[node * 2 + 1]

        xs = []
        events = []

        for x, y, l in squares:
            xs += [x, x + l]
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        xs = sorted(set(xs))
        events.sort()

        index = { v: i for i, v in enumerate(xs) }
        n = len(xs)

        count = [0] * (4 * n)
        seg = [0.0] * (4 * n)

        total, prev_y = 0, events[0][0]
        strips = []

        for y, t, x1, x2 in events:
            if y > prev_y:
                h = y - prev_y
                w = seg[1]
                total += w * h
                strips.append((prev_y, h, w))
                prev_y = y
            update(1, 0, n - 1, index[x1], index[x2], t)

        half, acc = total / 2, 0

        for y, h, w in strips:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w
        
        return 0


        
def main():
    sol = Solution()
    print(sol.separateSquares([[0,0,1],[2,2,1]]))
    print(sol.separateSquares([[0,0,2],[1,1,1]]))

if __name__ == '__main__':
    main()