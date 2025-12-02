#List comprehension in pyton is a short and clean way to create list
#syntax list = [expression for iteam in iterable]
#Example
list1 = [1,2,3,4,5,6,7,8,9,10]
#creating the square  list of the list1
square_list = [x*x for x in list1]
print(list1)
print(square_list)

########################################################################
#with if condition in list
list1 = ["apple","ball","cat","dog","elephant"]
list2 = []
for x in list1:
    if "a" in x:
        list2.append(x)

print(list2)

list3 = [x for x in list1 if "a" in x] #same concept
print(list3)
#for loop with append in list2
#can understand more in loop

########################################################################
#for loop with range 
list4 = [x for x in range(10) if x > 5]
print(list4)
#range is used to generate number 
#range is also useful for indexing in pyton

########################################################################

