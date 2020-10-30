#Name - Tun Myat
#ID - 51705354

import cgi
import cgitb

cgitb.enable()
FORM = cgi.FieldStorage()

print("Content-type: text/html")    #HTML is following
print()

g_id = FORM.getvalue("g_id")

print("<H1>Requesting New Image For Gallery</H1>")

print("<form action='new_image_add.py?g_id={0}' method = 'post'>".format(g_id))
print("New Image Title: <input type='text' name='image_title'><br>")
print("New Image link: <input type='text' name='image_link'><br>")
print("New Image Artist: <input type='text' name='image_artist'><br>")
print("New Image Year: <input type='text' name='image_year'><br>")
print("New Image Type: <input type='text' name='image_type'><br>")
print("New Image Width: <input type='text' name='image_width'><br>")
print("New Image Height: <input type='text' name='image_height'><br>")
print("New Image Location: <input type='text' name='image_location'><br>")
print("New Image Description: <input type='text' name='image_description'><br>")
	
print("<input type='submit' value='Submit'>")

print("</form>")

print("""

<p>
<a href="image.py?g_id={0}">Return to Image List</a> &nbsp
<a href="gallery.py">Return to Gallery</a> &nbsp
<a href="main.py">Return to Home</a> &nbsp
</p>

""".format(g_id))

