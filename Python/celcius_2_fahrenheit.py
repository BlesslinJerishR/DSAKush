class celcius_2_fahrenheit:

    def Temperature():
        choice = int(input("""Enter the Conversion you need to convert
        1. Celcius to Fahrenheit
        2. Fahrenheit to Celcius
        >> """))
        if choice == 1:
            celcius = int(input("""Enter the temperature in degree celcius 
        >> """))
            fahrenheit = (celcius*1.8) + 32
            print("The converted temperature is " , fahrenheit)
        if choice == 2:
           fahrenheit = int(input("""Enter the temperature in degrees fahrenheit
           >> """))
           celcius = (fahrenheit - 32) * (5/9)
           print("The converted temperature is " , celcius)
        else:
            print("Enter 1 or 2 Only")
    Temperature()