import csv

def write_to_file(first_name, last_name, email, company):
    with open('data.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'company']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': first_name, 'last_name': last_name, 'email': email, 'company': company})

