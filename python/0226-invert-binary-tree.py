# recursive dfs
class Solution(object):
    def invertTree(self, root):
        if not root: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# iterative dfs
class Solution(object):
    def invertTree(self, root):
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
