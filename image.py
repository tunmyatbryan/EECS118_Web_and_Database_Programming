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

sql="SELECT image_id,title,link,gallery_id,artist_id,detail_id FROM image WHERE gallery_id='{}'".format(g_id)
cur.execute(sql)


print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>List of all the images details</title>
	</head>
	<body>
""")

items = cur.fetchall()

for row in items:
	print("""
	<div>
		<p>Image title: {0} <br>
		Image link: {1} <br>
		<img src="{1}"> &nbsp
		<a href="image_detail.py?i_id={2}&g_id={3}&a_id={4}&d_id={5}">Detail Image</a> &nbsp
		<a href="image_edit.py?i_id={2}&g_id={3}">Edit Image</a> &nbsp
		<a href="image_delete.py?i_id={2}&g_id={3}">Delete Image</a> &nbsp
		<br><br>
		</p>
	</div>
	""".format(row[1], row[2], row[0], g_id, row[4], row[5]))
	

print("""
	<br><br>
	The total number of image is {0}
	<br>
	<a href="new_image.py?g_id={1}"><br>Add New Image</a> &nbsp
	<p>
	<a href="gallery.py">Return to Gallery</a> &nbsp
	<a href="main.py">Return to Home</a> &nbsp
	</p>
	
	</body>
</html>	
""".format(len(items), g_id))

db.close()
