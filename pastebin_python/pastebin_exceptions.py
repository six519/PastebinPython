"""
.. module:: pastebin_exceptions
	:sypnosis: This module contains all of the exceptions

.. moduleauthor:: Ferdinand Silva <ferdinandsilva@ferdinandsilva.com>

"""
class PastebinBadRequestException(Exception):
	pass

class PastebinNoPastesException(Exception):
	pass

class PastebinFileException(Exception):
	pass