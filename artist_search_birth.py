#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting Artist birth year information</H1>")

print("<b>Please enter the Artist birth year<br></b>")
print("<form action='artist_search_birth_result.py' method = 'post'>")

print("Artist Birth Year: <input type='text' name='artist_birth_year'><br><br>")
	
print("<input type='submit' value='Search'></form>")