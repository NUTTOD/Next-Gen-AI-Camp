def list(lst):
  for i in range(len(lst) - 1):
      if lst[i] > lst[i + 1]:
          return False
  return True

sample_list = [1, 2, 3, 4, 5]
print(list(sample_list))  

sample_list = [5, 4, 3, 2, 1]
print(list(sample_list))