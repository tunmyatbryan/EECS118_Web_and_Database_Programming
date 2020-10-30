#Name - Tun Myat
#ID - 51705354

import pymysql
import cgi

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

sql="SELECT gallery_id,name,description FROM gallery"
cur.execute(sql)


print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>List of all the galleries</title>
	</head>
	<body>
	<h1>The list of all the galleries</h1>
""")

for row in cur.fetchall():
	print("""
	
	<div>
		<p>Gallery Name: {0} &nbsp
		Description: {1} &nbsp
		
		<a href="image.py?g_id={2}">View</a> &nbsp
		
		<a href="gallery_edit.py?g_id={2}">Edit</a> &nbsp
		
		<a href="gallery_delete.py?g_id={2}">Delete</a> &nbsp
		
		</p>
		
	</div>
	""".format(row[1], row[2], row[0]))

print("""
	<p>
	<a href="new_gallery.py">Add New Gallery</a> &nbsp
	<a href="main.py">Return to Home</a>
	</p>
	</body>
	
</html>	
""")

db.close()
