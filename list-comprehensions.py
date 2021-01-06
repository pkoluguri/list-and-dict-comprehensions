#creating an (num) list
nums = [1,2,3,4,5,6,7,8,9]
#creating another (list1) and adding (n) variable for the elements in nums 
list1 = [n for n in nums]
print(list1)
#using map and lambda
#creating an list (my_list) taking evry element in nums and making an variable (n) and multiplying with itself
my_list = map(lambda n: n*n, nums)
print(my_list)
#doing the samething but it is more easy to understand
square = [n*n for n in nums]
print(square)
#taking evry even number in nums
even = [n  for n in nums if n%2==0]
print(even)
#using the filter and lambda
#doing the same thing but in lambda
unique_nums = filter(lambda n:n%2 == 0,nums)
print(unique_nums)
#creating an list my_list and for letter in abcd we are assingning each number from 1 to 4
my_list = [(letter,num) for letter in "abcd" for num in range(4)]
print(my_list)
#creating an nums list with some elements repeating
nums = [1,1,2,2,3,4,5,6,7,7,8,9,9]
#creating an set and adding each element of nums in unique_nums and because it is set evry element is unique 
unique_nums = {n for n in nums}
print(unique_nums)