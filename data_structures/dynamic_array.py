class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0

    # Assume that index i is valid.
    def get(self, i: int) -> int:
        return self.arr[i]

    # Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    # Assume that the array is non-empty.
    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
