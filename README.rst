PastebinPython
==============

A complete http://pastebin.com API wrapper for Python

Sample Usage
============
::

	"""
	Creating paste from file...

	"""
	from pastebin_python import PastebinPython
	from pastebin_python.pastebin_exceptions import PastebinBadRequestException, PastebinNoPastesException, PastebinFileException
	from pastebin_python.pastebin_constants import PASTE_PUBLIC, EXPIRE_10_MIN
	from pastebin_python.pastebin_formats import FORMAT_NONE, FORMAT_PYTHON, FORMAT_HTML

	pbin = PastebinPython(api_dev_key='<unique api key>')

	try:
		pbin.createAPIUserKey('<username>','<password>')
		print pbin.createPasteFromFile('/home/six519/Downloads/email.html', 'Email format testing 2...', FORMAT_HTML, PASTE_PUBLIC, EXPIRE_10_MIN)
	except PastebinBadRequestException as e:
		print e.message
	except PastebinFileException as e:
		print e.message

Code Documentation
==================

You can read the documentation at: http://pythonhosted.org/pastebin_python/

