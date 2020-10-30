#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting image type information</H1>")

print("<b>Please enter the type of the image<br></b>")
print("<form action='image_search_type_result.py' method = 'post'>")

print("Image Type: <input type='text' name='image_type'><br><br>")
	
print("<input type='submit' value='Search'></form>")