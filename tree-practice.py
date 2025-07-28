class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def postorder_traversal(root):
    # TODO: implement postorder traversal
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

def preorder_traversal(root):
    # TODO: Implement the function
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def second_minimum_in_tree(root):
    # TODO: implement the function
    min_value = second_min_value = None
    def second_minimum_in_nodes(node):
        nonlocal min_value, second_min_value
        if not node:
            return
        if min_value is None:
            min_value = node.value
        elif node.value < min_value:
            second_min_value = min_value
            min_value = node.value
        elif second_min_value is None:
            second_min_value = node.value
        elif min_value < node.value < second_min_value:
            second_min_value = node.value
        second_minimum_in_nodes(node.left)
        second_minimum_in_nodes(node.right)

    second_minimum_in_nodes(root)
    if min_value == second_min_value:
        return None
    return second_min_value

def reverse_tree(root):
    # TODO: implement
    if root is None:
        return None
    reverse_tree(root.left)
    reverse_tree(root.right)
    root.left, root.right = root.right, root.left
    return root

def is_binary_search_tree(root: TreeNode) -> bool:
    # TODO: implement

    def is_binary_search_node(node, max_value=None, min_value=None) -> bool:
        if node is None:
            return True
        if (max_value and node.value > max_value) or (min_value and node.value < min_value):
            return False
        return \
                is_binary_search_node(node.left, max_value=node.value, min_value=min_value) and \
                is_binary_search_node(node.right, max_value=max_value, min_value=node.value)

    return is_binary_search_node(root)

if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
    print(is_binary_search_tree(root))
    root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))
    print(is_binary_search_tree(root))