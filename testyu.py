import json
import csv
import re
def check_name(name):
    sname = name.split()
    regex = re.compile('[@_!#$%^&*()-+=`,.;<>?/\|}{~:]')
    if (len(sname)!=1):
         return False
    elif (regex.search(str(name)) == None or  bool(re.search(r'\d', str(name)))!=True):
        return False
    elif ((str(name)).islower()==False):
        return False
    else :
        return True


rows=[]
with open("pclub.csv",'r') as files:
    reader = csv.reader(files)
    for row in reader:
        rows.append(row)
        if (check_name(row[0])==True) : 
            print(row[0])



with open("students.json") as f:
    data = json.load(f)
    
for i in range(len(rows)):
    for k in range(len(data)):
        if (check_name(rows[i][0])==False  and rows[i][0]==data[k]['n']):
            print( data[k]['n'] + ',' + data[k]['i'] + ',' + data[k]['d'] + ',' + rows[i][1] + ',' + rows[i][2])



