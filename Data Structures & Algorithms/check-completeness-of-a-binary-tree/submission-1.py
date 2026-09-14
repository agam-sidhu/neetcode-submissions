# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])                  # BFS queue
        seen_null = False                  # Tracks if we've seen a missing child

        if not root:                       # Empty tree is complete
            return True

        while q:
            node = q.popleft()             # Process next position in level order

            if node is None:
                seen_null = True            # Any later real node would be invalid
            else:
                if seen_null:
                    return False            # Real node appeared after a gap

                q.append(node.left)         # Add left child, even if None
                q.append(node.right)        # Add right child, even if None

        return True                         # No completeness violation found