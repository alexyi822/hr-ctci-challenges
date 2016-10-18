""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys

def check_binary_search_tree_(root):
    return check_bst(root, -sys.maxint - 1, sys.maxint)

def check_bst(root, min, max):
    if root is None:
        return True
    if root.data < min or root.data > max:
        return False
    return check_bst(root.left, min, root.data - 1) and check_bst(root.right, root.data + 1, max)
