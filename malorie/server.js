// Create Server
var express = require('express');
var app = express();

// Response is index.html file
app.get("/", function(req, res){
    res.sendFile("index.html", { root: __dirname });
});

// run server
var server = app.listen(8000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log("Sever listening @ http://%s:%s", host, port);
});
