class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


    def heightBalancedBinaryTree(self,tree):
        # Write your code here.
	    def isHeightBalanced(tree):
		    if tree is None:
			    return 0
		    left = isHeightBalanced(tree.left)
		    right = isHeightBalanced(tree.right)
		    if left == -1 or right == -1:
			    return -1
		    if abs(left-right) > 1:
			    return -1
		    return max(left,right)+1
	    return isHeightBalanced(tree) != -1

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.left.right.left = Node(7)
tree.root.left.right.right = Node(8)
tree.root.left.right.right.left = Node(9)

print(tree.heightBalancedBinaryTree(tree.root))




    