#Modifying the string in Python
#python has buit in methods that you can use in string

#####################################################################
#Upper case

#The upper() function return all the string or character in uppercase
# EXAMPLE
a = "I am learning python and using git to save code"
print(a.upper()) 



def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


def hello():
    return "Hello World"

hello=uppercase(hello)
print(hello())


list1=[1,2,3,4]


square_of_num=list(map(lambda x: x**2,list1))
print(square_of_num)


even_num=list(filter(lambda x: x%2==0, list1))
print(even_num)



y=lambda x,y,z: x+y+z 
print(y(1,2,3))