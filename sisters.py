#   Matthew Lingle
#   ​CSCI 102 – Section B
#   Week 6 - Lab B - Users
#   References: None
#   Time: 60 minutes

print("Enter the users separated by commas:")
users=input("USERS>")
users=users.split(",")
for i in range(len(users)):
    users[i]=users[i].lower()
print("\nYou entered the following users:")
print(users)
duplicate=[]
print("The Unique Users and their occurences are:")
for user in users:
    if(user not in duplicate):
        duplicate.append(user)
        duplicate.append(users.count(user))
print(duplicate)
