#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def score_finder(playerNames,playerScores,string):
    found = False
    for i in range(len(playerNames)):
        if playerNames[i].lower() == string.lower():
            print("OUTPUT",string,"got a score of",playerScores[i])
            found = True
    if not found:
        print("OUTPUT player not found")
