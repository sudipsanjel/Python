#Modifying the string in Python
#python has buit in methods that you can use in string

#####################################################################
#Upper case

#The upper() function return all the string or character in uppercase
# EXAMPLE
a = "I am learning python and using git to save code"
print(a.upper()) 
print("sudip".upper())
#Both are valid 

#####################################################################
b = 'HELLO WORLD!'
print(b.lower())
print("SUDIP".lower())

#####################################################################
#Remove WhiteSpace
#It removes space from before or after the actual text from strings
c = "     I am learning Python"
print(c.strip())
print("       i am learning Python ".strip())
#Both are same 

#####################################################################

#Replace String
#replace() is used to replace a string with another string
d = " Hello Python"
print(d.replace("H","K"))
print("PYTHON".replace("P","K"))

#####################################################################

#Split String
e = "my,name,is,sudip"
print(e.split(","))
print("my,name".split(","))
#NOTE: we can also use character to split the string

#####################################################################




