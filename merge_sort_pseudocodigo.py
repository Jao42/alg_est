from math import floor

def merge(arr, inicio_esq, meio, fim_dir, arr_aux):
  apontador_esq = inicio_esq
  apontador_dir = meio
  for k in range(inicio_esq, fim_dir):
    if apontador_esq < meio and (
        (apontador_dir >= fim_dir) #acabou o array da direita(ent pode jogar o resto dos elem da esq)
        or (arr[apontador_esq] < arr[apontador_dir]) #ou elemento esquerda menor q da direita
    ):
      arr_aux[k] = arr[apontador_esq]
      apontador_esq += 1
    else:
      arr_aux[k] = arr[apontador_dir]
      apontador_dir += 1
  for i in range(inicio_esq, fim_dir):
    arr[i] = arr_aux[i] #populando o array com os novos elementos ordenados

def merge_sort(arr, inicio_esq, fim_dir, arr_aux):
  if (fim_dir - inicio_esq) < 2:
    return 0
  meio = floor((inicio_esq + fim_dir) / 2)
  merge_sort(arr, inicio_esq, meio, arr_aux)
  merge_sort(arr, meio, fim_dir, arr_aux)
  merge(arr, inicio_esq, meio, fim_dir, arr_aux)

arr_len = int(input())
arr = [int(i) for i in input().split()]
merge_sort(arr, 0, arr_len, arr[::])
print(arr)
