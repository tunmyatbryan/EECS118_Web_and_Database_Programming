#Name - Tun Myat
#ID - 51705354

import cgi
import cgitb

cgitb.enable()
FORM = cgi.FieldStorage()

print("Content-type: text/html")    #HTML is following
print()

g_id = FORM.getvalue("g_id")

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting New Detail of the Gallery</H1>")

print("<form action='gallery_update.py?g_id={0}' method = 'post'>".format(g_id))

print("Edit Gallery Name: <input type='text' name='gallery_name'><br>")
print("Edit Gallery Description: <input type='text' name='gallery_description'><br><br>")
	
print("<input type='submit' value='Submit'></form>")

print("""
	<a href="gallery.py">Return to Gallery</a> &nbsp
""")