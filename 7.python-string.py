#Python String
#string in pyton are either quotation in either single or double
############################################################################################################

#EXAMPLE
x = 'sudip' #single
y = "sanjel" #double
print(x,y)
############################################################################################################
#quotes inside quotes
print("It's alright")
print('my name is "sudip sanjel"')
print("my name is 'sudip' ")

#cant use same type single or double quotes thats illegal
#print('It's alright) this gives error

############################################################################################################

#Assigning String to Variabe
#String can be assigned to variable as 
x = "hello this is string"
print(x)

############################################################################################################
#Assigning multiline string
x= """
hello my name is sudip sanjel.I am learning python.
This is the example of  assigning multiline string 
"""

print(x)
#we can use single quotes alsosame as double quotes

############################################################################################################

#String As an Array

a = "Hello World"
print(a[1])
#indexing also count space in the string

############################################################################################################

#Looping Through a String 

for x in "sudip":
    print(x)

#another way of loops
x = 'sudip'
for x in x:
    print(x)

#both are same

############################################################################################################

#String Length
#To get length opf the string we use len() function 
#Example
x = "python"
print(len(x))

x = 'I am learning python'
print(len(x))
#can print length of lond strings 
############################################################################################################

#Check String
#it is used to check if the certain character and string is presented in the string
#Example 
x = "my name is sudip sanjel. I am learning python"
print("sudip" in x) #IT gives either true of false value 

#Using if to print 
if 'sanjel' in x:
    print('YES sanjel is in the sentence')

############################################################################################################
#if not is also used like in

print("sanjel" not in x)

#using if
if 'hello' not in x:
  print("hello is not in the string")
