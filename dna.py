#   Tracy Camp
#  ​CSCI 101 – Section B
#   Python Lab 6
#   References: None
#   Time: 45 minutes
print("Enter a DNA String (of length < 1000):")
print("STRING>")
s=input()
f=0
for i in s:
    if i not in "ACGT":
        print("Invalid string is provided")
        f=1
        break 
if f!=1:
    l=list(s)
print("OUTPUT", l.count("A"),l.count("C"),l.count("G"),l.count("T"),sep=" ")
res=""
for i in l:
    if i=='T':
        res=res+'U'
else:
    res+=i
print("OUTPUT", res)
