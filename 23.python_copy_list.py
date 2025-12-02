#we can directly copy list by list1 = list2 
#but list1 will be reference to list2 so change made in list 1 will change in list2
#using copy method
list1 = ['ball', 'apple', 'alphabet', 'aerospace', 'aeroplane']
list2 = list1.copy()
print(list2)

########################################################################
#using list method
list3 = list(list2)
print(list3)
