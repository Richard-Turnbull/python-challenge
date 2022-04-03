#----------------------------------------------------------------------------------------------
# IMPORT MODULES
#----------------------------------------------------------------------------------------------
import os
import csv

#----------------------------------------------------------------------------------------------
# SET EMPTY LISTS FOR REQUIRED VARIABLES
#----------------------------------------------------------------------------------------------
months = []
total = []

#----------------------------------------------------------------------------------------------
# ASSIGN FILEPATH TO VARIABLE, OPEN FILE WITH CSV.READER, THEN SKIP HEADER ROW
#----------------------------------------------------------------------------------------------
# Set csv file location (navigate from where this .py file is saved)
bank_data_csv = os.path.join("Resources", "budget_data.csv")

# Open file using CSV module
with open(bank_data_csv) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     # Skip header row
    csv_header = next(csvreader, None)

#----------------------------------------------------------------------------------------------
# LOOP THROUGH EACH ROW AND APPEND SOURCE DATA VALUES TO LISTS CONTAINED IN THE VARIABLES
#----------------------------------------------------------------------------------------------
     # ForLoop: loop through each row
    for row in csvreader:
         
          # Append first column (date) to months list
        months.append(row[0])
          # Append second column (profit/loss) to total list
        total.append(int(row[1]))

#----------------------------------------------------------------------------------------------
# CALCULATE CHANGE (INCREASE/DECREASE) BETWEEN EACH MONTH AND STOR IN VARIABLE
#----------------------------------------------------------------------------------------------
monthly_change = [y-x for x, y in zip(total[:-1], total[1:])]

#----------------------------------------------------------------------------------------------
# FIND WHICH MONTH HAD LARGEST INCREASE IN PROFITS
#----------------------------------------------------------------------------------------------
# iterate through "lge_increase" list
for a, b in enumerate(monthly_change):
     # Check if the value for that iteration is equal to the max value in the "lge_increase" list
     if b == max(monthly_change):
          # if the value was equal to the max, assign the iteration (index) number to a new variable "months_max_index"
          months_max_index = (a + 1)

# iterate throught the "months" list to the same iteration (index) you defined in the "months_max_index" variable above
for c in [months[months_max_index]]:
     # assign the value from the same iteration in the "months" list to a new variable "Lge_increase_month"
     lge_increase_month = c

#----------------------------------------------------------------------------------------------
# FIND WHICH MONTH HAD LARGEST DECREASE IN PROFITS
#----------------------------------------------------------------------------------------------
# iterate through "lge_decrease" list
for d, e in enumerate(monthly_change):
     # Check if the value for that iteration is equal to the min value in the "lge_decrease" list
     if e == min(monthly_change):
          # if the value was equal to the min, assign the iteration (index) number to a new variable "months_min_index"
          months_min_index = (d + 1)

# iterate throught the "months" list to the same iteration (index) you defined in the "months_min_index" variable above
for f in [months[months_min_index]]:
     # assign the value from the same iteration in the "months" list to a new variable "Lge_decrease_month"
     lge_decrease_month = f

#----------------------------------------------------------------------------------------------
# PRINT TABLE TO TERMINAL
#----------------------------------------------------------------------------------------------
print('________________________________________________________')
print('                                    ')
print('Financial Analysis')
print('--------------------------------------------------------')
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(total)}')
print(f'Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}')
print(f'Greatest Increase in Profits: {lge_increase_month} (${max(monthly_change)})')
print(f'Greatest Decrease in Profits: {lge_decrease_month} (${min(monthly_change)})')
print('--------------------------------------------------------')

#----------------------------------------------------------------------------------------------
# WRITE TABLE TO NEW CSV FILE NAMED "OUTPUT"
#----------------------------------------------------------------------------------------------
# Set csv file location (navigate from where this .py file is saved)
output_csv = os.path.join("analysis", "output.csv")

# Open cvs file with write ('w') permissions
with open(output_csv, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to rows
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['--------------------------------------------------------'])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total: ${sum(total)}'])
    csvwriter.writerow([f'Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {lge_increase_month} (${max(monthly_change)})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {lge_decrease_month} (${min(monthly_change)})'])