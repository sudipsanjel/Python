#Note all string methods return new values 
#they doesnot change the orginal value 

a = "this IS string"
#capitalize()
#change first lettter of string into capital letter

b = a.capitalize()
print(b)

#####################################################################
#casefold()
#convert string into lower case //same as lowercase()

b = a.casefold()
print(b)


#####################################################################
#center()
#string will be placed in the center of given length
text = "hello"
print(text.center(10,"2"))

#####################################################################
#count()
#return the number of times a specified value occurs in a string

text = "i am learning python"
print(text.count("a")) #occurance of a is 2

#####################################################################
#encode()
#return the encoded version of string
print(text.encode())
#####################################################################
#endswith()
#return true if the string ends with specified vacle
text = "the string end with a"
print(text.endswith("with a"))
print(text.endswith("a"))

#####################################################################
#expandtabs()
#sets the tab size for string
text = "hello \t world"
print(text.expandtabs(10))
#basicall the argument decide the size of tab
#####################################################################
#find()
#To find the specific word or character in the string
text = "i am learning python .find python using find()"
print(text.find("python"))

#####################################################################
#format()
#used in modification of placeholder


#format_map()
#format specified value in the string
text ="Hello World {place}"
print(text.format(place ="place holder"))

text2 = "Hello {place1} .Thjs is {place2}".format(place1= "world",place2="pyrhon")
print(text2)

#########################################################################
#index()
#It is used for finding the occurrence of word in strings
text = "The index is used to find the occurrence in string"
print(text.index("i",2,20))

#string start and ending can be given in index() method

########################################################################
#isalnum()
#Return true if all the character in the string is alpha numeric

text = "Hello123"
print(text.isalnum())


########################################################################

#isalpha()
#Return true if all the characters in string is alphabet
text = "aeitou hhh"
print(text.isalpha())


########################################################################
#isascii()
#Return true if all character are ascii in string
print(text.isascii())


########################################################################
#isdecimal()
#Return true if all string is decimal 
print(text.isdecimal())


########################################################################
#isdigit()
#Return true if al character in string is digit
print(text.isdigit())




########################################################################
#isidentifier()
#Return true if the string is identifier 
text = "def"
print(text.isidentifier())

########################################################################
#islower()
#Return true if atring is lowercase
text ="I am learning python . Python is fun"
print(text.islower())


########################################################################
#isnumeric()
#Return true if all string are numeric
print(text.isnumeric())


########################################################################
#isprintable()
#Return true if all character is printable
print(text.isprintable())

########################################################################
#isspace()
#Return true if all character is whitespace
text=" "
print(text.isspace())

########################################################################
#istitle
#Return true if string follows the rule of title
#Title means starting case is upper case and rest is lowercase and no space
text = "Helloworld"
print(text.istitle())

########################################################################
#isupper()
#Return true if all string are in upper case
print(text.isupper())

########################################################################
#join()
#Join takes all item as iterable and join them together
myTuple = {"Python" ,"is","fun"}
print(" ".join(myTuple))

########################################################################
#ljust()
#used to left aligh the text
print(text.ljust(20,"&"))

########################################################################
#lower()
#Convert string into lowercase
print(text.lower())

########################################################################
#lstrip()
#Return the left trim version of string
txt = "     Strip      "
x  = txt.lstrip()
print("This is left ",x,"Example")

########################################################################
#maketrans()
#This method return a mapping table that can be used with the translate() method
#to replace specified character
txt = "hello ram"
x = "arm"
y = "ejo"
myTable = str.maketrans(x,y)
print(txt.translate(myTable))

########################################################################

#partition()
#Return a tuple where the string is parted into three parts
txt = "I am learning python"
print(txt.partition("learning"))

#create three partition where one partition is given as argument

########################################################################
#replace()
txt = "i like learning python"
print(txt.replace("python","programming language"))
#can take three parameter.the third one is for occurance words

########################################################################
#rfind()
#The rfind methos is used to find the last occurance of the specified value.
#takes two parameter one for start and end
print(txt.rfind("e"))
print(txt.rfind("e",7,20))
#starting and ending position is for the two parameter

########################################################################

#rindex()
#The rindex() method finds the last occurrence of the specified value
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
#print last occurance of 'case' string
#extra two parameter can be given for start and and end of the position.
########################################################################
#rjust 
#It will give right align of the string
#Example
txt = "     string     "
txt = txt.rjust(20,"@")
x = f"hello this is {txt} used for rjust"
print(x)
#It is used for alignment

########################################################################

#rpartition()
#The rpartition() method searches for the last occurrence of a specified string,
# and splits the string into a tuple containing three elements.
txt = "Python is fun.Python is a programming language"
print(txt.rpartition("python"))

########################################################################

#rsplit()
#The rsplit() method splits a string into a list, starting from the right.

txt = "ram , shyam , hari"
print(txt.rsplit(","))

#makes the list from right

########################################################################
#rstrip()
#Return the right trim version of the string.
txt = "banana ,s"
x= txt.rstrip(",s")
print("this is ",x,"It is fruit")
#trim ,s from txt 

########################################################################
#split()
#split a string into a ist where each word is a list
txt = "welcome to the jungle"
print(txt.split())
print(txt.split(" "))
#parameter for spliting position 

########################################################################
#splitlines()
#split the string at the line brakes and return a list
txt = "hello this is \n string line brake"
print(txt.splitlines())
#true of false parameter is used to specified 
# splitted parameter should be included or not

########################################################################

#startwith()
#Return true if the string starts with the specified value
txt = "Hello world"
print(txt.startswith("HELLO"))

########################################################################
#strip()
#return trim version of the string
#remove extra whitespace in the string
txt = "     Hello    "
print(txt.strip())

########################################################################
#swapcase()
#In swap case lower case become upper case and upper case become lower case.
txt = "hELLO WORLD"
print(txt.swapcase())

########################################################################
#title()
#Convert each character of each word to upper case
txt = "hello world"
print(txt.title())

########################################################################
#translate()
#Return a translated string
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))

########################################################################
#upper()
#return a upper case of string
txt = " www.github.com/sudipsanjel"
print(txt.upper())

########################################################################
#zfill()
#Fills the string with a specified number of 0 values at rhe beginning.
txt = '50'
print(txt.zfill(10))


########################################################################
