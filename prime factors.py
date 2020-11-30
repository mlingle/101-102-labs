#   Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 5 - Lab B - Prime Factors
#   References: no one
#   Time: 15 minutes
print("Enter a positive integer to generate its Prime Factors:")
import math
def primeFactors(n):
    while n % 2 == 0: 
        print (2),
        n = n / 2
        
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0:
            print(i),
            n = n / i

    if n > 2: 
        print(n)
        

n = int(input("INPUT>"))
print("The Prime Factors for the integer", n ,"are:")
primeFactors(n)


