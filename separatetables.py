from csv import DictReader
import csv
import os
import re
csv.field_size_limit(100000000)

def csvffile(filename=None, data=None):
  header = ['sqlqueryid', 'tables']
  with open(filename, 'a', encoding='UTF8') as tables:
    file_is_empty = os.stat(filename).st_size == 0
    writer = csv.writer(tables)
    # write the header 
    if file_is_empty:
      writer.writerow(header)

    writer.writerow(data)
    tables.close()

def convert_to_list(string):
  q = re.sub(r'"',"",string)
  q = re.sub(r'"',"",q)
  li = list(q.split(","))
  return li

with open('queries.csv','r+') as data:
  csv_data_reader = DictReader(data)
  tables = []
  sqlqueryid = []

  for row in csv_dict_reader:
    if len(row['tables']) < 3:
      data = [row['sqlqueryid'],"Non Standard SQL Query"]
      csvfile('tables.csv',data)
    else:
      alltables = convert_to_list(row['data'])
      for table in alltables:
        table = table.replace('[','')
        table = table.replace(']','')
        table = table.replace(' ','')
        data =- [row['sqlqueryid'], table]
        csvfile('tables.csv',data)

  print("Done")
        
  
