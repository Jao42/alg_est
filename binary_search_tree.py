#[1, 2, 3, 4, 5, 6, 7]

class BST_Node():
  def __init__(self, value: int, left_node=None, right_node=None):
    self.value = value
    self.left_node = left_node
    self.right_node = right_node
  def __str__(self):
    return str(self.value)


class BinarySearchTree():
  def __init__(self, elements: list):
    self.elements = elements
    self.inicio = self.createBinarySearchTree()

  def createBinarySearchTree(self):
    inicio = BST_Node(self.elements[0])
    els = self.elements[1::]
    for i in els:
      atual = inicio
      while True:
        atual_value = atual.value
        if i >= atual_value and atual.right_node == None:
          atual.right_node = BST_Node(i)
          break
        if i < atual_value and atual.left_node == None:
          atual.left_node = BST_Node(i)
          break
        if i >= atual_value:
          atual = atual.right_node
          continue
        atual = atual.left_node
    return inicio
  def find_element(self, e: int) -> bool:
    atual = self.inicio
    print("inicio ->", atual.value)
    while atual != None:
      value = atual.value
      if e > value:
        atual = atual.right_node
        print("direita -> ", atual.value)
        continue
      if e < value:
        atual = atual.left_node
        print("esquerda -> ", atual.value)
        continue
      print("ENCONTRADO!")
      return True
    print("NÃO ENCONTRADO!")
    return False
  def em_ordem(self, node='') -> str:
    if node == '':
      node = self.inicio
    if node == None:
      return ''
    self.em_ordem(node.left_node)
    print(node, end=' ')
    self.em_ordem(node.right_node)

a = BinarySearchTree([21, 2, 100, 432, 43, 22])
print(a.find_element(22))
a.em_ordem()
