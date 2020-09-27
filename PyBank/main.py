#import modules
import os
import csv

#find file
budget_data = os.path.join('Resources','budget_data.csv')

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
totalmonths= len(list(reader))-1 #-1 for the header
print(totalmonths)


#find total profit/losses
file = open(budget_data)
reader = csv.reader(file)
totalprofit= sum(list(reader.(0,2)))
print(totalprofit)



    
    
months = len(list(budget_data))
print(months)


#find total months
with open(budgetreader, 'r') as f:
    reader = csv.reader(f)
    first_col_len = len(next(zip(*reader)))







# Specify the file to write to
budget_analysis = os.path.join('Analysis', 'analysis.txt')

with open(budget_analysis, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the second row and etc
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Total Months: '])
    csvwriter.writerow(['Average Change: '])
    csvwriter.writerow(['Greatest Increase in Profits: '])
    csvwriter.writerow(['Greatest Decrease in Profits: '])








