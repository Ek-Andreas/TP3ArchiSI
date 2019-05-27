def get_template():
    template = """
<html>
<head>
    <title>The World News</title>
</head>
    <body>
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
        <button onclick="location.href = '/addBooks';" id="myButton" class="float-left submit-button" >Add Books</button>

    </body>
</html>"""
    return template