# Get a number
number = abs(int(input("Enter a number to check whether it is a prime or not : ")))

# To check greater than 1
if number > 1:
    for num in range(2, number):
        # print(number,num)
        if number % num == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")

else:
    print("It is not a prime number") 
