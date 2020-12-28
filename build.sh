#!/bin/bash

PY=$(which python3)
PELICAN="pelican"
PELICANOPTS=""

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py
PUBLISHDIR=~/.stderr.cz

GITHUBSSH="git@github.com:jakubjedelsky/stderr.cz"
COMMITCOMMENT="Publishing."

function print_help {
    cat << EOF
Build script for a pelican web site. Based on thr original Makefile.

Usage: $0 [command]

Commands:
  help          print this help and exit
  html          (re)generate the web site
  clean         remove the generated files
  regenerate    regenerate files upon modification, exit with ^C
  serve         serve site at http://localhost:8000, exit with ^C
  publish       publish at (my) github

EOF
}

function clean {
    if [ -d $OUTPUTDIR ] ; then
        find $OUTPUTDIR -mindepth 1 -delete
    fi
}

function html {
    clean
    $PELICAN $INPUTDIR -o $OUTPUTDIR -s $CONFFILE $PELICANOPTS
}

function regenerate {
    clean
    $PELICAN -r $INPUTDIR -o $OUTPUTDIR -s $CONFFILE $PELICANOPTS
}

function serve {
    if [ -d $OUTPUTDIR ] ; then
        pushd $OUTPUTDIR > /dev/null
        $PY -m pelican.server
        popd > /dev/null
    else
        echo "There is no output directory. Try to run '$0 html' first."
        exit 2
    fi
}

function publish {
    if [ ! -d $PUBLISHDIR ] ; then
        mkdir -p $PUBLISHDIR
        git clone -b gh-pages $GITHUBSSH $PUBLISHDIR
    else
        pushd $PUBLISHDIR > /dev/null
        git pull origin gh-pages
        popd > /dev/null
    fi
    $PELICAN $INPUTDIR -o $PUBLISHDIR -s $CONFFILE $PELICANOPTS
    pushd $PUBLISHDIR > /dev/null
    rm -rf author category tag tags.html
    git add -A
    git commit -m "$COMMITCOMMENT"
    git push origin gh-pages
    popd > /dev/null
}

case "$1" in
    help)
        print_help && exit 0
        ;;
    html)
        $1
        ;;
    clean)
        $1
        ;;
    regenerate)
        $1
        ;;
    serve)
        $1
        ;;
    publish)
        $1
        ;;
    *)
        echo $"Usage: $0 {help|html|clean|regenerate|serve|publish}"
        exit 2
esac
