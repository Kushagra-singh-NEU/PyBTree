class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


import collections

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if not current_node.right:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def find(self, data):
        if not self.root:
            return False
        else:
            return self._find(data, self.root)

    def _find(self, data, current_node):
        if not current_node:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._find(data, current_node.left)
        else:
            return self._find(data, current_node.right)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, current_node, data):
        if not current_node:
            return current_node
        if data < current_node.data:
            current_node.left = self._delete(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._delete(current_node.right, data)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                min_node = self._find_min(current_node.right)
                current_node.data = min_node.data
                current_node.right = self._delete(current_node.right, min_node.data)
        return current_node

    @staticmethod
    def _find_min(current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def preorder_traversal(self, callback):
        self._preorder_traversal(self.root, callback)

    def _preorder_traversal(self, current_node, callback):
        if current_node:
            callback(current_node.data)
            self._preorder_traversal(current_node.left, callback)
            self._preorder_traversal(current_node.right, callback)

    def level_order_traversal(self):
        result = []
        if not self.root:
            return result
        queue = collections.deque([self.root])
        while queue:
            level_result = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_result)
        return result

    def max_depth(self):
        return self._max_depth(self.root)

    def _max_depth(self, node):
        if not node:
            return 0
        else:
            left_height = self._max_depth(node.left)
            right_height = self._max_depth(node.right)
            return max(left_height, right_height) + 1

    def max_path_sum(self):
        if not self.root:
            return 0
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            max_sum = max(max_sum, left + right + node.data)
            return max(left, right) + node.data

        dfs(self.root)
        return max_sum




# Create an instance of BinaryTree
tree = BinaryTree()

# Insert elements into the binary tree
tree.insert(10)
tree.insert(5)
tree.insert(16)
tree.insert(4)
tree.insert(7)
tree.insert(12)
tree.insert(17)
tree.insert(1)
tree.insert(6)
tree.insert(9)
tree.insert(11)
tree.insert(14)
tree.insert(18)

# Test find operation
print(tree.find(11))  # Output: True
print(tree.find(3))   # Output: False

# Perform a preorder traversal and print node data
print("Preorder Traversal:")
tree.preorder_traversal(lambda x: print(x))

# Calculate and print the maximum depth of the tree
print("Maximum Depth:")
print(tree.max_depth())  # Output: 4

# Perform a level order traversal and print the tree level by level
print("Level Order Traversal:")
print(tree.level_order_traversal())
# Output: [[10], [5, 16], [4, 7, 12, 17], [1, 6, 9, 11, 14, 18]]

# Calculate and print the maximum path sum in the tree
print("Maximum Path Sum:")
print(tree.max_path_sum())  # Output: 71
