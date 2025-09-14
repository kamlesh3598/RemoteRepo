import csv
import faker as fk

client_file_name = 'emp.csv'  # file sent by client on daily basis
headers = ['eid', 'ename', 'ecity', 'esal']  # headers of client files

# fake module
fake = fk.Faker('en_IN')


def createEmployees():
    with open(file=client_file_name, mode='a+', newline="") as emp_file:
        write = csv.DictWriter(emp_file, fieldnames=headers)
        write.writeheader()
        cities = ['Pune', 'Mumbai', 'Chennai', 'Delhi', 'Bangalore']
        i = 0
        while i < 5:
            eid, ename, ecity, esal = [fake.random_int(100, 200), fake.name(), fake.random_element(elements=cities),
                                       fake.random_int(min=1000, max=50000)]
            write.writerows(
                [{'eid': eid, 'ename': ename, 'ecity': ecity, 'esal': esal}, ]
            )

            i += 1


if __name__ == 'sample':
    createEmployees()  # call the function to create employee data in emp.csv
