#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting image location</H1>")

print("<b>Please enter the location of the image<br></b>")
print("<form action='image_search_location_result.py' method = 'post'>")

print("Image location: <input type='text' name='image_location'><br><br>")
	
print("<input type='submit' value='Search'></form>")