# I don't think this is used in the online app, just for debugging

import mysql.connector
import json # Import the json python package

from phoneBook import phoneBook # Imports the phoneBook class from phoneBook.py (i think). That doesn't include the import mysql.connector line in phoneBook.py, so that's why that library is loaded above

pb=phoneBook() # Rename the class phoneBook to pb

o=input("Select an option (1-serach first, 2-search last, 3-search type, 4-add, 5-edit, 6-delete, 7-end): ")
while o!='7':
  if o=='1':
    search=input("First name: ")
    pbResults=pb.findByFirst(search) # Execute the findByFirst function from the phoneBook (pb) class
    print(json.dumps(pbResults)) # Print the list of tuples that funciton returns (the subset of the table you searched for). use json.dumps to convert the Python object (list of tuples) into a json string first because... it looks slightly different that way.
  elif o=='2':
    search=input("Last name: ")
    pbResults=pb.findByLast(search)
    print(json.dumps(pbResults))
  elif o=='3':
    search=input("Type: ")
    pbResults=pb.findByType(search)
    print(json.dumps(pbResults))
  elif o=='4':
    first=input("First: ")
    last=input("Last: ")
    phone=input("Phone: ")
    ptype=input("Type: ")
    pbResults=pb.addEntry(first,last,phone,ptype)
    print(json.dumps(pbResults))
  elif o=='5':
    idnum=input("ID: ")
    first=input("First: ")
    last=input("Last: ")
    phone=input("Phone: ")
    ptype=input("Type: ")
    pb.editEntry(idnum,first,last,phone,ptype)
    pbResults=printResults(pbResults)
    print(json.dumps(pbResults))
  elif o=='6':
    rid=form.getvalue("deleteid")
    pbResults=pb.delete(rid)
    print(json.dumps(pbResults))
  else:
    print("Error,Bad command:"+o)
  o=input("Select an option (1-serach first, 2-search last, 3-search type, 4-add, 5-edit, 6-delete, 7-end): ")
