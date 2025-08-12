var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.listen(5678);

app.get("/te.st", function(req, res){
  res.send("<h1>ok</h1>");
});

app.get("/param.test", function(req, res){
  var a = +req.query.a;
  var b = +req.query.b;
  var c = a + b;
  res.send(c+"");
})

app.get("/json.res.test", function(req, res){
  var a = +req.query.a;
  var b = +req.query.b;
  var c = a + b;

  var res_data = {
    "result" : c
  }

  res.setHeader = ("Access-Control-Allow-Origin", "*");
  res.send(res_data);
})
// app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
