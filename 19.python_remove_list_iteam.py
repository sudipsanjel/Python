#To remove specific iteam
list1 = ['apple', 'ball', 'cat', 'dog', 'elephant', 'fan', 'gun']
list1.remove("apple")
print(list1)

########################################################################
#pop method
#it remove item of specific index
list1 = ['apple', 'ball', 'cat', 'dog', 'elephant', 'fan', 'gun']
list1.pop(1)
print(list1)

#if parameter is not given to pop it will remove all iteam from list
#del keyword is aldo used to remove the iteam by indexing
list1 = ['apple', 'ball', 'cat', 'dog', 'elephant', 'fan', 'gun']
del list1[0]
print(list1)

########################################################################
#clear method clear all the list element
list1.clear()
print(list1)

########################################################################
