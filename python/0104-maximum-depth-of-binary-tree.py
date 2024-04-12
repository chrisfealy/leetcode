# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative DFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        depth = 0
        while stack:
            node, node_depth = stack.pop()
            if node:
                depth = max(depth, node_depth)
                stack.append([node.left, node_depth + 1])
                stack.append([node.right, node_depth + 1])

        return depth

# BFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth
