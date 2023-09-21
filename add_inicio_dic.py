dic_inicial = {"Segundo" : 2, "Terceiro" : 3, "Quarto" : 4}


def dic_add_inicio(dic_inicial, chave, valor):
  dic_novo = {}
  dic_novo[chave] = valor
  for i in list(dic_inicial.keys()):
      dic_novo[i] = dic_inicial[i]
  return dic_novo


novo_dic = dic_add_inicio(dic_inicial, "Primeiro", 1)
print(novo_dic)
