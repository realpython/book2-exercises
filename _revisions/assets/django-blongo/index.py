<!DOCTYPE html>
<html lang="en">
 <head>
   <meta charset="utf-8">
   <title>Blongo: Django + Mongo</title>
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta name="description" content="">
   <meta name="author" content="">

   <!-- Le styles -->
   <link href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.5/yeti/bootstrap.min.css" rel="stylesheet">
   <style>
     body {
       padding-top: 60px;
     }
   </style>
   <script src="http://code.jquery.com/jquery-2.2.4.min.js" type="text/javascript">
    {% block extrahead %}
    {% endblock %}
   </script>
 </head>

 <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Blongo</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

   <div class="container">
    {% if latest_posts %}
      {% for post in latest_posts %}
        <h3>{{ post.title }}</h3>
        <p><em>{{ post.created_at }}</em></p>
        <p>{{ post.content }}</p>
        <br>
      {% endfor %}
    {% endif %}
   </div> <!-- /container -->

 </body>
</html>
