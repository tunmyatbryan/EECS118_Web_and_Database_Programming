#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting Artist country information</H1>")

print("<b>Please enter the Artist country<br></b>")
print("<form action='artist_search_country_result.py' method = 'post'>")

print("Artist country: <input type='text' name='artist_country'><br><br>")
	
print("<input type='submit' value='Search'></form>")