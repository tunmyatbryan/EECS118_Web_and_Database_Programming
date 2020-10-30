#Name - Tun Myat
#ID - 51705354

import cgi
import pymysql

import cgitb

cgitb.enable()

print("Content-type: text/html")    #HTML is following
print()

FORM = cgi.FieldStorage()


db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

sql = "INSERT INTO gallery (name, description) VALUES (\"{}\", \"{}\")".format(FORM.getvalue("gallery_name"), FORM.getvalue("gallery_description"))
cur.execute(sql)

db.commit()


print("""

<html>
<body>
<h1>Added New Gallery Successfully.</h1>


<p><a href="gallery.py">Return to Gallery</a></p>
<p><a href="main.py">Return to Home</a></p>

</body>
</html>

""")

db.close()