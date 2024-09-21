from typing import List


class ListNode:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    # Assume that index is greater than or equal to 0.
    def get(self, index: int) -> int:
        current_node = self.head.next
        i = 0

        while current_node:
            if i == index:
                return current_node.val
            current_node = current_node.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if self.head == self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        # self.tail = self.tail.next

    # Assume that index is greater than or equal to 0.
    def remove(self, index: int) -> bool:
        current_node = self.head
        i = 0

        while current_node:
            if i == index:
                break
            current_node = current_node.next
            i += 1

        if current_node and current_node.next:
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        result = []
        current_node = self.head.next

        while current_node:
            result.append(current_node.val)
            current_node = current_node.next

        return result
