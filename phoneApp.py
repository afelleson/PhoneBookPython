#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
import sys
import json
import cgi
import cgitb
#cgitb.enable()
# the following causes a message to be written in /fifo if the python program fails
cgitb.enable(display=0, logdir="/home/fifo")

sys.path.insert(1, '/home/students/username/PhoneBookPython/') #CHANGE. I think this is the path to your 'home' in cslab: where you go when you first log in via ssh (and then the PhoneBookPython folder inside that)

from phoneBook import phoneBook # Import the phoneBook class form phoneBook.py

def fixAttr(s): # Funciton to fix a missing attribute by converting it to an empty string
  if s==None:
    return("")
  return(s)

def printHeader():
  print ("""Content-type: text/html\n""")

def main():
  printHeader()
  # the following allow debug messages to be written into /tmp
  # If you use, CHANGE file name to your username.
  #l=open("/home/fifo/username.log","a")
  #l.write("Test Message:")
  pb=phoneBook() # Rename phoneBook class to pb
  form = cgi.FieldStorage() # Class of cgi used to access submitted form data (like mode and search terms)
  if (form.getvalue("operation")): # Read user-selected mode
    operation=form.getvalue("operation")
    #]write("op:"+operation)
    search=form.getvalue("find") # Read the search terms typed by the user
    # Fix Null search parameter
    search=fixAttr(search)
    if search==None:
      search=""
    if "Last" in operation:
      pbResults=pb.findByLast(search) # Execute the appropriate function
      print(json.dumps(pbResults)) # Convert table subset output to json string & print it
    elif "First" in operation:
      pbResults=pb.findByFirst(search)
      print(json.dumps(pbResults))
    elif "Type" in operation:
      pbResults=pb.findByType(search)
      print(json.dumps(pbResults))
    elif "Add" in operation:
      first=form.getvalue("afname")
      last=form.getvalue("alname")
      phone=form.getvalue("aphone")
      ptype=form.getvalue("atype")
      first=fixAttr(first)
      last=fixAttr(last)
      phone=fixAttr(phone)
      ptype=fixAttr(ptype)
      pbResults=pb.addEntry(first,last,phone,ptype)
      print(json.dumps(pbResults))
    elif "edit" in operation:
      idnum=form.getvalue("editid")
      first=form.getvalue("editfname")
      last=form.getvalue("editlname")
      phone=form.getvalue("editphone")
      ptype=form.getvalue("edittype")
      first=fixAttr(first)
      last=fixAttr(last)
      phone=fixAttr(phone)
      ptype=fixAttr(ptype)
      pbResults=pb.editEntry(idnum,first,last,phone,ptype)
      print(pbResults)
      print(json.dumps(pbResults))
    elif "delete" in operation:
      rid=form.getvalue("deleteid")
      pbResults=pb.delete(rid)
      print(json.dumps(pbResults))
    else:
      print("Error,Bad command:"+operation)
      #l.write("Error,Bad command:"+operation)
    #l.close()
  else:
    print("Error in submission")

main()
