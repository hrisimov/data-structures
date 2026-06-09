class ListNode:

    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = capacity * [None]
        self.size = 0

    # Time Complexity: O(1)
    def insert(self, key: int, value: int) -> None:
        index = self.__hash(key)
        node = self.__get_node(self.map[index], key)

        if node:
            node.val = value
            return

        self.map[index] = ListNode(key, value, self.map[index])
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    # Time Complexity: O(1)
    def get(self, key: int) -> int:
        index = self.__hash(key)
        node = self.__get_node(self.map[index], key)

        if not node:
            return -1

        return node.val

    # Time Complexity: O(1)
    def remove(self, key: int) -> bool:
        index = self.__hash(key)
        previous = None
        current = self.map[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.map[index] = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_map = self.map
        self.capacity *= 2
        self.map = self.capacity * [None]

        for node in old_map:
            while node:
                index = self.__hash(node.key)
                self.map[index] = ListNode(node.key, node.val, self.map[index])
                node = node.next

    def __hash(self, key: int) -> int:
        return key % self.capacity

    @staticmethod
    def __get_node(head: ListNode | None, key: int) -> ListNode | None:
        current = head

        while current:
            if current.key == key:
                break
            current = current.next

        return current
