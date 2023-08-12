from BinaryTree import Node
from BinaryTree import BinaryTree

quant_nos, quant_pais = [int(i) for i in input().split()]
nos_valores = [[int(i) if i != '-1' else None for i in input().split()] for j in range(quant_pais)]

nos = []
for val in nos_valores:
  no = Node(val[0])
  no.left = Node(val[1]) if val[1] != None else None
  no.right = Node(val[2]) if val[2] != None else None
  nos.append(no)

possiveis_pais = []
arvore = None
for no in nos:
    if no.value == 0:
        arvore = BinaryTree(no)
        possiveis_pais.append(no.left)
        possiveis_pais.append(no.right)
        continue
    #substituir lista por fila em prox. refat
    while(len(possiveis_pais) != 0):
        atual = possiveis_pais.pop(0)
        if no.value == atual.value:
           atual.left = no.left
           atual.right = no.right
           possiveis_pais.append(atual.left)
           possiveis_pais.append(atual.right)
           break

arvore.pre_order()
print('\n')
arvore.in_order()
print('\n')
arvore.post_order()
print('\n')

