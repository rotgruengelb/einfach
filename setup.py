from setuptools import setup, find_packages
import codecs
import os
from einfach import __version__, __license__

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = __version__
DESCRIPTION = 'A collection of useful code "snippets"'
LONG_DESCRIPTION = 'A collection of useful code "snippets" or "helpers" that implement little but annoying to add things for you'

# Setting up
setup(
    name = "einfach",
    version = VERSION,
    author = "rotgruengelb (Daniel)",
    author_email = "<code@rotgruengelb.net>",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = LONG_DESCRIPTION + "\n" + long_description,
    packages = find_packages(),
    license = __license__,
    url="https://github.com/rotgruengelb/einfach",
    project_urls = {
        'Source': 'https://github.com/rotgruengelb/einfach',
        'Issues': 'https://github.com/rotgruengelb/einfach/issues',
        'Wiki': 'https://github.com/rotgruengelb/einfach/wiki/Features'
    },
    install_requires = [],
    keywords = ['python', 'helper', 'helpers', 'help', 'easy code', 'ease of use', "snippets", "code snippets"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces"
    ]
)
