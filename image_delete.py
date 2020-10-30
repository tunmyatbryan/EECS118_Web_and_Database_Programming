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

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

sql = "DELETE FROM image WHERE image_id={}".format(i_id)
cur.execute(sql)

db.commit()

print("""

<html>
<body>
<h1>Delete Image Successfully.</h1>
	
<p>
<a href="image.py?g_id={0}">Return Image List</a> &nbsp
<a href="gallery.py">Return to Gallery List</a> &nbsp
<a href="main.py">Return to Home Page</a> &nbsp
</p>

</body>
</html>

""".format(g_id))

db.close()