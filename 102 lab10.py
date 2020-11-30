#   Matthew Lingle
#  ​ CSCI 102 – Section C
#   Week 10 Lab
#   References: None
#   Time: 45 minutes


with open("formations.csv", "r")as f:
    with open("formations_parse.csv", "w", newline='') as wf:
        reader=csv.reader(f)
        writer=csv.writer(wf)
        next(reader)
        writer.writerow(['depth', 'start', 'depth'])
        row=[]
        row_list[0].split("-")
        start_depth = float(start_depth)
        end_depth = float(end_depth)
        average = round(((start_depth + end_depth)/2),1)
        rows.append([depth,start_depth, end_depth, average,formation])
print("Output formations_parse.csv")        
