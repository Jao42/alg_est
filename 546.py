class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None


def parsear_str_arvore(str_arvore):

  str_arvore = str_arvore[1:-1]
  inicio_esq = str_arvore.find('(')
  valor = str_arvore[:inicio_esq]
  if valor == '':
    return None
  no = No(int(valor))

  aux = 0
  fim_esq = 0
  for i in range(len(str_arvore)):
    if str_arvore[i] == '(':
      aux += 1
    if str_arvore[i] == ')':
      aux -= 1
      if aux == 0:
        fim_esq = i
        break
  no.esquerda = parsear_str_arvore(str_arvore[inicio_esq:fim_esq + 1])
  no.direita = parsear_str_arvore(str_arvore[fim_esq + 1::])
  return no


def em_ordem(no):
  if no == None:
    return ''
  em_ordem(no.esquerda)
  print(no.valor)
  em_ordem(no.direita)



def verificar_no_bst(no, minimo=float('-inf'), maximo=float('inf')):
  if not no:
    return True
  if no.valor <= minimo or no.valor >= maximo:
    return False

  return (verificar_no_bst(no.esquerda, minimo, no.valor) and
    verificar_no_bst(no.direita, no.valor, maximo))

str_arvore = input().replace(" ", "")
no = parsear_str_arvore(str_arvore)
print("VERDADEIRO" if verificar_no_bst(no) else "FALSO")
