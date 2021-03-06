import os

from setuptools import setup, find_packages
import os, fnmatch

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def getScripts():
    x = []
    for (dirpath, dirnames, filenames) in os.walk('tools'):
        x.extend(os.path.join(dirpath,f) for f in filenames)
    return x

setup(
    name = "lain",
    version = "0.1",
    author = "Fabian Yamaguchi",
    author_email = "fyamagu@gwdg.de",
    description = "An evaluation framework for vulnerability recognition in C/C++ code",
    license = "GPLv3",
    url = "http://github.com/fabsx00/lain",
    long_description = read('README.md'),
    packages = find_packages(),
    scripts = getScripts(),
    zip_safe = False
)
