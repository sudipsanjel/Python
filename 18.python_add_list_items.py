#Append items
#to add item at the end of the list

list1 = ['apple', 'ball', 'cat', 'dog', 'elephant']
list1.append("fan")
print(list1)

########################################################################

#insert item
list1.insert(0,"inserting")
print(list1)

########################################################################
#extend list
#to append element from another list to the current list
list1 = ['apple', 'ball', 'cat', 'dog', 'elephant']
list2 = ['fan','gun','hang']
list1.extend(list2)
print(list1)
#change the list1 or append element of list2 into list1

########################################################################

#Add any Iterable
#extend method doesnot have to be list it works for list and tuple also

list1 = ['apple', 'ball', 'cat', 'dog', 'elephant']
tuple1 = ("fan","gun")
list1.extend(tuple1)
print(list1)

########################################################################
