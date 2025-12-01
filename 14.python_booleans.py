#Booleans represent one of the two values
#eother TRUE or FALSE
#in programming the booleans is used to know if the given expression is true or false
#EXAMPLE
print(10 > 5)  #TRUE
print(1 == 0)  #FALSE
print(5 < 3)  #TRUE
#When you run a condition in if statement it gives true of false according to cindition
########################################################################
#IF STATEMENT
#EXAMPLE
x = 10
y = 4
if x > y:
    print(x,"is grater than",y)
else:
    print(y,"is grater than",x)

########################################################################
#EVALUATE VALUE AND VARIABLES
#thr bool() function gives you to evaluate any value and give you TRUE or FALSE

print(bool('hello'))
print(bool(15))
print(bool(10<4))
#The input like false,none,0,"",(),[],{} gives false value
#########################################################################
# FUNCTION CAN RETURN BOOLEAN

def myFUNCTION():
    return True
x= myFUNCTION()
print(x)  
print(myFUNCTION())

#printing yes if true and no if false
if myFUNCTION():
    print("yes")
else:
    print("no")

########################################################################

#isinstance()
x = 100
print(isinstance(x,int))
#isinstance return true or false and it is built in function

########################################################################

 