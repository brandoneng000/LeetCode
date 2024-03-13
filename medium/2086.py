class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if "HHH" in hamsters or hamsters == "H" or hamsters.startswith("HH") or hamsters.endswith("HH"):
            return -1
        
        hamsters = hamsters.replace("H.H", "H")

        return hamsters.count("H")
        
def main():
    sol = Solution()
    print(sol.minimumBuckets(hamsters = "H..H"))
    print(sol.minimumBuckets(hamsters = ".H.H."))
    print(sol.minimumBuckets(hamsters = ".HHH."))

if __name__ == '__main__':
    main()