class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder_recursion":
            return self.preorder_print_recursion(tree.root, "")
        elif traversal_type == "preorder_stack":
            return self.preorder_print_stack(tree.root)
        elif traversal_type == "inorder_stack":
            return self.inorder_print_stack(tree.root)
        elif traversal_type == "inorder_recursion":
            return self.inorder_print_recursion(tree.root, "")
        elif traversal_type == "postorder_recursion":
            return self.postorder_print_recursion(tree.root, "")
        elif traversal_type == "postorder_stack":
            return self.postorder_print_stack(tree.root)
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print_recursion(self, start, traversal):

        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print_recursion(start.left, traversal)
            traversal = self.preorder_print_recursion(start.right, traversal)
        return traversal

    def preorder_print_stack(self, start):
        fringe = []
        fringe.append(start)
        traversal = ""
        while len(fringe) > 0:
            x = fringe.pop()
            traversal += (str(x.value) + "-")
            if x.right:
                fringe.append(x.right)
            if x.left:
                fringe.append(x.left)
        return traversal

    def inorder_print_recursion(self, start, traversal):
        if start:
            traversal = self.inorder_print_recursion(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print_recursion(start.right, traversal)
        return traversal

    def inorder_print_stack(self, start):
        fringe = []
        fringe.append(start)
        traversal = ""
        while len(fringe) > 0:
            if fringe[-1].left:
                fringe.append(fringe[-1].left)
            elif fringe[-1].right:
                fringe.append(fringe[-1].right)
            else:
                x = fringe.pop()
                if len(fringe) > 0:
                    traversal += (str(x.value) + "-")
                    if fringe[-1].right:
                        x = fringe.pop()
                        traversal += (str(x.value) + "-")
                        fringe.append(x.right)

        return traversal

    def postorder_print_recursion(self, start, traversal):
        if start:
            traversal = self.postorder_print_recursion(start.left, traversal)
            traversal = self.postorder_print_recursion(start.right, traversal)
            traversal += (str(start.value) + "-")

        return traversal

    def postorder_print_stack(self, start):
        fringe = []
        visited = {}
        fringe.append(start)
        traversal = ""
        while len(fringe) > 0:
            if fringe[-1].right and fringe[-1] not in visited:
                fringe.append(fringe[-1].right)
                visited[fringe[-1]] = "True"
                if fringe[-2].left:
                    fringe.append(fringe[-2].left)
                    visited[fringe[-2]] = "True"
            elif fringe[-1].left and fringe[-1] not in visited:
                fringe.append(fringe[-1].left)
                visited[fringe[-1]] = "True"

            else:
                traversal += (str(fringe[-1].value) + "-")
                fringe.pop()

        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += (str(queue.peek()) + "-")
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     8   9
#            / \
#           6   7


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)
tree.root.left.right.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(f'Pre-order using recursion is : {tree.print_tree("preorder_recursion")}')
print(f'Pre-order using stack is     : {tree.print_tree("preorder_stack")}')
print(f'In-order using recursion is  : {tree.print_tree("inorder_recursion")}')
print(f'In-order using stack is      : {tree.print_tree("inorder_stack")}')
print(f'Post-order using recursion is: {tree.print_tree("postorder_recursion")}')
print(f'Post-order using stack is: {tree.print_tree("postorder_stack")}')
print(f'Post-order using queue is    : {tree.print_tree("levelorder")}')