#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def update_string(string1, string2,index):
    if index < len(string1):
        newstring=""
        for i in range(len(string1)):
            if i==index:
                newstring += string2
            else:
                newstring += string1[i]
        print(newstring)
    else:
        print("given index[] not found in []".format(index,string1)
    
