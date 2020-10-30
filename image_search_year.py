#Name - Tun Myat
#ID - 51705354

print("Content-type: text/html")    #HTML is following
print()


print("<H1>Requesting image type rage of creation year</H1>")

print("<b>Please enter the rage of the image creation year<br></b>")
print("<form action='image_search_year_result.py' method = 'post'>")

print("From start year: <input type='text' name='image_year_start'>")
print("to end year: <input type='text' name='image_year_end'><br><br>")
	
print("<input type='submit' value='Search'></form>")