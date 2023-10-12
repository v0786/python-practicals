#Create tuple
t = (1, 2, 3, 4, 5)
print ("The values in tuple are:",t)
#add element in tuple
t=t+(7,)
print ("Tuple after adding element :",t)
#slice tuple
print ("Tuple after slice : ", t[2:4]) #multiplication
print(" Multiplication : ", (t*2))
#len of tuple
print (" The length of tuple is:", len(t))
#find maximum and minimum value in tuple
print ("The maximum value of tuple is: ",max(t))
print ("The maximum value of tuple is: ",min(t)) #delete tuple
del t
print ("Tuple deleted" )
