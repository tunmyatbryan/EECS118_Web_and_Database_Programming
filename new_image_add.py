#Name - Tun Myat
#ID - 51705354

import cgi
import pymysql

import cgitb

cgitb.enable()

print("Content-type: text/html")    #HTML is following
print()

FORM = cgi.FieldStorage()

g_id = FORM.getvalue("g_id")
a_name = FORM.getvalue("image_artist")

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()


sql = "SELECT artist_id FROM artist WHERE name = '{}'".format(a_name)
cur.execute(sql)

row = cur.fetchone()

if not row:
	print("""<html>
	<body>
	<h1>Artist name is not valid. Please retype again.</h1>
	<p><a href="new_image.py?g_id={}">Return back</a></p>
	</body>
	</html>""".format(g_id))
	
else:
	
	sql = "INSERT INTO detail (year, type, width, height, location, description) VALUES ({}, \"{}\", {}, {}, \"{}\", \"{}\")".format(FORM.getvalue("image_year"), FORM.getvalue("image_type"), FORM.getvalue("image_width"), FORM.getvalue("image_height"), FORM.getvalue("image_location"), FORM.getvalue("image_description"))
	cur.execute(sql)

	sql = "SELECT MAX(detail_id) FROM detail"
	cur.execute(sql)
	d_id = cur.fetchone()[0]


	sql = "INSERT INTO image (title, link, gallery_id, artist_id, detail_id) VALUES (\"{}\", \"{}\", {}, {}, {})".format(FORM.getvalue("image_title"), FORM.getvalue("image_link"), g_id, row[0], d_id)
	cur.execute(sql)
	
	sql = "SELECT MAX(image_id) FROM image"
	cur.execute(sql)
	i_id = cur.fetchone()[0]
	
	sql = "UPDATE detail SET image_id={} WHERE detail_id={}".format(i_id, d_id)
	cur.execute(sql)


	db.commit()


	print("""

	<html>
	<body>
	<h1>Added New Image Successfully.</h1>
		
	<p>
	<a href="image.py?g_id={0}">Return to Image list</a> &nbsp
	<a href="gallery.py">Return to Gallery</a> &nbsp
	<a href="main.py">Return to Home</a>
	
	</p>
	
	</body>
	</html>

	""".format(g_id))

	db.close()