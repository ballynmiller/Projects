var babelify = require('babelify');
var buffer = require('vinyl-buffer');
var browserify = require('browserify');
var gulp = require('gulp');
var nodemon = require('gulp-nodemon');
var source = require('vinyl-source-stream');
var watchify = require('watchify');


gulp.task('synchronize', function(){
    var stream = watchify(
        browserify({
            debug: true,
            fullPaths: false,
            entries: ['lib/js/main.jsx'],
            extensions: ['.jsx'],
            output: ['dist/js'],
            transform: [babelify]
        })
    );

    return stream.bundle()
        .on('error', function(err){
            console.log(err);
            this.emit('end');
        })
        .pipe(source('main.js'))
        .pipe(buffer())
        .pipe(gulp.dest('dist/js'))
});

gulp.task('server', ['watch'], function(){
    nodemon({
        script: 'server.js'
    });
});

gulp.task('watch', function(){
    gulp.watch('lib/js/main.jsx', ['synchronize']);
})

gulp.task('default', ['synchronize', 'watch', 'server']);
