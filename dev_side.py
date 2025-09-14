import client_side as client
import csv
import os

# client sent file name
client_file = client.sample.client_file_name

# Path for send the file by client and read it
output_path = r"C:\Users\ADMIN\pycharmprojects\PythonModules\output"

# Path for Generate the employee data using employee city and store in cities csv files
input_path = r"C:\Users\ADMIN\pycharmprojects\PythonModules\input"

# process path to store employee csv file after delete
process_path = r"C:\Users\ADMIN\pycharmprojects\PythonModules\process"

# if client sent the duplicates data in first file then we need to find and remove duplicates data (first time file send by client)
unique_ids_cities = []
unique_ids_process = []


def readFile(fp):
    read_employee_data = csv.DictReader(fp)
    for employee in read_employee_data:
        dataProcess(employee)  # call the function here for create city wise data


def createData(data):
    # to store employee data as per employee city
    city = data['ecity']  # Employee city name
    city_csv_file = '{}.csv'.format(city)  # input files

    with open(file=os.path.join(output_path, city_csv_file), mode='a', newline='') as output_file:
        write = csv.DictWriter(output_file, fieldnames=client.headers)
        # store employee data
        write.writerow(data)


def dataProcess(data):
    if not os.listdir(process_path):
        ids = data['eid']
        if ids not in unique_ids_cities:
            createData(data)
            unique_ids_cities.append(ids)

    else:
        file = open(os.path.join(process_path, client_file), mode='r')
        read = csv.DictReader(file)
        process_file_data = list(read)
        eid = [val for key, val in data.items()][0]
        old_ids = [my_dict['eid'] for my_dict in process_file_data]
        if eid not in old_ids:
            createData(data)
        file.close()


if __name__ == '__main__':
    with open(file=os.path.join(input_path, client_file), mode="r") as input_file:  # output file path

        readFile(input_file)  # call the function read data

        # read employee data
        input_file.seek(0)
        read_new = csv.DictReader(input_file)
        new_data = list(read_new)

        # write data in process folder created employee emp.csv file
        if os.listdir(process_path):
            process_file = open(file=os.path.join(process_path, client_file), mode='r+',
                                newline='')  # process file path
            read_old = csv.DictReader(process_file)
            old_data = [my_dict['eid'] for my_dict in list(read_old)]
            for my_dict in new_data:
                if my_dict['eid'] not in old_data:
                    write = csv.DictWriter(process_file, fieldnames=client.headers)
                    write.writerow(my_dict)
        else:
            # store the file in process directory
            process_file = open(file=os.path.join(process_path, client_file), mode='a', newline='')  # process file path
            write = csv.DictWriter(process_file, fieldnames=client.headers)
            write.writeheader()
            for my_dict in new_data:
                if my_dict['eid'] not in unique_ids_process:
                    write.writerow(my_dict)
                    unique_ids_process.append(my_dict['eid'])

        process_file.close()

    # remove the employee csv file send by client
    os.remove(os.path.join(input_path, client_file))
