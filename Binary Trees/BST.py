
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, value):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         if self.value is None:
#             self.value = value
#             return
#         currentNode = self
#         loop = True
#         while loop:
#             if value < currentNode.value:
#                 if currentNode.left is not None:
#                     currentNode = currentNode.left
#                 else:
#                     currentNode.left = BST(value)
#                     loop = False
#             elif value > currentNode.value:
#                 if currentNode.right is not None:
#                     currentNode = currentNode.right
#                 else:
#                     currentNode.right = BST(value)
#                     loop=False
#             else:
#                 print(f"Node already present")
#
#         return self
#
#     def contains(self, value):
#
#         currentNode = self
#
#
#         while True:
#
#             if value < currentNode.value:
#                 if currentNode.left is not None:
#                     currentNode = currentNode.left
#                 else:
#                     return False
#             elif value > currentNode.value:
#                 if currentNode.right is not None:
#                     currentNode = currentNode.right
#                 else:
#                     return False
#             else:
#                 if currentNode.value == value:
#                     return True
#
#
#
#     def remove(self, value,parentNode = None):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#
#         currentNode = self
#
#         while currentNode is not None:
#
#             if value < currentNode.value:
#                parentNode = currentNode
#                currentNode = currentNode.left
#             elif value > currentNode.value:
#                 parentNode = currentNode
#                 currentNode = currentNode.right
#             else:
#                 # case 1: Node to be removed has left and right children
#                 if currentNode.left is not None and currentNode.right is not None:
#                     right_lowest_value = currentNode.right.getMinValue()
#                     currentNode.value = right_lowest_value
#                     currentNode.right.remove(right_lowest_value,currentNode)
#                 # case2 : Node to be removed has no parent node
#                 elif parentNode is None:
#                     if currentNode.left:
#                         currentNode.value = currentNode.left.value
#                         currentNode.right = currentNode.left.right
#                         currentNode.left = currentNode.left.left
#
#                     elif currentNode.right:
#                         currentNode.value = currentNode.right.value
#                         currentNode.left = currentNode.right.left
#                         currentNode.right = currentNode.right.right
#                     else:
#                         pass
#                 elif parentNode.left == currentNode:
#                     parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
#                 elif parentNode.right == currentNode:
#                     parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
#                 break
#         return self
#
#     def getMinValue(self):
#         currentNode = self
#         while currentNode.left is not None:
#             currentNode = currentNode.left
#
#         return currentNode.value
#         #
#         #     10
#         #    /  \
#         #   6   15
#         #  /    /  \
#         # 5    14   17
#
# class InorderIterator:
#   def __init__(self, root):
#     self.fringe = []
#     self.fringe.append((root,False))
#     return
#
#   def hasNext(self):
#     if len(self.fringe) > 0:
#       return True
#     else:
#       return False
#   # getNext returns null if there are no more elements in tree
#   def getNext(self):
#     node,traversed = self.fringe.pop()
#     if node:
#       if traversed:
#         return node
#       else:
#         self.fringe.append((node.right,False))
#         self.fringe.append((node,True))
#         self.fringe.append((node.left,False))
#     return None
#
# def inorder_using_iterator(root):
#   iter = InorderIterator(root)
#   result = ""
#   while iter.hasNext():
#     ptr = iter.getNext()
#     if ptr is not None:
#       result += str(ptr.value) + " "
#   return result
#
#
# # arr = [25,125,200,300,75,50,12,35,60,75]
# # root = create_BST(arr)
#
#
# bst = BST(25)
# bst.insert(125)
# bst.insert(200)
# bst.insert(350)
# bst.insert(50)
#
# bst.insert(75)
# bst.insert(100)
#
# print("Inorder Iterator = ", end = "")
# print(inorder_using_iterator(bst))
#
#
# def find_min(node):
#     while node.left is not None:
#         node = node.left
#     return node
#
#
# def inorder_successor_bst(root, d):
#     successor = None
#     while root is not None:
#         if d < root.value:
#             successor = root
#             root = root.left
#         elif d > root.value:
#             root = root.right
#         else:
#             if root.right:
#                 successor = find_min(root.right)
#             break
#
#     return successor
#
#
# arr = [25,125,200,350,50,75,100]
# tree = BST(25)
# for i in range(1,len(arr)):
#     tree.insert(arr[i])
#
# for i in arr:
#     succ = inorder_successor_bst(tree, i)
#     if succ is not None:
#         print(f"successor of {i} is {inorder_successor_bst(tree, i).value}")
#     else:
#         print(f"successor of {i} is None")

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_min(right_node):
    while right_node.left:
        right_node = right_node.left
    return right_node

def findSuccessor(tree, node):
    fringe = []
    fringe.append(tree)
    successor = None
    while len(fringe) > 0:
        item = fringe.pop()
        if item == node:
            successor = item.right
            break
        elif node == item.right:
            if item.right.right is None:
                successor = item.parent
            else:
                successor = find_min(item.right)
            break
        elif node == item.left:
            successor = item
            break
        else:
            if item.right:
                fringe.append(item.right)
            if item.left:
                fringe.append(item.left)
    return successor

def is_bst_rec(root, min_value, max_value):
  if root == None:
    return True

  if root.data < min_value or root.data > max_value:
    return False

  return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
  return is_bst_rec(root,float('-inf'),float('inf'))

root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.parent = root
root.right = BinaryTree(3)
root.right.parent = root
root.left.left = BinaryTree(4)
root.left.left.parent = root.left
root.left.right = BinaryTree(5)
root.left.right.parent = root.left
root.left.right.left = BinaryTree(6)
root.left.right.left.parent = root.left.right
root.left.right.right = BinaryTree(7)
root.left.right.right.parent = root.left.right
root.left.right.right.left = BinaryTree(8)
root.left.right.right.parent = root.left.right.right


node = root.left.right
expected = root.left.right.right.left
if findSuccessor(root, node) == expected:
    print("True")






