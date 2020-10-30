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

sql="SELECT detail_id,image_id,year,type,width,height,location,description FROM detail WHERE detail_id='{}'".format(d_id)
cur.execute(sql)


print("Content-type: text/html")    #HTML is following
print()


print("""
<html>
	<head>
		<title>The image details</title>
	</head>
	<body>
""")

items = cur.fetchall()

for row in items:

	print("""
	<div>
		<p>
		Image year: {0} <br>
		Image type: {1} <br>
		Image width: {2} <br>
		Image height: {3} <br>
		Image location: {4} <br>
		Image description: {5} <br>
		
		<a href="artist_detail.py?g_id={6}&i_id={7}&a_id={8}&d_id{9}">Detail Artist</a> &nbsp
				
		</p>
	</div>
	""".format(row[2], row[3], row[4], row[5], row[6], row[7], g_id, i_id, a_id, d_id))
	

print("""
	
	<p>
	<a href="image.py?g_id={0}"><br>Return to image list</a> &nbsp
	<a href="gallery.py">Return to Gallery</a> &nbsp
	<a href="main.py">Return to Home</a> &nbsp
	</p>
	
	</body>
</html>	
""".format(g_id))

db.close()
