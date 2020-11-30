#   Matthew Lingle
#  ​CSCI 101 – Section B
#   Python Lab 5
#   References: None
#   Time: 2 hours
import os

def restart():
    restart = input(" Would you like to restart this program ? (y/n) ")
    if restart.lower() == "yes" or restart.lower() == "y":
        
        clear = lambda: os.system('cls')
        clear()
        Main()
    if restart.lower() == "n" or restart.lower() == "no":
        print(" Goodbye")
        print(" =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        exit()

def Main():
    print(" Welcome to the Binary-Octal-Decimal Converter")
    print(" =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print(" Enter an option: ")
    print(" 1. Binary-Decimal Conversion ")
    print(" 2. Decimal-Binary Conversion")
    print(" 3. Octal-Decimal Conversion")
    print(" 4. Decimal-Octal Conversion")
    print(" 5. Quit")
    inp = int(input(" Option> "))
    
    if inp == 1:
        binary = input(" BINARY-STR>")
        for value in binary:
            if value != "0" and value != "1":
                print(" ERROR: Input", binary, "is NOT a binary number.")
                restart()
        binary = int(binary)
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while binary1 != 0:
            dec = binary1 % 10
            decimal = decimal + dec * pow(2, i)
            binary1 = binary1 // 10
            i += 1
        print(" Binary", binary, "is Decimal", decimal)
        restart()
    
    if inp == 2:
        decimal = input(" DECIMAL_NUMBER>")
        arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for value in decimal:
            if value not in arr:
                print(" ERROR: Input", decimal, "is NOT an octal number")
                restart()
        decimal = int(decimal)
        
        binary = bin(decimal).replace("0b", "")
        print(" Decimal", decimal, "is Binary", binary)
        restart()
    
    if inp == 3:
        octal = input(" OCTAL-STR>")
        arr = ["0", "1", "2", "3", "4", "5", "6", "7"]
        for value in octal:
            if value not in arr:
                print(" ERROR: Input", octal, "is NOT an octal number")
                restart()
        octal = int(octal)
        octal1 = octal
        decimal_value = 0
        base = 1
        while octal1:
            last_digit = octal1 % 10
            octal1 = octal1 // 10
            decimal_value += last_digit * base
            base = base * 8
        print(" Octal", octal, "is Decimal", decimal_value)
        restart()
    
    if inp == 4:
        decimal = input(" DECIMAL_NUMBER>")
        arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for value in decimal:
            if value not in arr:
                print(" ERROR: Input", decimal,"is NOT an octal number")
                restart()
        decimal = int(decimal)
        
        octal = oct(decimal).replace("0o", "")
        print(" Decimal", decimal, "is octal", octal)
        restart()
    
    if inp == 5:
        print(" Goodbye!")
        print(" =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        exit()
    else:
        print("ERROR: Please choose from [1 - 5]")
        Main()
Main()
