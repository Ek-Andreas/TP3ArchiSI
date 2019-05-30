def get_template():
    template = """
<html>

<head>
    <title>The World News :: Articles</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" >
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
</head>
   <body>
    <br>
    <div class="container">

    <div class="row" style= "margin-top:40px; padding: 0 10px;">
    <div class="col-md-6">
        <button onclick="location.href = '/add';" id="myButton" class="float-left submit-button" >Add a new Article</button>

            <div class="panel panel-primary" >
                            <div class="panel-body">

    <form action="/search" method="post">
        <input type="text" name="value">
        <input type="submit" value="Search">
    </form>
                <div class="panel-body">
                </div>
                <table class="table table-hover" id="dev-table">

                </tr>
                    <thead style="background-color : #e6e6e6;">
                        <tr>
                            <th>author</th>
                            <th>section</th>
                            <th>Status</th>
                            <th>Date</th>
                            <th>Title</th>
                        </tr>
                    </thead>
                    <tbody>
            % for row in rows:
             <tr>
                  % for cell in row:
                  <td>${cell}</td>
                  % endfor
             </tr>
             </tr>
             % endfor                    
             </tbody>
            </div>
        </div>

    </div>
</div>
</body>
</html>"""
    return template




