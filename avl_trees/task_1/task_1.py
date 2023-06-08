from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height  = 1


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, root: Node, key: int) -> Node:
        if not root:
            return Node(key)

        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, z: Node) -> Node:
        y = z.right
        tmp = y.left

        y.left = z
        z.right = tmp

        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )
        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    def right_rotate(self, z: Node) -> Node:
        y = z.left
        tmp = y.right

        y.right = z
        z.left = tmp

        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )
        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        return y

    @staticmethod
    def get_height(root: Node) -> int:
        if not root:
            return 0
        return root.height

    def get_balance(self, root: Node) -> int:
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def delete_node(self, root: Node, key: int) -> Union[Node, None]:
        if not root:
            return root

        elif key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp

            elif root.right is None:
                tmp = root.left
                root = None
                return tmp

            tmp = self.get_min_value_node(root.right)
            root.value = tmp.value
            root.right = self.delete_node(root.right, tmp.value)

        if root is None:
            return root

        root.height = 1 + max(
            self.get_height(root.right),
            self.get_height(root.left)
        )

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def get_min_value_node(self, root: Node):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)


def main():
    tree = AVLTree()
    numbers = [int(x) for x in input().split()]
    for number in numbers:
        if number >= 0:
            tree.root = tree.insert(tree.root, number)
        else:
            tree.root = tree.delete_node(tree.root, -number)

    print(tree.get_height(tree.root))


if __name__ == '__main__':
    main()
