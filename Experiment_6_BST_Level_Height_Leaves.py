from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                print(f"Duplicate value {data} ignored.")
                return

    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])
        level = 0
        while queue:
            count = len(queue)
            values = []
            for _ in range(count):
                node = queue.popleft()
                values.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(f"Level {level}: {' '.join(map(str, values))}")
            level += 1

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def leaf_nodes(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.data]
        return self.leaf_nodes(node.left) + self.leaf_nodes(node.right)


def main():
    original_tree = BinarySearchTree()
    new_tree = BinarySearchTree()

    n = int(input("Enter number of nodes: "))
    if n < 0:
        print("Number of nodes cannot be negative.")
        return

    values = []
    for i in range(n):
        value = int(input(f"Enter value {i + 1}: "))
        values.append(value)
        original_tree.insert(value)

    for value in values:
        new_tree.insert(value)

    print("\nOriginal BST - Level-wise:")
    original_tree.level_order()
    print("\nNew BST - Level-wise:")
    new_tree.level_order()
    print("\nHeight of Original BST (in edges):",
          original_tree.height(original_tree.root))
    print("Leaf Nodes of Original BST:", *original_tree.leaf_nodes(original_tree.root))


if __name__ == "__main__":
    main()
