#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name='schematics-wtf',
  version='0.1.0-alpha',
  license='BSD',
  description='Schematics Model to WTForm converter',
  url='http://github.com/ryanolson/schematics-wtf',
  packages=['schematics_wtf'],
  install_requires = [
    'schematics>=0.8.0-alpha',
    'wtforms'
  ],
  dependency_links = [
    'https://github.com/j2labs/schematics/tarball/master#egg=schematics-0.8.0-alpha'
  ],
  classifiers=[
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: Other/Proprietary License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
  ],
)
