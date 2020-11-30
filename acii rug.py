#   Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 5 - Lab A - ASCII Carpet
#   References: no one
#   Time: 15 minutes

def make_rug(width,height,c) :
    for h in range(height) :
        for w in range(width) :
            print(c, end = " ") 
            print("\n")



wid = int(input("Enter the Width of the Rug(1 <= width <= 50): "))                 
hig = int(input("Enter the Height of the Rug(1 <= width <= 50): "))      
ch = str(input("Enter the ASCII Character you want to print on the Rug: "))
print("A", wid,"x",hig ,"rug with character", ch ,"will look like:")
ch.strip()                                   
make_rug(wid,hig,ch)
