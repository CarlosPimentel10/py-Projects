# Working with csv files; creating and editing

import csv
"""
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_id', 'product_id', 'product_price'])
    writer.writerow([1000, 1, 10])
    writer.writerow([1001, 2, 15])
"""
with open('data.csv') as file:
    reader = csv.reader(file)
#    print(list(reader))
    for row in reader:
        print(row)
