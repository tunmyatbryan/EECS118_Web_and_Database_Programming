#Name - Tun Myat
#ID - 51705354

import pymysql
import cgi
import cgitb

cgitb.enable()

FORM = cgi.FieldStorage()

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

artist_country = FORM.getvalue("artist_country")

sql="SELECT artist_id,name,birth_year,country,description FROM artist WHERE country=\"{}\"".format(artist_country)
cur.execute(sql)


print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>List of all the Artists by country</title>
	</head>
	<body>
	<h1>List of all the Artists by country</h1>
""")

for row in cur.fetchall():
	print("""
	
	<div>
		<p>
		Artist Name: {1} &nbsp
		Artist Birth Year: {2} &nbsp
		Artist country: {3} &nbsp
		Artist Description: {4} &nbsp
		
		<a href="artist_edit.py?a_id={0}">Edit</a> &nbsp
		
		<a href="artist_delete.py?a_id={0}">Delete</a> &nbsp
		
		</p>
		
	</div>
	""".format(row[0], row[1], row[2], row[3], row[4]))

print("""
	<p>
	<a href="main.py">Return to Home</a>
	</p>
	</body>
	
</html>	
""")

db.close()