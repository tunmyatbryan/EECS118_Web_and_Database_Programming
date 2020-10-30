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

g_id = FORM.getvalue("g_id")
i_id = FORM.getvalue("i_id")
a_id = FORM.getvalue("a_id")
d_id = FORM.getvalue("d_id")

sql="SELECT artist_id,name,birth_year,country,description FROM artist WHERE artist_id='{}'".format(a_id)
cur.execute(sql)

print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>The artist details</title>
	</head>
	<body>
""")

items = cur.fetchall()

for row in items:

	print("""
	<div>
		<p>
		Artist name: {0} <br>
		Artist birth_year: {1} <br>
		Artist country: {2} <br>
		Artist description: {3} <br>
				
		</p>
	</div>
	""".format(row[1], row[2], row[3], row[4]))
	

print("""
	
	<p>
	<a href="image.py?g_id={0}">Return to image list</a> &nbsp
	<a href="gallery.py">Return to Gallery</a> &nbsp
	<a href="main.py">Return to Home</a> &nbsp
	</p>
	
	</body>
</html>	
""".format(g_id))

db.close()
