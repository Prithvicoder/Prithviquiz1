num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
        num1 = int(num1)
        num2 = int(num2)
        for x in range(num1,num2+1):
          if x % 2 == 0:
            print(x,"is an even number")

except ValueError:print("Please enter a number.")  
  

try:

    num1 = int(num1)
    num2 = int(num2)   
    if num2<num1:
        print ("please enter the smallest number first")
except ValueError:print() 