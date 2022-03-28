# A single class called phoneBook that connects to, searches, and edits a mysql database

import mysql.connector

class phoneBook:
  def __init__(self): # Connect to the database using login info
    # View databases at http://cslab.kenyon.edu/phpmyadmin/index.php?db=felleson1&target=db_structure.php
    HOST = "localhost"
    USER = "yourUsername" # CHANGE THIS
    DB = "yourUsername" # CHANGE THIS. This is the parent of the table you want to access made, shown on the left of the phpmyadmin page. Probably your username, but you should also have access to a database named after your team.
    PASS= "yourStudentID" # CHANGE THIS
    self.mydb = mysql.connector.connect( # Uses the connect function from the mysql.connector library to get access to your database. Makes that database into an attribute (named mydb) of the object 'self'
      host=HOST,
      user=USER,
      passwd=PASS,
      database=DB,
      auth_plugin='mysql_native_password' # ?? This is an optional argument, not sure why we're using it here
    )
    return

  def findByLast(self,last):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM PhoneBook WHERE Last like '%"+last+"%'"); # SQL code that manipulates the table PhoneBook in your database
    myresult = mycursor.fetchall()
    return(myresult)

  def findByFirst(self,first):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM PhoneBook WHERE First like '%"+first+"%'");
    myresult = mycursor.fetchall()
    return(myresult)

  def delete(self,idnum):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("DELETE FROM PhoneBook WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")

  def addEntry(self,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("INSERT INTO PhoneBook(First,Last,Phone,Type) VALUES ('"+first+"','"+last+"','"+phone+"','"+ptype+"')")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")

  def editEntry(self,idnum,first,last,phone,ptype):
    mycursor = self.mydb.cursor()
    try:
      mycursor.execute("UPDATE PhoneBook SET First = '"+first+"', Last ='"+last+"', Phone ='"+phone+"', Type ='"+ptype+"' WHERE ID='"+idnum+"'")
      self.mydb.commit()
    except Exception as e:
      return "Error,"+ str(e)
    finally:
      self.mydb.close()
    return ("success")
