#Every Three Numbers

def every_three_nums(start):
  num_between = [*range(start, 101, 3)]
  return num_between

print(every_three_nums(81))


#Remove Middle

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1]
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#More Frequent Item

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2
  
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


#Double Index

def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        newList = lst[0:index]
        newList.append(lst[index] * 2)
        newList = newList + lst[index+1:]   
        return newList
  
print(double_index([3, 8, -10, 12], 2))


#Middle Item

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

#Divisible by Ten
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if (num % 10 == 0):
      count += 1
  return count
      

print(divisible_by_ten([20, 25, 30, 35, 40]))


#Delete Start Even Numbers

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))