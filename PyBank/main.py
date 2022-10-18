#Dependencies (things needed to run csv function)
import os
import csv

#getting to CSV file and processing it
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    #This creates a custom object (data is processed)
    csvreader = csv.reader(csvfile, delimiter =',')
    #skips the header/the very first row
    next(csvreader)

    #creating main variables
    total_months = []
    net_total = []
    average_change = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

    #creating variables needed for average_change
    current_profit = 0
    previous_profit = 0
    profit_change = 0
    
    #need list for getting greatest increase/decrease month
    profit_change_list = []

    for row in csvreader:
        #counting months
        total_months.append(csvreader)
        
        #adding total
        net_total.append(int(row[1]))
        
        #Calculating average change
        current_profit = int(row[1])
        profit_change = current_profit - previous_profit
        profit_change_list.append(profit_change)
        previous_profit = int(row[1])

        #Getting greatest increase/decrease month through every cycle
        greatest_increase = max(profit_change_list)
        greatest_decrease = min(profit_change_list)
        if greatest_increase == profit_change:
            greatest_increase_month = row[0]
        if greatest_decrease == profit_change:
            greatest_decrease_month = row[0]

#remove the first number (which is 0) in the list to correctly calculate the average change
profit_change_list.pop(0)
average_change = round(sum(profit_change_list)/len(profit_change_list),2)

#Printing results in terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}") 
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")     
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")   

#Exporting results
exportpath = os.path.join("Analysis").replace("\\","/")
with open(exportpath) as exportfile:
    exporttxt = csv.writer(exportfile)
    exporttxt.writerow(["Financial Analysis"])
    exporttxt.writerow(["--------------------------"])
    exporttxt.writerow([f"Total Months: {len(total_months)}"])
    exporttxt.writerow([f"Total: ${net_total}"])
    exporttxt.writerow([f"Average Change: ${average_change}"])
    exporttxt.writerow([f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}"])
    exporttxt.writerow([f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}"])
