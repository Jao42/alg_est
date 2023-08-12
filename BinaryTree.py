class Node:
  def __init__(self, value, node_left=None, node_right=None):
    self.left = node_left
    self.right = node_right
    self.value = value

class BinaryTree:
  def __init__(self, root):
    self.root = root
  def in_order(self, node='', camada=0):
    if node == None:
      return ''
    if node == '':
      node = self.root
    camada_atual = camada + 1
    self.in_order(node.left, camada_atual)
    print(('\t' * camada) + f'{node.value:4d}')
    self.in_order(node.right, camada_atual)

  def pre_order(self, node='', camada=0):
    if node == None:
      return ''
    if node == '':
      node = self.root
    camada_atual = camada + 1
    print(('\t' * camada) + f'{node.value:4d}')
    self.pre_order(node.left, camada_atual)
    self.pre_order(node.right, camada_atual)

  def post_order(self, node='', camada=0):
    if node == None:
      return ''
    if node == '':
      node = self.root
    camada_atual = camada + 1
    self.post_order(node.left, camada_atual)
    self.post_order(node.right, camada_atual)
    print(('\t' * camada) + f'{node.value:4d}')
