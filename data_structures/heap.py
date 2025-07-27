from typing import List


class MinHeap:

    def __init__(self):
        self.heap = [0]

    # Time Complexity: O(log(n))
    def push(self, val: int) -> None:
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    # Time Complexity: O(log(n))
    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.__percolate_down(1)
        return root

    # Time Complexity: O(1)
    def top(self) -> int:
        if len(self.heap) == 1:
            return -1

        return self.heap[1]

    # Time Complexity: O(n)
    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        self.heap.append(self.heap[0] if self.heap else 0)

        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self.__percolate_down(i)

    def __percolate_up(self, index):
        c = index
        p = c // 2

        while c > 1 and self.heap[c] < self.heap[p]:
            self.heap[c], self.heap[p] = self.heap[p], self.heap[c]
            c = p
            p = c // 2

    def __percolate_down(self, index):
        c = index
        l = 2 * c
        r = 2 * c + 1
        heap_len = len(self.heap)

        while l < heap_len:
            if r < heap_len and self.heap[l] >= self.heap[r] < self.heap[c]:
                # Swap with right child
                self.heap[c], self.heap[r] = self.heap[r], self.heap[c]
                c = r
            elif self.heap[l] < self.heap[c]:
                # Swap with left child
                self.heap[c], self.heap[l] = self.heap[l], self.heap[c]
                c = l
            else:
                break
            l = 2 * c
            r = 2 * c + 1
