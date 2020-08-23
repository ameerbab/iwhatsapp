# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in iwhatsapp/__init__.py
from iwhatsapp import __version__ as version

setup(
	name='iwhatsapp',
	version=version,
	description='iWhatsapp',
	author='iWEX Infomatics',
	author_email='emails@iwex.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
