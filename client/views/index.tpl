<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <style>
      .root {
        width: 100%;
        height: 100%;
      }
    </style>
    <title><%= htmlWebpackPlugin.options.title || 'Github users browser' %></title>
  </head>
  <body>
    <div class="root" id="root"></div>
  </body>
</html>
