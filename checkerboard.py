#   Matthew Lingle
#   CSCI 102 – Section A
#   Week 7 - Lab A - Checkerboard
#   References: None
#   Time: 45 minutes

print("What is the length of the sides of the checkerboard?")
length = int(input("length>"))

mat = [[0 for i in range(length)] for i in range(length)]


print("What are the strings with which to pattern it?")
first = input("FIRST> ")
second = input("SECOND> ")


pattern = [first,second]

pos = 0


for i in range(length):
    for j in range(length):
        
        mat[i][j] = pattern[pos]
        pos = (pos+1)%2 

print("A checkerboard with side length 8, first string is black, and second string is white is:")
print (mat)
