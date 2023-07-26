import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.time = { i: [0] for i in range(length) }
        self.snapshots = { (i, 0): 0 for i in range(length) }
        self.snapshot_id = 0
        

    def set(self, index: int, val: int) -> None:
        if self.time[index][-1] != self.snapshot_id:
            self.time[index].append(self.snapshot_id)
        self.snapshots[index, self.snapshot_id] = val

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if (index, snap_id) in self.snapshots:
            return self.snapshots[index, snap_id]

        last_time = bisect.bisect(self.time[index], snap_id)

        return self.snapshots[index, self.time[index][last_time - 1]]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)