#change list iteam
list1 = ["apple","ball","cat","dog"]
list1[0] = "apple1" #it change the value at index 0
print(list1)

########################################################################
#change the range of item value
list1[0:3] = ["CHANGE","THE","LIST"]
#STARTING FROM INDEX 0 AND ENDING AT INDEX 3 ,INDEX 3 NOT INCLUDED
print(list1)

########################################################################
#insert iteam in list anywhere

list1 = ["apple","cat","dog","elephant"]
list1.insert(1,"ball")
print(list1)

#two parameter one for index where to insert
#another for inserting element

