import csv


def csv_writer(path, data):
    with open(path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data)
