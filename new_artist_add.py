#Name - Tun Myat
#ID - 51705354

import cgi
import pymysql

print("Content-type: text/html")    #HTML is following
print()

FORM = cgi.FieldStorage()


db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'gallery')
cur = db.cursor()

sql = "INSERT INTO artist (name, birth_year, country, description) VALUES (\"{}\", {}, \"{}\", \"{}\")".format(FORM.getvalue("artist_name"), FORM.getvalue("artist_birth_year"), FORM.getvalue("artist_country"), FORM.getvalue("artist_description"))
cur.execute(sql)

db.commit()


print("""

<html>
<body>
<h1>Added New Artist Successfully.</h1>
	
<p><a href="main.py">Return to Home</a></p>

</body>
</html>

""")

db.close()