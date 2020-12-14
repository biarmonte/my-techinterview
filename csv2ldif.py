# THIS SCRIPT READS INTO THE CSV FILE WE CREATED WITH 'ADDFAKEUSER.PY' AND THEN CREATES 
# A LDIF FILE WITH THE INFO IT GOT. THE LDIF FILE ITS READY TO BE IMPORTED TO OUR LDAP SERVER.
import csv 
import pandas as pd


def csv2ldif():         

    arquivo_csv=open('./fakeusers.csv', 'r')
    arquivo_ldif=open('./ldifusers.ldif', 'a')

    reader=csv.reader(arquivo_csv, delimiter=',')
    users_qty= len(list(reader))
    
    var1 = 1

    df = pd.read_csv('./fakeusers.csv', header=None, usecols=[0,1,2,3,4,5,6,7])  

    while var1 != users_qty:    
        

        try:
            first_name=df[0][var1]
            last_name=df[1][var1]
            email=df[2][var1]       
            address=df[3][var1]
            city=df[4][var1]
            state=df[5][var1]
            country=df[6][var1]
            uid=df[7][var1]
        except:            
            arquivo_csv.close()
            arquivo_ldif.close()            
        
        arquivo_ldif.write('dn: uid='+uid+',ou=Users,dc=techinterview,dc=com\n')
        arquivo_ldif.write('changetype: add\n')
        arquivo_ldif.write('objectclass: inetOrgPerson\n')
        arquivo_ldif.write('ou: Users\n')
        arquivo_ldif.write('cn: '+first_name+'\n')
        arquivo_ldif.write('sn: '+last_name+'\n')
        arquivo_ldif.write('mail: '+email+'\n')
        arquivo_ldif.write('street: '+address+'\n')
        arquivo_ldif.write('l: '+city+'\n')
        arquivo_ldif.write('st: '+state+'\n')
        arquivo_ldif.write('uid: '+uid+'\n')
        arquivo_ldif.write('\n')
        
        var1=var1+1

if __name__ == '__main__':    
    csv2ldif()


