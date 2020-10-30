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

sql = "UPDATE gallery SET name=\"{}\", description=\"{}\" WHERE gallery_id={}".format(FORM.getvalue("gallery_name"), FORM.getvalue("gallery_description"), g_id)
cur.execute(sql)


db.commit()


print("""

<html>
<body>
<h1>Edit Gallery Successfully.</h1>
	
<p>
<a href="gallery.py">Return to Gallery</a> &nbsp
<a href="main.py">Return to Homne</a>

</p>

</body>
</html>

""")

db.close()