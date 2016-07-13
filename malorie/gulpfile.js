var babelify = require('babelify');
var browserify = require('browserify');
var browserSync = require('browser-sync').create();
var buffer = require('vinyl-buffer');
var clean = require('gulp-clean-css');
var gulp = require('gulp');
var less = require('gulp-less');
var nodemon = require('gulp-nodemon');
var path = require('path');
var source = require('vinyl-source-stream');
var watchify = require('watchify');
var rt = require('gulp-react-templates');
var templates = require('react-templatify');

gulp.task('synchronize', function(){
    var stream = watchify(
        browserify({
            debug: true,
            fullPaths: false,
            entries: ['lib/js/main.jsx'],
            extensions: ['.jsx'],
            output: ['dist/js'],
            transform: [templates, babelify]
        })
    );

    return stream.bundle()
        .on('error', function(err){
            console.log(err);
            this.emit('end');
        })
        .pipe(source('main.js'))
        .pipe(buffer())
        .pipe(gulp.dest('dist/js'));
});

gulp.task('rt', function(){
    gulp.src('lib/templates/**/*.rt')
        .pipe(rt())
        .pipe(gulp.dest('dist/templates'));
});

gulp.task('html', ['rt', 'images', 'convert-less'], function(){
    gulp.src("lib/**/*.html")
        .pipe(gulp.dest('dist/'));
});

gulp.task('images', function(){
    gulp.src("lib/img/*")
        .pipe(gulp.dest('dist/img'));
});

gulp.task('server', ['html'], function(){
    nodemon({
        script: 'server.js'
    });
});

gulp.task('convert-less', function(){
    gulp.src("lib/less/**/*.less")
        .pipe(less({
            paths: [path.join(__dirname, 'less', 'includes')]
        }))
        .pipe(clean())
        .pipe(gulp.dest('dist/css'));
});

gulp.task('browser-sync', function(){
    browserSync.watch('dist/**/*.*').on("change", browserSync.reload);
    browserSync.init({
        proxy: "localhost:3000",
        port: 4000
    });
});

gulp.task('watch', ['browser-sync'], function(){
    gulp.watch('lib/**/*.less', ['convert-less']);
    gulp.watch('lib/**/*.html', ['html']);
    gulp.watch('lib/**/*.rt', ['rt']);
    gulp.watch('lib/**/*.{png|jpg|jpeg}', ['images']);
    gulp.watch('lib/**/*.jsx', ['synchronize']);
});

gulp.task('default', ['synchronize', 'watch', 'html', 'images', 'server']);
