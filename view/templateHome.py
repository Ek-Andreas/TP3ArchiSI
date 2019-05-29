def get_template():
    template = """
<html>

<head>
    <title>The World News</title>
</head>
    <body>
    <br>
    <button onclick="location.href = '/addBooks';" id="myButton" class="float-left submit-button" >New</button>
<form action="/searchBooks" method="post">
        <input type="text" name="value">
        <input type="submit" value="Search">
    </form>
    <table>
        <tr>
            <td>title</td><td>author</td><td>date</td><td>section</td>
             % for row in rows:
             <tr>
                  % for cell in row:
                  <td>${cell}</td>
                  % endfor
             </tr>
             </tr>
             % endfor
        </table>
        
    </body>
</html>"""
    return template