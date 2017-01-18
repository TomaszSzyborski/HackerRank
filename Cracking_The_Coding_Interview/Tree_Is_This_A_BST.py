""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root, min_, max_):
    return (root is None or
            (root.data < max_ and root.data > min_
             and check(root.left, min_, root.data)
             and check(root.right, root.data, max_)))

def check_binary_search_tree_(root):
    return check(root, -float('inf'), float('inf'))


##INPUT
#2
#1 2 3 4 5 6 7

##OUTPUT
#Yes