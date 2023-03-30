import os
import csv

#sets path for data file
budget_csv = os.path.join("Resources", "budget_data.csv")

#store data in separate lists
months = []
profit_losses = []
monthly_change = []

#split on comma (make two columns)
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip first row
    next(csvreader)

    #add column 1 into its own list, add column 2 into its own list
    for row in csvreader:
        months.append(row[0])
        profit_losses.append((int(row[1])))

    #calculate monthly change (next month - current month) and store to list
    for monthly_profit in range(len(profit_losses)-1):
        currentMonthProfit = monthly_profit
        NextMonthProfit = monthly_profit + 1
        monthly_change.append(profit_losses[NextMonthProfit] - profit_losses[currentMonthProfit])

    #total number of months in data set
    totalMonths = len(months)
    #sum of profit/Loss column in data set
    totalProfitLoss = sum(profit_losses)
    
    #total of month to month Profit/Loss list
    totalMonthlyChange = sum(monthly_change)
    #average of month to month change
    averageProfitLoss = round(totalMonthlyChange/len(monthly_change),2)
    #highest and lowest monthly changes
    maxMonthlyChange = max(monthly_change)
    minMonthlyChange = min(monthly_change)

    #find index of month associated to Max/Min Changes
    maxChangeMonthindex = monthly_change.index(max(monthly_change))+1
    maxChangeMonth = months[maxChangeMonthindex]
    minChangeMonthindex = monthly_change.index(min(monthly_change))+1
    minChangeMonth = months[minChangeMonthindex]

#print financial analysis to terminal
print("\n\nFinancial Analysis\n\n--------------------------------------------------------")
print(f"Total month : {totalMonths}")
print(f"Total : ${totalProfitLoss}")
print(f"Average Change : ${averageProfitLoss}")
print(f"Greatest Increase in Profits : {maxChangeMonth} (${maxMonthlyChange})")
print(f"Greatest Decrease in Profits : {minChangeMonth} (${minMonthlyChange})")

#sets path for analysis doc output
output_file = os.path.join("analysis","budget_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:

    #writes financial analysis to nex txt file
    datafile.write("Financial Analysis\n\n--------------------------------------------------------\n\n")
    datafile.write(f"Total months : {totalMonths}\n")
    datafile.write(f"Total : ${totalProfitLoss}\n")
    datafile.write(f"Average Change : ${averageProfitLoss}\n")
    datafile.write(f"Greatest Increase in Profits : {maxChangeMonth} (${maxMonthlyChange})\n")
    datafile.write(f"Greatest Decrease in Profits : {minChangeMonth} (${minMonthlyChange})")