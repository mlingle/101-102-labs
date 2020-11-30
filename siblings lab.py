#Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 3 - Lab B - Three Siblings
#   References: None
#   Time: 40 minutes

number = int(input("Enter a positive number: "))
print("The sibling(s) who will work with the number follow:")
if number % 2 == 1:
    print("Output Jimmy")
    
if number > 10 and number <= 100:
    print("Output Jared")
    
total = int(number/10)+number%10

if number > 9 and number < 100 and (total == 6 or total == 8):
    print("Output Josephine")
