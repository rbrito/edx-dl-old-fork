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
    from urllib2 import (HTTPCookieProcessor, Request, urlopen,
                         build_opener, install_opener)
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import (HTTPCookieProcessor, Request, urlopen,
                                build_opener, install_opener)
