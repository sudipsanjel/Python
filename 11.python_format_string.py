#String Format
#we cannot combine or concatenation the string and variable
#print("I am learning python for ",+ 5) 
#That is illegal 
#we can combine string and variable usinf f-string of format() methos
#example
days = 5
txt = f"i am learning python for {days} days"
print(txt)
#OR
print(f"i am learning python for {days} days")
#####################################################################
#Placeholder and Modeifier

#Placeholder are special symbols inside string that get replaced by actual value
#Example

days = 10
txt = f"I am learning python fot {days} days"
print(txt)
#days variable is place holder inside that txt string's

#Modifier 
#Modifier control how the value appers inside the placeholder

value = 3.141527
print(f"value of pi is {value:.2f}")
#It print only 2 decimal points
print(f"using negative {value:+}")
print(f"using negative {value:-}") #by defult is 3.141527


#####################################################################



