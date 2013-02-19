"""
.. module:: pastebin_python.pastebin_constants
	:synopsis: This module contains the constants that can be used in the :meth:`pastebin_python.pastebin.PastebinPython.__processPost` , :meth:`pastebin_python.pastebin.PastebinPython.createPaste` and :meth:`pastebin_python.pastebin.PastebinPython.createPasteFromFile`

.. moduleauthor:: Ferdinand Silva <ferdinandsilva@ferdinandsilva.com>

"""
PASTEBIN_API_URL = "http://pastebin.com/api/"
PASTEBIN_API_POST_URL = "%s%s" % (PASTEBIN_API_URL, "api_post.php")
PASTEBIN_API_LOGIN_URL = "%s%s" % (PASTEBIN_API_URL, "api_login.php")

PASTE_PUBLIC = 0
PASTE_UNLISTED = 1
PASTE_PRIVATE = 2

EXPIRE_NEVER = "N"
EXPIRE_10_MIN = "10M"
EXPIRE_1_HOUR = "1H"
EXPIRE_1_DAY = "1D"
EXPIRE_1_MONTH = "1M"