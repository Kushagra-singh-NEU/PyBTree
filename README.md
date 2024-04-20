# PyBTree

PyBTree is a Python library that implements a binary tree data structure with various operations for insertion, deletion, searching, and traversal.

## Overview

A binary tree is a hierarchical data structure where each node has at most two children: left and right. The PyBTree library includes two main classes:

- **Node**: Represents a node in the binary tree.
  
- **BinaryTree**: Manages the binary tree structure and provides methods to manipulate and traverse the tree.

## Classes and Methods

### Node Class

The `Node` class represents a single node in the binary tree.

Attributes:
- `left`: Reference to the left child node (another `Node` instance).
- `right`: Reference to the right child node (another `Node` instance).
- `data`: Value stored in the node.

### BinaryTree Class

The `BinaryTree` class manages the binary tree structure.

Attributes:
- `root`: Reference to the root node of the binary tree.

Methods:
- `insert(data)`: Inserts a new node with the given data into the binary tree.
- `find(data)`: Searches for a node with the given data and returns `True` if found, otherwise `False`.
- `delete(data)`: Deletes a node with the given data from the binary tree.
- `preorder_traversal(callback)`: Performs a preorder traversal of the tree and applies a callback function to each node's data.
- `inorder_traversal(callback)`: Performs an inorder traversal of the tree and applies a callback function to each node's data.
- `postorder_traversal(callback)`: Performs a postorder traversal of the tree and applies a callback function to each node's data.
- `max_depth()`: Returns the maximum depth (height) of the binary tree.
- `level_order_traversal()`: Performs a level-order traversal of the tree and returns a list of lists representing each level.
- `max_path_sum()`: Computes the maximum path sum in the binary tree.

## Usage Example

```python
from binarytree import BinaryTree

# Create a binary tree instance
tree = BinaryTree()

# Insert elements into the binary tree
tree.insert(10)
tree.insert(5)
tree.insert(16)

# Search for a value in the tree
print(tree.find(5))  # Output: True

# Perform a preorder traversal and print node data
print("Preorder Traversal:")
tree.preorder_traversal(lambda x: print(x))

# Calculate the maximum depth of the tree
print("Maximum Depth:")
print(tree.max_depth())  # Output: 2

# Perform a level order traversal and print the tree level by level
print("Level Order Traversal:")
print(tree.level_order_traversal())
# Output: [[10], [5, 16]]
