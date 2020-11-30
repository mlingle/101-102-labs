#   Matthew Lingle
#  ​ CSCI 101 – Section B
#   Python Lab 9
#   References: 
#   Time: 45 minutes
print("Input the string to encrypt:")
a = str(input("STRING> "))
cipher = ""
for letter in a:
    if not letter.isalpha():
        cipher += letter
        continue
    if letter < 'm':
        if letter.isupper():
            cipher += chr(ord(letter) + (25 -(2*(ord(letter)-65))))
        else:
            cipher += chr(ord(letter) + (25 -(2*(ord(letter)-97))))
    else:
        if letter.isupper():
            cipher += chr(ord(letter) - ((2*(ord(letter)-65)- 25)))
        else:
            cipher += chr(ord(letter) - ((2*(ord(letter)-97)- 25)))
print("Your Atbash cipher is:", cipher)                         
print("OUTPUT", cipher)   
