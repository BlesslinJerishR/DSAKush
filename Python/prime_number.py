num = abs(int(input("Enter a number to check whether it is a prime or not : ")))
checker = 2
if num == 0:
        print("It is not a prime number")
elif num == 1 or num == 2:
        print("It is a prime number")
else:
    while checker < num:
        if num % checker == 0:
            print("It is not a prime number")
            break
        else:
            print("It is a prime number")
            break