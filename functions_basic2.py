def countdown(n):
  new_list = []
  for i in range(n, -1, -1):
    new_list.append(i)
  return new_list
# print(countdown(5))

def print_and_return(list):
  print(list[0])
  return list[1]
# print(print_and_return([1,2]))

def first_plus_length(list):
  return list[0] + len(list)
# print(first_plus_length([3,0,0,0,0]))

def values_greater_than_second(list):
  newList = []
  for i in list:
    if i > list[1]:
      newList.append(i)
  print(len(newList))
  return newList
# print(values_greater_than_second([5,2,3,2,1,4]))

def this_length_that_value(size, value):
  return [value] * size
# print(this_length_that_value(7,3))