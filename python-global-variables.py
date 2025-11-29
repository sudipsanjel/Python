#Global Variables
#Variable that are created outside of the functions

x = "python"

def myfunc():
    print("i am learning " + x)

myfunc()   #function calling

''' 
global and local variable difference is that 
global variable is golbally available and can be access by any function 
local variable is defined inside the function and that specific function can access that variable.
'''
#EXAMPLE

x = "sudip "

def func():
    x= 'sanjel' #local variable
    print(x)

func()

def func2():
    print(x)  #using global variable

func2()

# we can create global variable inside function by global key word

def sudip():
    global x 
    x = 'sudip'
    print(x)

sudip()

def sanjel():
    print(x)

sanjel()