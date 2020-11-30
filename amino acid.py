#   Matthew Lingle
#   ​CSCI 102 – Section C
#   Week 4 - Lab B - Amino Acids
#   References: None
#   Time: 55 minutes
print("Input the chemical elements of the amino acid:")
c = int(input("CARBON>"))
h = int(input("HYDROGEN>"))
n = int(input("NITROGEN>"))
o = int(input("OXYGEN>"))
s = int(input("SULFUR>"))

if c==3:
    if s==1:
        acid_name = "Cysteine"
    else:
        acid_name = "Alanine"

elif c==4:
    acid_name = "Asparagine"

elif c==5:
    acid_name = "Glutamine"

else:
    if h==14:
     acid_name = "Arginine"

    else:
        acid_name = "Histidine"

formula = "C-" + str(c) + "H-" + str(h) + "N-" + str(n) + "O-" + str(o) + "S-" + str(s)

print("The amino acid for {} is {}" .format(formula, acid_name))

print("OUTPUT {}" .format(formula))

print("OUTPUT {}" .format(acid_name))
      
