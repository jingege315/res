from TreeNode import TreeNode


def inorderTraversal(root: TreeNode):
    if root is None:
        return
    inorderTraversal(root.left)
    # do something here, e.g. print itself
    print(root.val)
    inorderTraversal(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    inorderTraversal(root)
