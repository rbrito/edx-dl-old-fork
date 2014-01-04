"""
Minor compatibility module for Python 2 and Python 3.

This avoids the need of the `six` module.
"""

# cookielib
try:
    import cookielib
except ImportError:
    import http.cookiejar as cookielib

# urllib, urllib2
try:
    from urllib import urlencode
    from urllib2 import HTTPCookieProcessor
    from urllib2 import Request
    from urllib2 import urlopen
    from urllib2 import build_opener
    from urllib2 import install_opener
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import HTTPCookieProcessor
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.request import build_opener
    from urllib.request import install_opener
