#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def find_word_count(listOfStrings,string):
    count = 0
    for eachValue in listOfStrings:
        words = eachValue.split(" ")
        for eachWord in words:
            if string == eachWord:
                count += 1
    return count
