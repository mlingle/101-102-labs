#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def intersect(list1,list2):
    newList = []
    for eachElement in list1:
        if eachElement in list2:
            newList.append(eachElement)
    return newList
