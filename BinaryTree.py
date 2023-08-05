class Node:
  def __init__(self, value, node_left=None, node_right=None):
    self.left = node_left
    self.right = node_right
    self.value = value

class BinaryTree:
  def __init__(self, root):
    self.root = root
  def in_order(self, node=''):
    if node == None:
      return ''
    if node == '':
      node = self.root
    self.in_order(node.left)
    print(node.value, end=' ')
    self.in_order(node.right)

  def pre_order(self, node=''):
    if node == None:
      return ''
    if node == '':
      node = self.root
    print(node.value, end=' ')
    self.pre_order(node.left)
    self.pre_order(node.right)

  def post_order(self, node=''):
    if node == None:
      return ''
    if node == '':
      node = self.root
    self.post_order(node.left)
    self.post_order(node.right)
    print(node.value, end=' ')

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
binary_tree = BinaryTree(root)

binary_tree.in_order()
print('\n')
binary_tree.pre_order()
print('\n')
binary_tree.post_order()
