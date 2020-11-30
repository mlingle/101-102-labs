#   Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 6 - Lab A - Lost Marbles
#   References: None
#   Time: 65 minutes

print('Enter a string of X\'s and O\'s:') 
strIn = input('Marbles> ') 

marbleLocations = [] 
indx = 0 

for marble in strIn: 
  
  if(marble == 'O'): 
    marbleLocations.append(indx) 
    
  indx = indx + 1 


print('Hi Lazy, I found your marbles for you. They are at', marbleLocations)
print('Your Marbles are at the following indices:')
print('OUTPUT ', marbleLocations)
