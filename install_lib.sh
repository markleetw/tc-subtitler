#!/bin/bash
BASEDIR=$(dirname $0)
cd $BASEDIR/g2butf8/lib/jianfan-0.0.1
python setup.py build
python setup.py install
cd $BASEDIR/g2butf8/lib/python2-chardet-2.0.1
python setup.py build
python setup.py install
