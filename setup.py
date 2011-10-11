#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, Mike Taylor
#
# This file is part of statio released under MIT license.
# See the LICENSE for more information.

from setuptools import setup, find_packages

import statio as pkg

name = pkg.__name__

setup(name=pkg.__name__,
      version=pkg.__version__,
      license="MIT",
      description=pkg.__doc__,
      long_description=open('README.rst', 'r').read(),
      author=pkg.__author__,
      author_email=pkg.__email__,
      url=pkg.__homepage__,
      packages=find_packages(),
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                  ],
     )