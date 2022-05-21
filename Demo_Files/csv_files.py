import csv

def add_user(fname,lname):
    with open('users.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([fname,lname])

        