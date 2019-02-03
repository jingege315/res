from TreeNode import TreeNode


def postorderTraversal(root: TreeNode):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    # do something here, e.g. print itself
    print(root.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    postorderTraversal(root)
