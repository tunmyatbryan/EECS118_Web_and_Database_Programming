#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting image artist</H1>")

print("<b>Please enter the artist of the image<br></b>")
print("<form action='image_search_artist_result.py' method = 'post'>")

print("Image artist: <input type='text' name='image_artist'><br><br>")
	
print("<input type='submit' value='Search'></form>")