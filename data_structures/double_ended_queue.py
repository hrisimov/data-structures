class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        self.__insert_node_between_nodes(
            ListNode(value),
            self.right.prev,
            self.right,
        )

    def appendleft(self, value: int) -> None:
        self.__insert_node_between_nodes(
            ListNode(value),
            self.left,
            self.left.next,
        )

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        node_to_remove = self.right.prev
        self.__remove_node_between_nodes(node_to_remove)
        return node_to_remove.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node_to_remove = self.left.next
        self.__remove_node_between_nodes(node_to_remove)
        return node_to_remove.val

    @staticmethod
    def __insert_node_between_nodes(new, prev, next):
        new.next = next
        next.prev = new
        new.prev = prev
        prev.next = new

    @staticmethod
    def __remove_node_between_nodes(node):
        node.prev.next = node.next
        node.next.prev = node.prev
