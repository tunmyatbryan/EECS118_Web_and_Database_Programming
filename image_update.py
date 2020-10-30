#Name - Tun Myat
#ID - 51705354

import cgi
import pymysql

import cgitb

cgitb.enable()

print("Content-type: text/html")    #HTML is following
print()

FORM = cgi.FieldStorage()

i_id = FORM.getvalue("i_id")
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
	<p><a href="image_edit.py?g_id={0}&i_id={1}">Return back to edit</a></p>
	</body>
	</html>""".format(g_id, i_id))

else:
		
	sql = "UPDATE image SET title=\"{}\", link=\"{}\" WHERE image_id={}".format(FORM.getvalue("image_title"), FORM.getvalue("image_link"),i_id)
	cur.execute(sql)

	sql = "UPDATE detail SET year={}, type=\"{}\", width={}, height={}, location=\"{}\", description=\"{}\" WHERE image_id={}".format(FORM.getvalue("image_year"), FORM.getvalue("image_type"), FORM.getvalue("image_width"), FORM.getvalue("image_height"), FORM.getvalue("image_location"), FORM.getvalue("image_description"),i_id)
	cur.execute(sql)

	db.commit()

	print("""

	<html>
	<body>
	<h1>Edit Image Successfully.</h1>
		
	<p>
	<a href="image.py?g_id={0}">Return to Image List</a> &nbsp
	<a href="gallery.py">Return to Gallery List</a> &nbsp
	<a href="main.py">Return to Home Page</a> &nbsp
	</p>

	</body>
	</html>

	""".format(g_id))

db.close()