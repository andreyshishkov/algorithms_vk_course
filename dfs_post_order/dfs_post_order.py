class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if node is None:
            return Node(value)
        elif node.value <= value:
            node.right = self.insert(node.right, value)
        elif node.value > value:
            node.left = self.insert(node.left, value)
        return node
            

def dfs(node):
    if node is not None:
        dfs(node.left)
        dfs(node.right)
        print(node.value, end=' ')


def main():
    n = int(input())
    values = [int(x) for x in input().split()]
    tree = BinaryTree()
    for value in values:
        tree.root = tree.insert(tree.root, value)

    dfs(tree.root)


if __name__ == '__main__':
    main()
