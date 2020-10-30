#Name - Tun Myat
#ID - 51705354

import cgi
import cgitb

cgitb.enable()
FORM = cgi.FieldStorage()

print("Content-type: text/html")    #HTML is following
print()

g_id = FORM.getvalue("g_id")
i_id = FORM.getvalue("i_id")

print("<H1>Requesting New Detail of the Image</H1>")

print("<form action='image_update.py?g_id={0}&i_id={1}' method = 'post'>".format(g_id, i_id))
print("Edit Image Title: <input type='text' name='image_title'><br>")
print("Edit Image link: <input type='text' name='image_link'><br>")
print("Edit Image Artist: <input type='text' name='image_artist'><br>")
print("Edit Image Year: <input type='text' name='image_year'><br>")
print("Edit Image Type: <input type='text' name='image_type'><br>")
print("Edit Image Width: <input type='text' name='image_width'><br>")
print("Edit Image Height: <input type='text' name='image_height'><br>")
print("Edit Image Location: <input type='text' name='image_location'><br>")
print("Edit Image Description: <input type='text' name='image_description'><br>")
	
print("<input type='submit' value='Submit'>")

print("</form>")

print("""

<p>
<a href="image.py?g_id={0}">Return to Image List</a> &nbsp
<a href="gallery.py">Return to Gallery</a> &nbsp
<a href="main.py">Return to Home</a> &nbsp
</p>

""".format(g_id))

