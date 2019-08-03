import os

import csv

budget_csv = os.path.join("budget_data.csv")
output_path = os.path.join("budget_data_results.csv")

total_months = 0
total_profit = 0
average_change = 0
max_change = 0
min_change = 0
monthly_profits = []
monthly_change = 0
monthly_change_list = []
month_year = []
i = 0

with open(budget_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        monthly_profits.append(int(row[1]))
        i = i + 1
        if i > 1:
            monthly_change = monthly_profits[i - 1] - monthly_profits[i - 2]
            monthly_change_list.append(monthly_change)
            month_year.append(row[0])

    average_change = round(sum(monthly_change_list)/len(monthly_change_list),2)
    max_change = max(monthly_change_list)
    max_change_month = month_year[monthly_change_list.index(max_change)]
    min_change = min(monthly_change_list)
    min_change_month = month_year[monthly_change_list.index(min_change)]

    print("Financial Analysis")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profit))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(max_change_month) + " $" + str(max_change))
    print("Greatest Decrease in Profits: " + str(min_change_month) + " $" + str(min_change))

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months:", total_months])
    csvwriter.writerow(["Total:", "$" + str(total_profit)])
    csvwriter.writerow(["Average Change:", "$" + str(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(max_change_month), "$" + str(max_change)])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(min_change_month), "$" + str(min_change)])