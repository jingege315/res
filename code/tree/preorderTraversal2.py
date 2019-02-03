from TreeNode import TreeNode

# def preorderTraversal(root: TreeNode):
#     stack=[root]
#     while len(stack)>0:
#         tree=stack.pop()
#         if tree is None:
#             continue
#         stack.append(tree.right)
#         stack.append(tree.left)
#         # do something here, e.g. print itself
#         print(tree.val)
def preorderTraversal(root: TreeNode):
    stack=[(root,False)]
    while len(stack)>0:
        tree,extend=stack.pop()
        if tree is None:
            continue
        if not extend:
            stack.append((tree.right,False))
            stack.append((tree.left,False))
            stack.append((tree,True))
        else:
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
    preorderTraversal(root)
