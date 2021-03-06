import sqlite3 as sqlite
	
try:
	from sqlite import encode, decode
except ImportError:
	import base64
	sqlite.encode = base64.encodestring
	sqlite.decode = base64.decodestring
else:
	sqlite.encode = encode
	sqlite.decode = decode


#connect to the database
conn = sqlite.connect('./app_database.db')
c = conn.cursor()

#create table PCID
conn.execute('''CREATE TABLE IF NOT EXISTS PCID
   (PCID 			  	  INT    NOT NULL,
   first_name             TEXT    NOT NULL,
   family_name       	  TEXT    NOT NULL,
   PRIMARY KEY (PCID));''')

#create table CHECKIN
conn.execute('''CREATE TABLE IF NOT EXISTS CHECKIN
   (No_to 			  	  INT    NOT NULL,
   code           		  INT    NOT NULL,
   PRIMARY KEY (No_to));''')

#create table CONTENT
conn.execute('''CREATE TABLE IF NOT EXISTS CONTENT
   (ContentID 			  	  INT    NOT NULL,
   PCID           		      INT    NOT NULL,
   timestamp				  INT    NOT NULL,
   title					  TEXT   NOT NULL,
   content					  TEXT   NOT NULL,
   imageID					  INT    NOT NULL,
   lat						  REAL   NOT NULL,
   lon						  REAL   NOT NULL,
   PRIMARY KEY (ContentID),
   FOREIGN KEY(PCID) REFERENCES PCID(PCID),
   FOREIGN KEY(imageID) REFERENCES IMAGE(imageID));''')
   
#create table IMAGE
conn.execute('''CREATE TABLE IF NOT EXISTS IMAGE
   (imageID 			  	  INT    NOT NULL,
   image					  BLOB   NOT NULL,
   PRIMARY KEY (imageID));''')
   
PCID = 1234
first_name = 'Sheldon'
family_name = 'Cooper'
code = 3333
No_to = 123456789
ContentID = 2222
timestamp = 134523219442
title = 'This is a test'
content = 'Ok, this is my content'
imageID = 9999
lat = 37.85
lon = -122.78
try:
	c.execute("INSERT INTO PCID VALUES (?,?,?)",\
	 (PCID, first_name, family_name))
except:
	pass

try: 
	c.execute("INSERT INTO CHECKIN VALUES (?,?)",\
	 (No_to, code))
except:
	pass

try:
	c.execute("INSERT INTO CONTENT VALUES (?,?,?,?,?,?,?,?)",\
	 (ContentID, PCID, timestamp, title, content, imageID, lat, lon))
except:
	pass
	
imagedata = open('Happy_cat.jpg', "rb").read()	 

try:
	c.execute("INSERT INTO IMAGE VALUES (?,?)",\
	 (imageID, sqlite.encode(sqlite.Binary(imagedata))))
except:
	pass
	  
conn.commit()

