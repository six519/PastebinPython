import pastebin_python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=pastebin_python.__app_name__,
    version=pastebin_python.__version__,
    description=pastebin_python.__description__,
    author=pastebin_python.__author__,
    author_email=pastebin_python.__author_email__,
    packages=['pastebin_python'],
    url=pastebin_python.__app_url__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url=pastebin_python.__download_url__,
)