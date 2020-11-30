#   Matthew Lingle
#  ​CSCI 101 – Section B
#   Python Lab 4
#   References: None
#   Time: 65 minutes

filingStatus=input("Enter filing status (single or joint) : ")
print("STATUS>", filingStatus)
income=float(input("Enter income : "))
print("INCOME>", income)

if  filingStatus.lower()=="single":
    tax=0 
    if(income<=9325):
        tax=income*0.1 
    elif(income>=9326 and income<=37950):
        tax=9325*0.1+(income-9325)*0.15 
    elif (income >= 37951 and income <=91900 ):
        tax = 9325 * 0.1 + (37950 - 9325) * 0.15 +(income-37950)*0.25 
    elif (income >= 91901 and income <=191650 ):
        tax = 9325 * 0.1 + (37950 - 9325) * 0.15 + (91900 - 37950) * 0.25+(income-91900)*0.28  
    elif (income >= 191651 and income <= 416900):
        tax = 9325 * 0.1 + (37950 - 9325) * 0.15 + (91900 - 37950) * 0.25 + (191650 - 91900) * 0.28+(income-191650)*0.33  
    elif (income >= 416901 and income <= 418400):
        tax = 9325 * 0.1 + (37950 - 9325) * 0.15 + (91900 - 37950) * 0.25 + (191650 - 91900) * 0.28+(416900-191650)*0.33+(income-416900)*0.35  
    elif (income >= 418401):
        tax = 9325 * 0.1 + (37950 - 9325) * 0.15 + (91900 - 37950) * 0.25 + (191650 - 91900) * 0.28 + (
                    416900 - 191650) * 0.33 + (418400 - 416900) * 0.35 +(income-418400)*0.396 
    print("The tax owed by this person with $",income,"is $",tax)
    print("OUTPUT", tax)
elif filingStatus.lower()=="joint":
    tax = 0  
    if (income <= 18650):
        tax = income * 0.1  
    elif (income >= 18651 and income <= 75900):
        tax = 18650 * 0.1 + (income - 18650) * 0.15  
    elif (income >= 75901 and income <= 153100):
        tax = 18650 * 0.1 + (75900 - 18650) * 0.15 + (income - 75900) * 0.25  
    elif (income >= 153101 and income <= 233350):
        tax = 18650 * 0.1 + (75900 - 18650) * 0.15 + (153100 - 75900) * 0.25 +(income-153100)*0.28 
    elif (income >= 233351 and income <= 416900):
        tax = 18650 * 0.1 + (75900 - 18650) * 0.15 + (153100 - 75900) * 0.25 + (
                    233350 - 153100) * 0.28+(income-233350)*0.33  
    elif (income >= 416901 and income <= 470700):
        tax = 18650 * 0.1 + (75900 - 18650) * 0.15 + (153100 - 75900) * 0.25 + (
                233350 - 153100) * 0.28 + (416900 - 233350) * 0.33 +(income-416900)*0.35 
    elif (income >= 470701):
        tax = 18650 * 0.1 + (75900 - 18650) * 0.15 + (153100 - 75900) * 0.25 + (
                233350 - 153100) * 0.28 + (416900 - 233350) * 0.33 + (470700 - 416900) * 0.35 +(income-470700)*0.396 # calculate tax of 39..6%
    print("The tax owed by this person with $", income, "is $", tax)
    print("OUTPUT", tax)
else:#when invalid filling status is entered
    print("Enter valid single or joint filling status")

print("the percent of income paid in taxes is %", ((tax/income)*100))
print("OUTPUT", ((tax/income)*100))
