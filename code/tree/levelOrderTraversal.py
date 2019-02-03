from TreeNode import TreeNode

def levelOrderTraversal(root: TreeNode):
    stack=[root]
    while len(stack)>0:
        tree=stack.pop(0)
        if tree is None:
            continue
        stack.append(tree.left)
        stack.append(tree.right)
        # do something here, e.g. print itself
        print(tree.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    levelOrderTraversal(root)
