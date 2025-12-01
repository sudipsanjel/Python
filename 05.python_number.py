#Python Numbers 
#There are three numeric data type in python
#int float complex
#Examoles 
a = 1     #integer 
b = 1.1     #float
c = 1j    #Complex number
#To check the data type use this code
print(type(a))
print(type(b))
print(type(c))
##########################################################################################
#Integer 
#Integer are value of positive, negative and whole number but not the decimal number
#Example
x = 1
y = -1 
z = 2837373
#To check the data type
print(type(x))
print(type(y))
print(type(z))


#########################################################################################
#Float 

x = 1.1
y = -1.1
z = 38373.272
#To check the data type
print(type(x))
print(type(y))
print(type(z))


#########################################################################################
#Complex
x = 1+1j
y = 1j
z = -6j
#To check
print(type(x))
print(type(y))
print(type(z))


########################################################################################
#Type conversion In python
#You can convet the data type into any data tyoe by simple int() float() and complex () function
#Example
x = 1 #int
y = 1.1 #float
z = 2j   #complex
a = 1+2j #complex

#conversion from int to float 
c = float(x)
print(c) #int to float
d = int(y)
print(d) #float to integer
e = complex(x)
print(e) #int to complex
f= complex(y)
print(f) #float to complex

#note you cannot comvert complex number to other data type



####################################################################################
#Python doesn't have the random number function 
#but it has built in module for generating random numbers 
#Example
import random 

print(random.randrange(1,10))

print(random.randrange(1,100))

    