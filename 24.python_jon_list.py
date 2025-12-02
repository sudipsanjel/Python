list1 = ["apple","ball","cat"]
list2 = [1,4,2,6]
list3 = list1 + list2
print(list3)

########################################################################
#can use extend method 
list1.extend(list2)
print(list1)
#It doesnot return but change the list
########################################################################
#using for loop and append
list1 = ["apple","ball","cat"]
list2 = [1,4,2,6]

list3 =[]
for x in list1:
    list2.append(x)
print(list2)
