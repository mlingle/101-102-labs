#   Matthew Lingle
#  ​ CSCI 101 – Section B
#   Python Lab 7
#   References: None
#   Time: 60 minutes

def check_if_watered(Field, R, C):
   for i in range(R):
       for j in range(C):                                               
           if Field[i][j] == 'w':                                       
               if j+1 < C and Field[i][j+1] == 'c':                   
                   Field[i][j+1] = 'wc'
               if j-1 >= 0 and Field[i][j-1] == 'c':
                   Field[i][j-1] = 'wc'
               if i+1 < R and Field[i+1][j] == 'c':
                   Field[i+1][j] = 'wc'
               if i-1 >= 0 and Field[i-1][j] == 'c':
                   Field[i-1][j] = 'wc'
               if i-1 >= 0 and j-1 >= 0 and Field[i-1][j-1] == 'c':
                   Field[i-1][j-1] = 'wc'                  
               if i-1 >= 0 and j+1 < C and Field[i-1][j+1] == 'c':
                   Field[i-1][j+1] = 'wc'      
               if i+1 < R and j-1 >= 0 and Field[i+1][j-1] == 'c':
                   Field[i+1][j-1] = 'wc'
               if i+1 < R and j+1 < C and Field[i+1][j+1] == 'c':
                   Field[i+1][j+1] = 'wc'
   output = []
   for i in range(R):
       for j in range(C):                                               
           if Field[i][j] == 'c':
               output.append((i, j))
   return output                                                       

def main():
   print("Input the number of rows and columns in the crop field:")
   R = int(input("ROWS> "))                                           
   C = int(input("COLUMNS> "))
   print("Input each row of the crop field.")
  
   Field = []                                                           
   for i in range(R):                                                   
       rowString = input("ROW" + str(i) + "> ")
       row = rowString.split()                                           
       Field.append(row)                                               

   val = check_if_watered(Field, R, C)                                   
   if val == []:                                                       
       print("All crops are watered!")
       print("Output True")
   else:                                                               
        print("Not all the crops are watered!")
        print("Output False")
        print("The following crops are not watered: ")
        print("Output", val)

main()


