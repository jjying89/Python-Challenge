#import modules
import os
import csv

#find data
election_csv = os.path.join("Resources", "election_data.csv")

#output analysis
election_analysis = os.path.join("Analysis", "analysis.txt")

#define variables & list
totalvotes = 0
votes=[]
candidates=[]


#open csv
with open(election_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    for column in csv_reader:
        votes.append(column[0])
        candidates.append(column[2])


    #find total votes
    totalvotes = len(votes)
    


    #find candidate votes
    khan = candidates.count("Khan")
    correy = candidates.count("Correy")
    li = candidates.count("Li")
    otooley = candidates.count("O'Tooley")

    
    #find candidate voter percentage
    khan_percentage = round((khan/totalvotes)*100)
    correy_percentage = round((correy/totalvotes)*100)
    li_percentage = round((li/totalvotes)*100)
    otooley_percentage = round((otooley/totalvotes)*100)

    

    #find winner
    if khan > correy > li > otooley:
        winner = "khan"
    
    elif correy > khan > li > otooley:
        winnier = "correy"

    elif li > khan > correy > otooley:
        winner = "li"
    
    elif otooley > khan > correy > li:
        winner = "otooley"

    #print results
    print("Election Results")
    print("------------------")
    print("Total Votes: " + str(totalvotes))
    print("------------------")
    print("Khan: " + str(khan_percentage) + "%" + "(" + str(khan) + ")")
    print("Correy: " + str(correy_percentage) + "%" + "(" + str(correy) + ")")
    print("Li: " + str(li_percentage) + "%" + "(" + str(li) + ")")
    print("Khan: " + str(otooley_percentage) + "%" + "(" + str(otooley) + ")")
    print("------------------")
    print("Winner " + str(winner))

with open(election_analysis, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Votes: " + str(totalvotes) + "\n")
    txtfile.write("------------------\n")
    txtfile.write("Khan: " + str(khan_percentage) + "%" + "(" + str(khan) + ")" + "\n")
    txtfile.write("Correy: " + str(correy_percentage) + "%" + "(" + str(correy) + ")" + "\n")
    txtfile.write("Li: " + str(li_percentage) + "%" + "(" + str(li) + ")" + "\n")
    txtfile.write("Khan: " + str(otooley_percentage) + "%" + "(" + str(otooley) + ")" + "\n")
    txtfile.write("------------------\n")
    txtfile.write("Winner: " + str.upper(winner) + "\n")


