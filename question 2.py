class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
    if (root is None):
        return 0
    leftdepth = solution(root.left)
    print(" Left depth:", leftdepth)
    rightdepth = solution(root.right)
    print(" Right Depth:", rightdepth)

    if (leftdepth > rightdepth):
        depth= 1 + leftdepth
        print("Depth:", depth)
    else:
        depth= 1 + rightdepth
        print("Depth:", depth)
    return depth

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
print(solution(a3))