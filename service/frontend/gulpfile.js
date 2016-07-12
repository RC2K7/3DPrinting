// Define destination directory
var target = '../../public/dist'

// Register Plugins
var gulp = require('gulp'); 
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');

// Compile Sass
gulp.task('sass', function() {
    return gulp.src('styles/*.scss')
        .pipe(sass({
            outputStyle: 'compressed'
        }))
        .pipe(gulp.dest(target + '/css'));
});

// Compile CoffeeScript

// Concatenate & Minify JS
gulp.task('scripts', function() {
    return gulp.src('scripts/*.js')
        .pipe(uglify())
        .pipe(gulp.dest(target + '/js'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('scripts/*.js', ['scripts']);
    gulp.watch('styles/**/*.scss', ['sass']);
});

// Default Task
gulp.task('default', ['sass', 'scripts', 'watch']);