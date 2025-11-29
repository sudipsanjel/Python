#VARIABLES

x= 5
y = 'sudip'
z = 3.1415

print(x,y,z)

######################################################################################


#CASTING
#if you want to specify the data type of variable this can be done using casting
#conversion from one to another data type 

x = str(3)
y = float(3)
z = int(3.14)

print(x,y,z)

######################################################################################


#Get the type of data
#EXAMPLE 
#Lets take the above variables
print(type(x))
print(type(y))
print(type(z))


######################################################################################


#VARIABLES NAME

myvar = 'sudip'
my_var = 'sudip' 
_myvar = 'sudip' 
myvAR = 'sudip' 
MYVAR = 'sudip' 
myvar1 = 'sudip'

#illegal variables name
"""
2myvar = 'sudip'
my-var = ' sudip'
my var = 'sudip'

"""


######################################################################################



#MANY VALUE TO MULTIPLE VARIABLE

x,y,z = "sudip","is","programming"
print(x)
print(y)
print(z) 

#ONE VALUE TO MULTIPLE VARIABLE

x = y = z = "sudip is programming"
print(x)
print(y)
print(z) 

######################################################################################

#Unpack a collection 
#if you have collection of avlue in list 
#python is allowed to unpack or extract thr value from the list
#EXAMPLE

name = ['sudip','ram','shyam'] 

x,y,z = name
print(x)
print(y)
print(z) 

