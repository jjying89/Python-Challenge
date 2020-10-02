#import modules
import os
import csv

#find data
budget_data = os.path.join('Resources','budget_data.csv')

#output analysis
budget_analysis = os.path.join("Analysis", "analysis.txt")

#set analysis variables/list
totalmonths=0
totalprofit=0
date=[]
profitandlosses=[]


#open csv
with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    next(csv_reader)

    #append list
    for column in csv_reader:
        date.append(column[0])
        profitandlosses.append(column[1])

    #find total months
    totalmonths = len(date)
    print(totalmonths)
    
    #find total profit
    profit = map(int, profitandlosses)
    totalprofit = sum(profit)
    print(totalprofit)

#find average profit
#set additional variables/list
monthlychange = 0
totalchange=0
averageprofit = 0
i = 0
monthlychanges = []
    
for i in range(len(profitandlosses)-1):
    monthlychange = int(profitandlosses[i+1]) - int(profitandlosses[(i)])   
    monthlychanges.append(monthlychange)            
    totalchange = totalchange + monthlychange
    averageprofit = totalchange / (totalmonths-1) #dividing by 1 month less
    formatted_averageprofit = "{:.2f}".format(averageprofit) #make it 2 decimal places

    #finding greatest increase
    gincrease = max(monthlychanges)
    g_index = monthlychanges.index(gincrease)
    gincrease_date = date[g_index+1] #plus 1 to get correct month

    #finding greatest decrease
    gdecrease = min(monthlychanges)
    g_index = monthlychanges.index(gdecrease)
    gdecrease_date = date[g_index+1] #plus 1 to get correct month

#print results
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(totalprofit))
print(f"Average Change: ${formatted_averageprofit}")
print(f"Greatest Increase in Profits: {gincrease_date}({gincrease})")
print(f"Greatest Decrease in Profits: {gdecrease_date}({gdecrease})")

#output results to analysis
with open(budget_analysis, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months: " + str(totalmonths) +"\n")
    txtfile.write("Total: $" + str(totalprofit) + "\n")
    txtfile.write(f"Average Change: ${formatted_averageprofit}\n")
    txtfile.write(f"Greatest Increase in Profits: {gincrease_date}({gincrease})\n")
    txtfile.write(f"Greatest Decrease in Profits: {gdecrease_date}({gdecrease})\n")


