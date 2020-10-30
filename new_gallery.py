#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting New Gallery</H1>")

print("<b>Please type the detail of new gallery<br></b>")
print("<form action='new_gallery_add.py' method = 'post'>")

print("Gallery Name: <input type='text' name='gallery_name'><br>")
print("Gallery Description: <input type='text' name='gallery_description'><br><br>")
	
print("<input type='submit' value='Submit'></form>")