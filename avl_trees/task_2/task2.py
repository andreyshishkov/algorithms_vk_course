class Node:

    def __init__(self, key: int):
        self.key = key
        self.height = 1
        self.number = 1

        self.left = self.right = None


class AvlTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(root: Node) -> int:
        if not root:
            return 0
        return root.height

    def get_balance(self, root: Node) -> int:
        return self.get_height(root.right) - self.get_height(root.left)

    def fix_height(self, root: Node) -> None:
        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)
        root.height = 1 + max(h_left, h_right)

    @staticmethod
    def fix_number(root: Node) -> None:
        left_num = root.left.number if root.left else 0
        right_num = root.right.number if root.right else 0
        root.number = left_num + right_num + 1

    def right_rotate(self, z: Node) -> Node:
        y = z.left
        tmp = y.right

        y.right = z
        z.left = tmp

        self.fix_height(z)
        self.fix_height(y)

        self.fix_number(z)
        self.fix_number(y)

        return y

    def left_rotate(self, z: Node):
        y = z.right
        tmp = y.left

        y.left = z
        z.right = tmp

        self.fix_height(z)
        self.fix_height(y)

        self.fix_number(z)
        self.fix_number(y)

        return y

    def make_balance(self, root: Node) -> Node:
        self.fix_height(root)
        if self.get_balance(root) == 2:
            if self.get_balance(root.right) < 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        if self.get_balance(root) == -2:
            if self.get_balance(root.left) > 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        return root

    def insert(self, root: Node, key: int, ) -> Node:
        global position
        if not root:
            return Node(key)

        root.number += 1
        if key < root.key:
            position += 1 + (root.right.number if root.right else 0)
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return self.make_balance(root)

    def find_min(self, root: Node) -> Node:
        if not root.left:
            return root
        return self.find_min(root.left)

    def remove_min(self, root: Node) -> Node:
        if not root.left:
            return root.right
        root.left = self.remove_min(root.left)
        root.number -= 1
        return self.make_balance(root)

    def remove(self, root: Node, pos: int):
        if root is None:
            return None
        if pos >= root.number:
            return root
        acc = 0
        nodes = []
        while True:
            right_num = root.right.number if root.right else 0

            if pos - acc > right_num:
                nodes.append(root)
                root = root.left
                acc += right_num + 1
            elif pos - acc < right_num:
                if root.right is not None:
                    nodes.append(root)
                    root = root.right
                else:
                    break

            else:
                left = root.left
                right = root.right
                key = root.key
                #  del root

                if right is None:
                    if left is None:
                        if len(nodes):
                            root = nodes.pop()
                            if root.key > key:
                                root.left = None
                            else:
                                root.right = None
                            root.number -= 1
                        else:
                            return None

                    else:
                        root = left

                else:
                    min_node = self.find_min(right)
                    min_node.right = self.remove_min(right)
                    min_node.left = left
                    self.fix_number(min_node)
                    root = self.make_balance(min_node)

                break

        while len(nodes):
            p1 = nodes.pop()
            p1.number -= 1
            if p1.key > root.key:
                p1.left = root
            else:
                p1.right = root
            root = self.make_balance(p1)
        return root

    def delete(self, node: Node) -> None:
        if not node:
            return
        self.delete(node.left)
        self.delete(node.right)
        del node


def main():
    n = int(input())
    tree = AvlTree()
    result = []

    global position
    for _ in range(n):
        command, value = (int(x) for x in input().split())

        if command == 1:
            position = 0
            tree.root = tree.insert(tree.root, value)
            result.append(position)
        else:
            tree.root = tree.remove(tree.root, value)

    print(*result)


if __name__ == '__main__':
    position = 0
    main()
