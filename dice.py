#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 9 - Lab A - Rolling a Die
#   References: Colin TA
#   Time: 20 minutes
import random
print("Input the number of rolls to make:")
N=int(input("NUMBER>"))
print("Input the seed for the random number generator:")
S=int(input("SEED>"))      
random.seed(S)
list1=[]
for i in range(N):
    d=random.randint(1,6)
    list1.append(d)
print("Your", N,"rolls follow")
print("OUTPUT 1 occured", list1.count(1), "times")
print("OUTPUT 2 occured", list1.count(2), "times")
print("OUTPUT 3 occured", list1.count(3), "times")
print("OUTPUT 4 occured", list1.count(4), "times")
print("OUTPUT 5 occured", list1.count(5), "times")
print("OUTPUT 6 occured", list1.count(6), "times")
