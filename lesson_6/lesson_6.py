unsorted_list = [24, 23, 1, 2, 15, 5, 8, 17, 99, 0, -11, -2, 4, 5, 66, 52, 53, 50, 49, 42]

# BUBBLE SORT
def bubble_sort(lst):
   n = len(lst)
   for i in range(n):
      for j in range(0, n-i-1):
         if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
   return lst

print(bubble_sort(unsorted_list))

# SELECTION SORT
def selection_sort(lst):
   n = len(lst)
   for i in range(n):
      min_index = i
      for j in range(i+1, n):
         if lst[j] < lst[min_index]:
            min_index = j
      lst[i], lst[min_index] = lst[min_index], lst[i]
   return lst
 
print(selection_sort(unsorted_list))


# BINARY SEARCH
def binary_search(Val, lst):
   First = 0
   Last = len(lst) - 1
   ResultOk = False
   Pos = -1

   while First <= Last:
      Middle = (First + Last) // 2
      if Val == lst[Middle]:
         ResultOk = True
         Pos = Middle
         break
      elif Val > lst[Middle]:
         First = Middle + 1
      else:
         Last = Middle - 1

   if ResultOk:
      print(f"Элемент найден")
   else:
      print("Элемент не найден")

   return Pos

sorted_list = bubble_sort(unsorted_list)
result = binary_search(99, sorted_list)
print(f"Результат поиска: {result}")