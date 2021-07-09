# This script is designed to take SQL response times from a log, export them to \
# a CSV and display a small bar chart. As with all automation scripts, be aware \
# there is a chance the script may not work 100% accurately. It's a good idea \
# to verify the data from this scripts output should you decide to use it.

# CSV export will save to the location the script is run from.

# Import libraries
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import csv

#Path to log file
log_path = ""
transactions = {}
log_values = []

def find_transactions():
    text = open(log_path, "r")
    counter = 0
    for line in text:
        if line.find('ms in transaction') != -1:
            if line.find('Delete took ') != -1 or line.find('reader took ') != -1:
                transaction_start = line.find(' took ') - 14
                transaction_end = line.find('ms in transaction') + 2
            else:
                transaction_start = line.find('query took ') - 13
                transaction_end = line.find('ms in transaction') + 2
            location_start = line.find(' in transaction ') + 16
            transaction = str(line[transaction_start:transaction_end])
            log_values.append(["Log Line: {c}, Transaction Time: {t}, Transaction Info: {i}".format(c=counter, t=transaction, i=line[location_start:])])
            update = {counter: transaction}
            transactions.update(update)
        counter += 1

def create_output():
    a_file = open("ResponseTimeResults.csv", "w")
    writer = csv.writer(a_file)
    writer.writerow(['Log Line', 'Transaction Time', 'Transaction Info'])
    for x in log_values:
        writer.writerow(x)
    a_file.close()

def create_chart():
    values_string = list(transactions.values())
    values = []
    keys = list(transactions.keys())
    for x in values_string:
        slice = x.find('took ')
        values.append((int(x[slice + 5:-2])))
    sns.barplot(x = values, y = keys)
    plt.show()

find_transactions()
create_output()
create_chart()
