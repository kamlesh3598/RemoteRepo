import sample
import csv
import os

headers = sample.headers  # employee headers/fields names

path = r"C:\Users\ADMIN\pycharmprojects\PythonModules\input"  # input folder absolute path


# file for read emp.csv file data
def readFile():
    with open(file=sample.client_file_name, mode='r') as file:
        data = csv.DictReader(file)
        data = list(data)
        return data


# file for dump emp.csv new file data into input folder
def createFile(data):
    with open(file=os.path.join(path, sample.client_file_name), mode='x', newline='') as file:
        write = csv.DictWriter(file, fieldnames=headers)
        write.writeheader()
        write.writerows(data)


if __name__ == 'client_side':
    # send a file in input folder
    createFile(readFile())  # call the function to read data from emp.csv file and dump into input folder

    # Delete the emp.csv file after sent to the output folder
    os.remove(sample.client_file_name)
