from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node(key: {self.key}, val: {self.val})'


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.__insert(self.root, key, val)

    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def __insert(self, root, key, val):
        if not root:
            return TreeNode(key, val)

        if key > root.key:
            root.right = self.__insert(root.right, key, val)
        elif key < root.key:
            root.left = self.__insert(root.left, key, val)
        else:
            root.val = val

        return root

    def get(self, key: int) -> int:
        return self.__get(self.root, key)

    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def __get(self, root, key):
        if not root:
            return -1

        if key > root.key:
            return self.__get(root.right, key)
        elif key < root.key:
            return self.__get(root.left, key)
        else:
            return root.val

    def getMin(self) -> int:
        if not self.root:
            return -1

        return self.__get_min_node(self.root).val

    # Time Complexity: O(h)
    # Space Complexity: O(1)
    def getMax(self) -> int:
        if not self.root:
            return -1

        current = self.root

        while current.right:
            current = current.right

        return current.val

    def remove(self, key: int) -> None:
        self.root = self.__remove(self.root, key)

    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def __remove(self, root, key):
        if not root:
            return None

        if key > root.key:
            root.right = self.__remove(root.right, key)
        elif key < root.key:
            root.left = self.__remove(root.left, key)
        else:
            if root.left and root.right:
                min_node = self.__get_min_node(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.__remove(root.right, min_node.key)
            else:
                return root.left or root.right

        return root

    def getInorderKeys(self) -> List[int]:
        keys = []
        self.__get_inorder_keys(self.root, keys)
        return keys

    # Time Complexity: O(n)
    # Space Complexity:
    #   - O(h) space for the recursion stack
    #   - O(n) space for the output array
    def __get_inorder_keys(self, root, keys):
        if not root:
            return

        self.__get_inorder_keys(root.left, keys)
        keys.append(root.key)
        self.__get_inorder_keys(root.right, keys)

    # Time Complexity: O(h)
    # Space Complexity: O(1)
    @staticmethod
    def __get_min_node(root):
        current = root

        while current.left:
            current = current.left

        return current
