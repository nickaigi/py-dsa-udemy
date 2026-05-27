import ctypes


class DynamicArray(object):
    def __init__(self) -> None:
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, k: int):
        if not 0 <= k < self.n:
            return IndexError("K is out of bounds!")

        return self.A[k]

    def append(self, ele: int):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if capacity isn't enough
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap: int):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap: int):
        return (new_cap * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(100):
        arr.append(i)
        print(f"Len = {len(arr)} -> Current capacity {arr.capacity}")
