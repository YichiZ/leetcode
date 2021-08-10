
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preorder_print_msg(self, node: Node, msg):
        if node:
            msg += str(node.value) + "-"
            msg = self.preorder_print_msg(node.left, msg)
            msg = self.preorder_print_msg(node.right, msg)
        return msg

    def preorder(self, node: Node):
        res = []
        if node:
            res.append(node.value)
            res += self.preorder(node.left)
            res += self.preorder(node.right)
        return res

    def insert(self, parent_node: Node, new_value: int) -> None:
        # if data exist
        # smaller
        # larger
        if new_value:
            if new_value < parent_node.value:
                if parent_node.left:
                    self.insert(parent_node.left, new_value)
                else:
                    parent_node.left = Node(new_value)
                    return
            else:
                if parent_node.right:
                    self.insert(parent_node.right, new_value)
                else:
                    parent_node.right = Node(new_value)
                    return

    def get(self, parent, value):
        pass

    def remove(self, parent, value):
        pass
        # insertion
        # removal
        # swap


if __name__ == "__main__":
    root = Node(1)
    tree = BinaryTree(root)

    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.insert(tree.root, 4)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)

    print(tree.preorder(tree.root))
