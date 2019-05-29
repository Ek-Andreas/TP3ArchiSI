def get_template():
    template = """
<html>

<head>
    <title>Search for a book</title>
</head>
    <body>
    <br>
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
        <button onclick="location.href = '/';" id="myButton" class="float-left submit-button" >Return Home</button>

    </body>
</html>"""
    return template