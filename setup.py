import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
setup(
  name="ordrin",
  version='0.0.1',
  packages=['ordrin']
  description="Ordr.in API Client",
  author="Ordr.in",
  author_email="tech@ordr.in",
  url="https://github.com/ordrin/api-py",
  install_requires=['requests'],
  classifiers=[
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Development Status :: 4 - Beta",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet"])
