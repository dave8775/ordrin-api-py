import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

import sys
if not (sys.version_info.major == 2 and sys.version_info.minor == 7):
    print "This package only works with Python 2.7"
    exit()

setup(
  name="ordrin",
  version='0.1.7',
  packages=['ordrin', 'ordrindemo'],
  py_modules=['distribute_setup'],
  description="Ordr.in API Client",
  author="Ordr.in",
  author_email="tech@ordr.in",
  url="https://github.com/ordrin/api-py",
  install_requires=['requests>=0.13.1'],
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Development Status :: 4 - Beta",
    "Topic :: Software Development",
    "Topic :: Internet"],
  scripts=('ordrindemo/ordrin_api_demo.py',))
