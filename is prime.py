#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def is_prime(x):             
    if(x==0 or x==1):
        return False
    for i in range(2,x-1):   
        if (x % i) == 0:     
            return False
    else:                    
        return True
