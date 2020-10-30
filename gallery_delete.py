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


db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()


sql="SELECT image_id FROM image WHERE gallery_id='{}'".format(g_id)
cur.execute(sql)

detail = cur.fetchone()

sql = "DELETE FROM gallery WHERE gallery_id={}".format(g_id)
cur.execute(sql)

sql = "DELETE FROM image WHERE gallery_id={}".format(g_id)
cur.execute(sql)


if detail:
	sql = "DELETE FROM detail WHERE image_id={}".format(detail[0])
	cur.execute(sql)

db.commit()

print("""

<html>
<body>
<h1>Delete Whole gallary (including images) Successfully.</h1>
	
<p>

<a href="gallery.py">Return to Gallery List</a> &nbsp
<a href="main.py">Return to Home Page</a> &nbsp
</p>

</body>
</html>

""")

db.close()