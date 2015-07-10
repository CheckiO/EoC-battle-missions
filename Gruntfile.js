"use strict";

module.exports = function (grunt) {
    grunt.initConfig({
        bower_concat: {
            all: {
                dest: 'res/js/libs.js',  // Склеенный файл
                exclude: []
            }
        },
        concat: {
            main: {
                src: [
                    'source/*.js'
                ],
                dest: 'res/js/scripts.js'
            }
        },
        less: {
            main: {
                options: {
                    cleancss: true,
                    compress: true,
                    relativeUrls: true
                },
                files: {
                    'res/css/bootstrap.css': 'bower_components/bootstrap/less/bootstrap.less'
                }
            }
        },
        sass: {
            dist: {
                files: {
                    'res/css/main.css': 'source/scss/main.scss'
                }
            }
        }


    });

    grunt.loadNpmTasks('grunt-bower-concat');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-sass');

    //Эти задания будут выполнятся сразу же когда вы в консоли напечатание grunt, и нажмете Enter
    grunt.registerTask('default', ['bower_concat', "less", "sass", "concat"]);
};