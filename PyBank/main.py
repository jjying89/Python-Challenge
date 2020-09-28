#import modules
import os
import csv

#find file
budget_data = os.path.join('Resources','budget_data.csv')

#set analysis variables
totalmonths=[]
totalprofit=[]
avgchange=[]
greatestincrease=[]
greatestdecrease=[]


#find total p&l
with open(budget_data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #skip header row
        next(csvreader, None) 

        # Gets number of rows in csv
        data=list(csvreader)

        row_count = len(data)
        
        print(row_count)


#read csvfile
with open(budget_data, 'r') as csvfile:

    budgetreader = csv.reader(csvfile, delimiter=',')

    print(budgetreader)

    #read header
    csv_header = next(budgetreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in budgetreader:
        print(row)







#find total months  
file = open(budget_data)
reader = csv.reader(file)
next(reader)#skip header
totalmonths= len(list(reader))
print(totalmonths)


# Specify the file to write to
budget_analysis = os.path.join('Analysis', 'analysis.txt')

with open(budget_analysis, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the second row and etc
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Total Months:'+ totalmonths])
    csvwriter.writerow(['Average Change: '])
    csvwriter.writerow(['Greatest Increase in Profits: '])
    csvwriter.writerow(['Greatest Decrease in Profits: '])


#find total profit/losses
cr = csv.reader(open(budget_data,"rb"))
cr.next() # to skip the header 
#error//       print sum(int(x[2])) for x in cr




with open(budget_data, "rb") as csv_file:
    reader = csv.DictReader(csv_file)
    total = sum(float(row["Profit/Losses"]) for row in reader)
print(total)



with open(budget_data) as fin:
    fin.next()
    total = sum(int(r[1]) for r in csv.reader(fin))
    print(total)


    
#find total months FAILED    
months = len(list(budget_data))
print(months)


#find total months FAILED
with open(budgetreader, 'r') as f:
    reader = csv.reader(f)
    first_col_len = len(next(zip(*reader)))
















