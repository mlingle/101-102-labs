#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   time: 45min
def union(list1,list2):
    newList = [eachElement for eachElement in list1]
    for eachElement in list2:
        if not eachElement in newList:
            newList.append(eachElement)
    return newList
