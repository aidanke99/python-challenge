import os
import csv

# directing which csv the code should pull from

budget_data_csv = os.path.join(" .. ", "Resources", "budget_data.csv")
budget_file = budget_data_csv

# calculating the total number of rows in csv file to dtermine the total number of months

def sum_rows(budget_file):
    count = 0
    with open(budget_data_csv, 'r') as budget_file:
        csvreader = csv.reader(budget_file)
        for row in csvreader:
            count += 1
    return count
result = sum_rows(budget_file) - 1
print(result)

# calculating the sum of total profit/losses throughout 86 months

def sum_value_in_csv(budget_file):
    total_sum = 0

    with open(budget_file, 'r') as budget_file:
        csv_reader = csv.reader(budget_file)

        next(csv_reader)

        for row in csv_reader:
            value = float(row[1])
# need absolute value to calculate the total changes, and not the net value
            total_sum = total_sum + abs(value)

    return total_sum

total_sum = sum_value_in_csv(budget_file)
print("total sum is", total_sum)

# find net value, to calculate the average monthly movement

def sum_netvalue_in_csv(budget_file):
    total_sum = 0

    with open(budget_file, 'r') as budget_file:
        csv_reader = csv.reader(budget_file)

        next(csv_reader)

        for row in csv_reader:
            value = float(row[1])
            total_sum = total_sum + value

    return total_sum

total_sum = sum_netvalue_in_csv(budget_file)
avg_movement = total_sum / 86
print("Average monthly movement is", avg_movement)

# use max value function to determine the month with the largest profit

def find_max_in_csv(budget_file):
    max_value = 0

    with open(budget_data_csv, 'r') as budget_file:
        csv_reader =  csv.reader(budget_file)

        next(csv_reader, None)

        for row in csv_reader:
            value = float(row[1])

            if max_value is None or value > max_value:
                max_value = value

    return max_value
filename = budget_data_csv
max_value = find_max_in_csv(budget_file)
print("Max return for a month was: ", max_value)

# use min value function to calculate the biggest loss in one month

def find_min_in_csv(budget_file):
    min_value = 0

    with open(budget_data_csv, 'r') as budget_file:
        csv_reader =  csv.reader(budget_file)

        next(csv_reader)

        for row in csv_reader:
            value = float(row[1])

            if min_value is None or value < min_value:
                min_value = value

    return min_value
filename = budget_data_csv
min_value = find_min_in_csv(budget_file)
print("Min return for a month was: ", min_value)


