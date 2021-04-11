import os
import csv

# Create empty lists for each column data
month_year = []
profit_loss = []

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')


    
with open(budget_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Loop through csv rows and add date and profit/loss data to empty lists
    for row in csvreader:
        month_year.append(row[0])
        profit_loss.append(int(row[1]))

    # Zip and together created lists and the initialize dictionary
    zip_list = zip(month_year, profit_loss)
    list_dict = dict(zip_list) 
    
    # Calculate # of Months
    months = len(month_year)   

    # Calculate net total
    net_total = sum(profit_loss)

    # Calculate average changes
    average = round((net_total / int(months)), 2)

    # Find Greatest Increase
    highest = max(profit_loss)

    # Find Greaest Decrease
    lowest = min(profit_loss)

    # Loop through dictionary to find corresponding date for highest and lowest
    for date, budget in list_dict.items():
        if budget == highest: 
            greatest_increase = str(date + " ($"  + str(highest) + ")")
        
        if budget == lowest:
            greatest_decrease = str(date + " ($"  + str(lowest) + ")")

    
    stdout = open('Resources/results.txt', 'w')
    # Print findings  
    print(f"Financial Analysis")
    print(f"_____________________________")
    print(f"Total Months: {months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average}")     
    print(f"Greatest Increase in Profits: {greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease}")
    stdout.close()