<html>
    <head>
        <title>Edit {{type}}</title>
    </head>
    <body>
        <h1>{{type}}</h1>
        <form action="" method="POST">
        <textarea type="text" name="data" cols="100" rows="50">{{data}}</textarea><br>
        <input type="hidden" name="type" value="{{type}}">
        <input type="submit" value="save">
        </form>
    </body>
</html>