#Name - Tun Myat
#ID - 51705354

import cgi

print("Content-type: text/html")    #HTML is following
print()


print("""

<html>
<body>

	<script type="text/javascript">
        document.write("<center><font size=+3>");
        var day = new Date();
        var hr = day.getHours();
        if (hr >= 0 && hr < 12) 
		{
            document.write("Good Morning!");
        } 
		else if (hr == 12) 
		{
            document.write("Good Noon!");
        } 
		else if (hr >= 12 && hr <= 17) 
		{
            document.write("Good Afternoon!");
        } 
		else 
		{
            document.write("Good Evening!");
        }
		document.write("<br>Welcome to Gallery.")
		
        document.write("</font></center>");
    </script>

<p><a href="gallery.py">List all the Galleries</a></p>

<p><a href="artist.py">List all the Artists</a></p>

<p><a href="new_gallery.py">Create New Gallery</a></p>

<p><a href="new_artist.py">Create New Artist</a></p>


<p><a href="image_search_type.py">Find the images by type</a></p>

<p><a href="image_search_year.py">Find the images by a given range of creation year</a></p>

<p><a href="image_search_artist.py">Find the images by artist name</a></p>

<p><a href="image_search_location.py">Find the images by location</a></p>

<p><a href="artist_search_country.py">Find artists by country</a></p>

<p><a href="artist_search_birth.py">Find the artists by birth year</a></p>


</body>
</html>

""")