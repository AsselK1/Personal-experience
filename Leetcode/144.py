# Recursive
class Solution_Recur(object):
    def preorderTraversal(self, root):
        pre = []

        def recursive(node):
            if node:
                pre.append(node.val)
                recursive(node.left)
                recursive(node.right)

        recursive(root)
        return pre


# Iterative
class Solution_Iter(object):
    def preorderTraversal(self, root):

