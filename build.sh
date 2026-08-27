#!/bin/bash

BASEDIR=$(cd "$(dirname "$0")" && pwd)
PY=$BASEDIR/.venv/bin/python3
PELICAN=$BASEDIR/.venv/bin/pelican
PELICANOPTS=""

INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

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

Publishing is handled by .github/workflows/publish.yml on push to master.

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
        $PELICAN -l -p 8000 -o $OUTPUTDIR -s $CONFFILE
    else
        echo "There is no output directory. Try to run '$0 html' first."
        exit 2
    fi
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
    *)
        echo $"Usage: $0 {help|html|clean|regenerate|serve}"
        exit 2
esac
