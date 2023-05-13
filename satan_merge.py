from math import floor

def merge(arr, inicio_esq, meio, fim_dir, arr_aux):
  apontador_esq = inicio_esq
  apontador_dir = meio
  for k in range(inicio_esq, fim_dir):
    if apontador_esq < meio and (
        (apontador_dir >= fim_dir) #acabou o array da direita
        or (arr[apontador_esq] < arr[apontador_dir]) #elemento esquerda menor q da direita
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
  particao_format = ('{'
  + ', '.join(
    str(i) for i in arr[inicio_esq:fim_dir])
  + '}')
  esq_format = ('{' +
                ', '.join(
                  str(i) for i in arr[inicio_esq:meio]
                ) + '}')
  dir_format = ('{' + ', '.join(
    str(i) for i in arr[meio:fim_dir]
  ) + '}')
  print(f'Separando o array V[{inicio_esq}...{fim_dir - 1}] : '
        + f'{particao_format} em V[{inicio_esq}...{meio - 1}] : '
        + f'{esq_format} e V[{meio}...{fim_dir - 1}] : {dir_format}')

  merge_sort(arr, inicio_esq, meio, arr_aux)
  merge_sort(arr, meio, fim_dir, arr_aux)
  esq_sort_format = ('{' +
                     ', '.join(
                       str(i) for i in arr[inicio_esq:meio]
                     ) + '}')
  dir_sort_format = ('{' +
  ', '.join(
    str(i) for i in arr[meio:fim_dir]
  ) + '}')
  print(f'Executando o merge nos arrays {esq_sort_format} e {dir_sort_format}')
  merge(arr, inicio_esq, meio, fim_dir, arr_aux)
  particao_ord_format = '{' + ', '.join(str(i) for i in arr[inicio_esq:fim_dir]) + '}'
  print(f'array ordenado : {particao_ord_format}')

input()
arr = [int(i) for i in input().split()]
merge_sort(arr, 0, len(arr), arr[::])
print(f'\nO array ordenado : {" ".join(str(i) for i in arr)}')
