from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 1000000007
        valid = dict()

        for mask in range(3 ** m):
            color = []
            mm = mask

            for i in range(m):
                color.append(mm % 3)
                mm //= 3

            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        adj = defaultdict(list)

        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adj[mask1].append(mask2)
        
        f = [int(mask in valid) for mask in range(3 ** m)]

        for i in range(1, n):
            g = [0] * (3 ** m)

            for mask2 in valid.keys():
                for mask1 in adj[mask2]:
                    g[mask2] += f[mask1]

                    if g[mask2] >= mod:
                        g[mask2] -= mod
            
            f = g
        
        return sum(f) % mod


def main():
    sol = Solution()
    print(sol.colorTheGrid(m = 1, n = 1))
    print(sol.colorTheGrid(m = 1, n = 2))
    print(sol.colorTheGrid(m = 5, n = 5))

if __name__ == '__main__':
    main()