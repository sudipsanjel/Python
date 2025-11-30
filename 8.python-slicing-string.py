#In python slicing means extracting a portion of a sequence like a string,list,tuple etc using a slice syntax.
#Syntax 
   # sequence[start : end : step]
"""
   start -----> index to start from
   end ------> indes to stop at
   step -----> how many step to move
"""

b = "Hello Worls"
print(b[2:7])
"""
start --->2
end ----->7  ( ending string is not included in every  case)
use indexing to confirm yourself
"""

############################################################################################################

#Slicing From The Start 
print(b[ : 5])

############################################################################################################

#Slicing to the end
print(b[4 : ])  #it slice of skip the starting character and goes all the way to end

############################################################################################################

#Negative Indexing
print(b[-5 : -2]) #starting from -5 which is W and end at -2 which is 'l' l is not included

############################################################################################################


