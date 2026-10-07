print("Enter a number less than 25")
number = int(input())

if number > 25:
    print("Error")
else:
   for i in range (number,26,1):
        print (f"Inside the loop, my variable is {i}")
