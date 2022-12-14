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

#Odd Indices

def odd_indices(lst):
  empty_list = []
  for list in range(1, len(lst), 2):
    empty_list.append(lst[list])
  return empty_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

#Exponents

def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base**power)
  return new_list


print(exponents([2, 3, 4], [1, 2, 3]))


#larger_num

def larger_sum(lst1, lst2):
  sum1 = sum(lst1)
  sum2 = sum(lst2)
  if sum1 >= sum2:
      return lst1
  else:
       return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))


# Over 9000

def over_nine_thousand(lst):
  sum1 = 0
  for number in lst:
    sum1 += number
    if sum1 >= 9000:
      break
  return sum1
  
 
print(over_nine_thousand([8000, 900, 120, 5000]))

#Max_num

def max_num(nums):
  maxVal = nums[0]
  for number in nums:
    if number > maxVal:
      maxVal = number
  return maxVal

print(max_num([50, -10, 0, 75, 20]))

#Same values

def same_values(lst1, lst2):
  newList = []
  for list in range(len(lst1)):
      if lst1[list] == lst2[list]:
        newList.append(list)
  return newList

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Reversed List

def reversed_list(lst1, lst2):
  for list in range(len(lst1)):
    if lst1[list] != lst2[len(lst2) - 1  - list]:
      return False
  return True
   


print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


#Simple Math challenges

def tenth_power(num):
  return pow(num, 10)

print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))


#dog years

def dog_years(name, age):
  age_of_dog = age * 7
  return name + ", " + "you are " + str(age_of_dog) + " years old in dog years"

print(dog_years("Lola", 16))

print(dog_years("Baby", 0))


#all operations

def lots_of_math(a, b, c, d):
  first =  a + b
  second = c -d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth
  

print(lots_of_math(1, 2, 3, 4))

print(lots_of_math(1, 1, 1, 1))
