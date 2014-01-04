[![Build Status](https://travis-ci.org/rbrito/edx-dl.png?branch=master)](https://travis-ci.org/rbrito/edx-dl)


# DESCRIPTION

Simple tool to download video lectures from edx-based sites.  It requires a
Python interpreter (either version 2.x with x >= 6 or version 3.x), a recent
version of `youtube-dl` and `BeautifulSoup4`.

It is written to be platform independent and should work fine under any
Unix, Windows or MacOS X system, provided the dependencies are met.

# DEPENDENCIES

## youtube-dl

We use `youtube-dl` to download video lectures from Youtube, with the main
idea being that "we don't want to reinvent the wheel".  Make sure you have
`youtube-dl` installed in your system.  Also, since Youtube changes its
layout frequently, make sure that the version of `youtube-dl` that you have
installed is the latest. If in doubt, run `youtube-dl --update`.

You can find `youtube-dl` at <https://github.com/rg3/youtube-dl>.

## BeautifulSoup

Scrapping the web can be very silly task, but BeautifulSoup makes it so easy
:), it isn't included in the python standard library.  Make sure you have
BeautifulSoup installed.

You can install it with

    pip install beautifulsoup4

or

    easy_install beautifulsoup4.

For more info, see <http://www.crummy.com/software/BeautifulSoup/#Download>.

# Files

## edx-dl.py
Python2 implementation for edx-downloader

## edx-downloader.py
The original file written by @shk3 in/for `python3` then updated by
@emadshaaban92 using `2to3`.


# USAGE

## For Python2.x
To use `edx-dl.py`, simply excute it with 2 arguments: email and password,
as in:

    python edx-dl.py user@user.com 123456

Your downloaded videos will be placed in a new Directory called
"Downloaded".  The script is very interactive, and if you have a issue
please tell us.


## For Python3.x

The instructions are the same as for python 2 except that you should use
`edx-downloader.py` instead of `edx-dl.py`:

    python3 edx-downloader.py user@user.com 123456
