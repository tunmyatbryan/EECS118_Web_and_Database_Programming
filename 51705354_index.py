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



<p><center><a href="main.py">Enter the Gallery</a></center></p>



</body>
</html>

""")