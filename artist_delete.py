#Name - Tun Myat
#ID - 51705354

import cgi
import pymysql

import cgitb

cgitb.enable()

print("Content-type: text/html")    #HTML is following
print()

FORM = cgi.FieldStorage()

a_id = FORM.getvalue("a_id")

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

sql = "DELETE FROM artist WHERE artist_id={}".format(a_id)
cur.execute(sql)

db.commit()

print("""

<html>
<body>
<h1>Delete Artist Successfully.</h1>
	
<p>

<a href="artist.py">Return to Artist List</a> &nbsp
<a href="main.py">Return to Home Page</a> &nbsp
</p>

</body>
</html>

""")

db.close()