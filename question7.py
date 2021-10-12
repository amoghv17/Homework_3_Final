class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def hasPathSum(node, sum):
    answer = 0
    subsum = sum - node.data


    if (subsum == 0 and node.left == None and node.right == None):
        return True


    if node.left is not None:
        answer = answer or hasPathSum(node.left, subsum)
    if node.right is not None:
        answer = answer or hasPathSum(node.right, subsum)

    return answer





sum = 25
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.left.right = Node(1)
root.right.right = Node(4)

if hasPathSum(root, sum):
    print("There is a root-to-leaf path with sum %d" % (sum))
else:
    print("There is no root-to-leaf path with sum %d" % (sum))