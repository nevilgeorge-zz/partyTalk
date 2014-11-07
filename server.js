// var connect = require('connect');
// var serveStatic = require('serve-static');
// var app = connect();
// app.use(serveStatic('angularjs'));
// app.listen(3000);

var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic(__dirname)).listen(8080);