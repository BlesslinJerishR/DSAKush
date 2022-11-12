class fibonacci_series:
    def Fibonacci_series():
        fibonacci = [0,1]
        n1, n2 = 0,1
        maxi = int(input("Enter a Number to generate Fibonacci series : "))
        if maxi >= 0:
            for num in range(1,maxi):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                fibonacci.append(n3)
            print(f"The fibonacci numbers of {maxi} numbers are {fibonacci}")
        else:
            print("Enter a positive number")
    Fibonacci_series()