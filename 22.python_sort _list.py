#can short alphanumerically
list1 = ["apple","ball","aeroplane","aerospace","alphabet"]
list1.sort()
print(list1)
#It change the orginal list

########################################################################
#numerically
list1 = [1,5,3,7,9,2,10,1000,100]
list1.sort()
print(list1)

########################################################################
#for reverse shorting 
list1 = ["apple","ball","aeroplane","aerospace","alphabet"]
list1.sort(reverse=True)
print(list1)


########################################################################
list1 = [1,5,3,7,9,2,10,1000,100]
list1.sort(reverse=True)
print(list1)

#It take parameter reverse = True for shordind in decending order
########################################################################
#Case sensitive 
#IT sort capital letter first and only lower case 
list1 = ["Ball","apple"]
list1.sort()
print(list1)


#we can use built in function key to solve this problem
list1.sort(key = str.lower)
print(list1)

########################################################################
#reverse the list regardless opf the apphabet
list1 = ["apple","ball","aeroplane","aerospace","alphabet"]
list1.reverse()
print(list1)

########################################################################
