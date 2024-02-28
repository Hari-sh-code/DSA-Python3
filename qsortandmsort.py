class Sorter:
  def __init__ (self,arr):
    self.arr = arr
  def mergesort(self):
    if len(self.arr)>1:
      mid = len(self.arr)//2
      left_arr = self.arr[:mid]
      right_arr = self.arr[mid:]
      left_sorter = Sorter(left_arr)
      right_sorter = Sorter(right_arr)
      left_sorter.mergesort()
      right_sorter.mergesort()
      i,j,k = 0,0,0
      while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
          self.arr[k] = self.arr[i]
          i+=1
        else:
          self.arr[k] = self.arr[j]
          j+=1
        k+=1
      while i<len(left_arr):
        self.arr[k] = left_arr[i]
        i+=1
        k+=1
      while j<len(right_arr):
        self.arr[k] = right_arr[j]
        j+=1
        k+=1
  def quicksort(self,left,right):
    if left < right:
      partition_pos = self.partition(left,right)
      self.quicksort(left,partition_pos-1)
      self.quicksort(partition_pos +1, right)
  def partition(self,left,right):
    i,j,pivot = 0,right-1,self.arr[right]
    while i<j:
      while i < right and self.arr[i]<pivot:
        i+=1
      while j > left and self.arr[i] > pivot :
        j-=1
      if i<j:
        self.arr[i],self.arr[j] = self.arr[j], self.arr[i]
    if self.arr[i] > pivot:
      self.arr[i], self.arr [right] = self.arr[right],self.arr[i]
    return i

original_arr = [9,7,6,4,3,5,7,8,5,3]
print("Original array: ",original_arr)
sorter = Sorter(original_arr)
sorter1 = Sorter(original_arr.copy())
sorter.quicksort(0,len(original_arr)-1)
sorter1.mergesort()
print("QuickSort result: ",sorter.arr)
print("MergeSort result: ",original_arr)
