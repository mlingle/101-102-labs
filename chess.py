#   Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 4 - Lab A - Missing Chess Pieces
#   References: None
#   Time: 25 minutes
print("Please enter the number of white chess pieces that you have of each type:")
King=(int)(input("KINGS>"))
Queen=(int)(input("QUEENS>")) 
Rooks=(int)(input("ROOKS>")) 
Bishops=(int)(input("BISHOPS>")) 
Knights=(int)(input("KNIGHTS>")) 
Pawns=(int)(input("PAWNS>")) 
print("The output below provides the number of each type you have (over or under):")
print("OUTPUT", 1-King,1-Queen,2-Rooks,2-Bishops,2-Knights,8-Pawns)
