# THIS SCRIPT USES PYTHON FAKER TO CREATE A BUNCH OF USERS WITH REAL DATA 
# AND THEN SAVES INTO A CSV FILE.
import csv
import random
from faker import Faker

# THE VAR 'USERS' DEFINES HOW MANY USERS YOU WANT TO CREATE. I SET IT TO 1000 LIKE IT WAS SUGGESTED
# BUT FEEL FREE TO CHOSE ANOTHER VALUE. 
USERS = 1000
fake = Faker()

# THIS FUNCTION IS RESPONSABLE FOR CREATE THE CSV FILE WITH ALL THE INFORMATION WE ARE GETTING FROM
# PYTHONS'S FAKER LIBRARY.
def create_csv_file():
    with open('./fakeusers.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'address', 'city', 'state',
                      'country', 'uid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        #THE VAR 'AUX' ITS AN ARBITRARY NUMBER SET TO HELP US DEFINE AN UID TO EACH USER.
        #TO CREATE MORE USERS AFTER RUNING THIS SCRIPT ONCE, PLEASE CHANGE THE AUX VALUE SO WE CAN ADD
        #USERS INTO LDAP SERVER WITHOUT PROBLEM.
        aux=9999

        for i in range(USERS):
            aux = aux+1
            writer.writerow(
                {
                    'first_name': fake.name(),
                    'last_name': fake.name(),
                    'email': fake.email(),
                    'address': fake.street_address(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'country': fake.country(),
                    'uid': int(aux)
                }
            )



if __name__ == '__main__':    
    create_csv_file()
    
