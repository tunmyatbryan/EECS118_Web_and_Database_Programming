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

i_location = FORM.getvalue("image_location")


print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>Search Result of all the images by artist name</title>
	</head>
	<body>
""")



sql="SELECT image_id FROM detail WHERE location=\"{}\"".format(i_location)
cur.execute(sql)


for row in cur.fetchall():
	sql="SELECT title,link,gallery_id,artist_id,detail_id FROM image WHERE artist_id={}".format(row[0])
	cur.execute(sql)
	
	image = cur.fetchone()
	if not image:
		continue

	print("""
	<div>
		<p>Image title: {0} <br>
		Image link: {1} <br>
		<img src="{1}"> &nbsp
		<a href="image_detail.py?i_id={5}&g_id={2}&a_id={3}&d_id={4}">Detail Image</a> &nbsp
		<a href="image_edit.py?i_id={5}&g_id={3}">Edit Image</a> &nbsp
		<a href="image_delete.py?i_id={5}&g_id={2}">Delete Image</a> &nbsp
		<br><br>
		</p>
	</div>
	""".format(image[0], image[1], image[2], image[3], image[4], row[0]))
	

print("""

	<p>
	<a href="main.py">Return to Home</a> &nbsp
	</p>
	
	</body>
</html>	
""")

db.close()
