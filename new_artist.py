#Name - Tun Myat
#ID - 51705354

import cgi

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting New Artist</H1>")

print("<b>Please type the detail of new artist<br></b>")
print("<form action='new_artist_add.py' method = 'post'>")

print("Artist Name: <input type='text' name='artist_name'><br>")
print("Artist Birth Year: <input type='text' name='artist_birth_year'><br>")
print("Artist Country: <input type='text' name='artist_country'><br>")
print("Artist Description: <input type='text' name='artist_description'><br><br><br>")
	
print("<input type='submit' value='Submit'></form>")