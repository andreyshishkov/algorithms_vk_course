from typing import Tuple, Any


# =================================== Naive Tree =========================================
class NaiveNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NaiveTree:

    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if node is None:
            return NaiveNode(value)
        elif node.value <= value:
            node.right = self.insert(node.right, value)
        elif node.value > value:
            node.left = self.insert(node.left, value)
        return node

    def get_depth(self, node):
        left_depth = self.get_depth(node.left) if node.left else 0
        right_depth = self.get_depth(node.right) if node.right else 0

        return max(left_depth, right_depth) + 1


# ============================= Decart Tree ============================================================
class TreapNode:

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority

        self.left = None
        self.right = None


class TreapTree:

    def __init__(self):
        self.root = None

    def insert(self, root: TreapNode, key: int, priority: int) -> TreapNode:
        if not root:
            return TreapNode(key, priority)

        if key <= root.key:
            root.left = self.insert(root.left, key, priority)

            if root.left.priority > root.priority:
                root = self.right_rotate(root)

        else:
            root.right = self.insert(root.right, key, priority)

            if root.right.priority > root.priority:
                root = self.left_rotate(root)

        return root

    @staticmethod
    def right_rotate(y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        return x

    @staticmethod
    def left_rotate(x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        return y

    def get_depth(self, node):
        left_depth = self.get_depth(node.left) if node.left else 0
        right_depth = self.get_depth(node.right) if node.right else 0

        return max(left_depth, right_depth) + 1


# =========== main function ====================================
def main():
    n = int(input())
    treap = TreapTree()
    naive = NaiveTree()

    for _ in range(n):
        key, priority = [int(x) for x in input().split()]

        naive.root = naive.insert(naive.root, key)

        treap.root = treap.insert(treap.root, key, priority)

    naive_depth = naive.get_depth(naive.root)
    treap_depth = treap.get_depth(treap.root)

    print(abs(naive_depth - treap_depth))


if __name__ == '__main__':
    main()
