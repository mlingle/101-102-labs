#   Matthew Lingle
#  ​ CSCI 101 – Section B
#   Python Lab 11
#   References: CASA mines
#   Time: 75 minutes
import csv
def read_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        list=[]
        myFileReader=csv.reader(f, delimiter= ',')
        for rows in myFileReader:
            list.append(rows)
        return list
rows = read_csv("aurora_police.csv")
print(rows[0])
def stops_by_race(rows, subject_race):
    count=0
    for row in rows:
        if subject_race=='white' and row[8]=='white':
            count+=1
        if subject_race=='asian' and row[8]=='asian/pacific islander':
            count+=1
        if subject_race=='ALL':
            count+=1
    return count
def stops_by_sex(rows, subject_sex):
    count=0
    for row in rows:
        if subject_sex=='male' and row[9]=='male':
            count+=1
        if subject_sex=='female' and row[9]=='female':
            count+=1
        if subject_sex=='ALL':
            count+=1
    return count
#The data on census.gov was similar to the data from the code.
#Whites were a little of 60% on census.gov and they were 65% from the code.
#the other races were about the same percentages.
            
    
             
    
