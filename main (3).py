#Created by: Owen Whalley
#Created on: 2022/10/11

#asks the user what value is being multiplied by another value, and assigns it to the variables x and y.
x = int(input("What is your first variable? : "))
y = int(input("What is your second variable? : "))

#assign the final answer represented by a to the value of 0.
a = 0

#multiplies using only addition and a while loop.
while y > 0:
    a += x 
    y -= 1
  
  #print the the final answer
print("The product is "+str(a))