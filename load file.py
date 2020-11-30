#   Matthew Lingle
#   CSCI 102 – Section C
#   Week 12 - Utility using Git and Incremental Development
#   References: Jack
#   Time: 45 minutes
def load_file(file_name):
    with open(file_name,"r") as file:
        return file.readlines()
    
