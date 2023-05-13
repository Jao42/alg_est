class Decoracao:
  def decorar_particao(arr, inicio, fim):
    return ('{'
    + ', '.join(
    str(i) for i in arr[inicio:fim])
    + '}')

  def mostrar_etapas_passo_recursivo(passo_rec_func):
    def wrapper(*args):
      arr, inicio_esq, meio, fim_dir, arr_aux = args
      arr_decorado = Decoracao.decorar_particao(arr, inicio_esq, fim_dir)
      esq_decorado = Decoracao.decorar_particao(arr, inicio_esq, meio)
      dir_decorado = Decoracao.decorar_particao(arr, meio, fim_dir)
      print(f'Separando o array V[{inicio_esq}...{fim_dir - 1}] : '
          + f'{arr_decorado} em V[{inicio_esq}...{meio - 1}] : '
          + f'{esq_decorado} e V[{meio}...{fim_dir - 1}] : {dir_decorado}')

      passo_rec_func(*args)
      esq_ord_decorado = Decoracao.decorar_particao(arr, inicio_esq, meio)
      dir_ord_decorado = Decoracao.decorar_particao(arr, meio, fim_dir)
      print(f'Executando o merge nos arrays {esq_ord_decorado} e {dir_ord_decorado}')
    return wrapper

  def mostrar_partes_mergeadas(merge_func):
    def wrapper(*args):
      merge_func(*args)
      arr, inicio_esq, meio, fim_dir, arr_aux = args
      arr_ord_decorado = Decoracao.decorar_particao(arr, inicio_esq, fim_dir)
      print(f'array ordenado : {arr_ord_decorado}')
    return wrapper


def merge_sort(arr, inicio_esq, fim_dir, arr_aux):
  @Decoracao.mostrar_partes_mergeadas
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

  @Decoracao.mostrar_etapas_passo_recursivo
  def passo_recursivo(arr, inicio_esq, meio, fim_dir, arr_aux):
    merge_sort(arr, inicio_esq, meio, arr_aux)
    merge_sort(arr, meio, fim_dir, arr_aux)


  if (fim_dir - inicio_esq) < 2:
    return 0
  meio = int((inicio_esq + fim_dir) / 2)
  passo_recursivo(arr, inicio_esq, meio, fim_dir, arr_aux)
  merge(arr, inicio_esq, meio, fim_dir, arr_aux)


arr_len = int(input())
arr = [int(i) for i in input().split()]
merge_sort(arr, 0, arr_len, arr[::])
print(f'\nO array ordenado : {" ".join(str(i) for i in arr)}')
