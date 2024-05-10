from typing import List

class Solution:
  def findKthLargest(self, nums: List[int], k: int, inicio=0, fim=None) -> int:
    if fim is None:
      fim = len(nums) - 1
    index = len(nums) - k
    index_pivot = self.particionar(nums, inicio, fim)
    if index_pivot == index:
      return nums[index_pivot]
    if index_pivot > index:
      return self.findKthLargest(nums, k, inicio, index_pivot - 1)
    return self.findKthLargest(nums, k, index_pivot + 1, fim)


  def particionar(self, arr, inicio, fim):
    particao = arr[inicio:fim + 1]
    tam = fim - inicio + 1
    pivot = particao[randint(inicio, fim + 1)]
    p_inicio = 1
    p_fim = len(particao) - 1

    while p_inicio <= p_fim
      if particao[p_inicio] <= pivot:
        p_inicio += 1
        continue
      if particao[p_fim] > pivot:
        p_fim -= 1
        continue
      aux = particao[p_inicio]
      particao[p_inicio] = particao[p_fim]
      particao[p_fim] = aux
      p_inicio += 1
      p_fim -= 1

    particao[0] = particao[p_fim]
    particao[p_fim] = pivot
    for i in range(len(particao)):
      arr[i + inicio] = particao[i]
    return p_fim + inicio


sol = Solution()
arr = [123, 434, 55, 333, 12, 100]
print(sol.findKthLargest(arr, 3))
  

