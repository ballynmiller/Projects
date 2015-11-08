// Create Server
var express = require('express');
var app = express();

app.use(express.static('dist'));

// Response is index.html file
app.get("/", function(req, res){
    res.sendFile("index.html", { root: __dirname });
});

// run server
var server = app.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log("Server listening @ http://%s:%s", host, port);
});
